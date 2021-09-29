from environs import Env


env = Env()
env.read_env()

class CeleryConfig:
	broker_url = env.str("BROKER_URL")
	backend_url = env.str("CELERY_RESULT_BACKEND")