from celery import Celery
from multiprocessing import Process

from instagram_download.settings import CeleryConfig

celery_app = Celery("tasks",
                    broker=CeleryConfig.broker_url,
                    include=["instagram_download.worker.jobs.tasks"],
                    backend=CeleryConfig.backend_url)


def worker():
    w = celery_app.Worker(
        loglevel="INFO",
        concurrency=2
    )
    w.start()


if __name__ == "__main__":
    w = Process(target=worker)
    w.start()