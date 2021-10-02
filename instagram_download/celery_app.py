from celery import Celery

from instagram_download.settings import CeleryConfig

celery_app = Celery("tasks",
                    broker=CeleryConfig.broker_url,
                    include=["instagram_download.worker.jobs.tasks"],
                    backend=CeleryConfig.backend_url)
