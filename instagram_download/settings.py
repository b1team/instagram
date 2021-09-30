from environs import Env


env = Env()
env.read_env()

class CeleryConfig:
	broker_url = env.str("CELERY_BROKER_URL")
	backend_url = env.str("CELERY_RESULT_BACKEND")

class InstagramUserConfig:
	login_username = env.str("INSTAGRAM_LOGIN_USERNAME")
	login_password = env.str("INSTAGRAM_LOGIN_PASSWORD")