from instagram_download.worker.worker import celery_app
from instagram_download.worker.jobs.instagram import InstagramScaper

instagram = InstagramScaper()

@celery_app.task
def insta_media_wrapper(url):
	media = instagram.get_media(url)
	return media

@celery_app.task
def instagram_url_wrapper(media):
	result = instagram.extract_media(media)
	return result