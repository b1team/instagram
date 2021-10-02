from instagram_download.celery_app import celery_app
from instagram_download.worker.jobs.instagram import InstagramScaper
from instagram_download.settings import InstagramUserConfig

instagram = InstagramScaper()
instagram.login(InstagramUserConfig.login_username, InstagramUserConfig.login_password)

@celery_app.task
def insta_media_wrapper(url):
	media = instagram.get_media(url)
	return media


@celery_app.task
def instagram_url_wrapper(media):
	result = instagram.extract_media(media)
	return result