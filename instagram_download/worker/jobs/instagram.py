import json
from typing import Any, Dict

import requests
from bs4 import BeautifulSoup

from instagram_download.constants import BASE_URL, FIREFOX, INSTAGRAM_APPLE, LOGIN_URL
from instagram_download.utils.logger import logger


class InstagramScaper:
    def __init__(self) -> None:
        self.session = requests.Session()

    def login(self, username: str, password: str):
        """Logs in to instagram."""
        self.session.headers.update({"Referer": BASE_URL, "user-agent": INSTAGRAM_APPLE})
        req = self.session.get(BASE_URL)

        self.session.headers.update({"X-CSRFToken": req.cookies["csrftoken"]})

        login_data = {"username": username, "password": password}
        login = self.session.post(LOGIN_URL, data=login_data, allow_redirects=True)
        self.cookies = login.cookies
        login_text = json.loads(login.text)
        if login_text.get("authenticated") and login.status_code == 200:
            self.session.headers.update({"user-agent": FIREFOX})
        else:
            logger.error("Login failed for %s", username)

    def _request_url(self, url) -> bytes:
        try:
            response = self.session.get(url, cookies=self.cookies)
            response.raise_for_status()
        except requests.HTTPError:
            raise requests.HTTPError("Received non-200 status code.")
        except requests.RequestException:
            raise requests.RequestException
        else:
            return response.content

    @staticmethod
    def extract_json(html) -> dict:
        soup = BeautifulSoup(html, "html5lib")
        script = str(soup.body.find_all("script")[11])
        raw_string = script[script.find("{") :].replace(");</script>", "")
        return json.loads(raw_string)

    def get_media(self, url: str) -> dict:
        try:
            response = self._request_url(url)
            json_data = self.extract_json(response)
            media = json_data["graphql"]["shortcode_media"]
        except Exception as e:
            logger.error("ERROR: %s", e)
            raise e
        return media

    def get_owner(self, media: dict) -> dict:
        owner = media["owner"]
        return {
            "profile_pic_url": owner.get("profile_pic_url"),
            "username": owner.get("username"),
            "full_name": owner.get("full_name"),
        }

    def get_image(self, media: dict) -> dict:
        return {"image": {"display_url": media.get("display_url"), "resources": media.get("display_resources")}}

    def get_video(self, media: dict) -> dict:
        return {"video": {"display_url": media.get("display_url"), "video_url": media.get("video_url")}}

    def get_url(self, media: dict) -> Dict[Any, Any]:
        if media["is_video"]:
            return self.get_video(media)
        else:
            return self.get_image(media)

    def _get_urls(self, nodes: list) -> dict:
        videos = []
        images = []
        for node in nodes:
            if node["node"]["is_video"]:
                video = self.get_video(node["node"])
                videos.append(video)
            else:
                image = self.get_image(node["node"])
                images.append(image)
        return {"images": images, "videos": videos}

    def extract_media(self, media: dict) -> dict:
        nodes = media.get("edge_sidecar_to_children")
        if nodes:
            return self._get_urls(nodes.get("edges"))
        else:
            return self.get_url(media)
