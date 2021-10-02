from instagram_download.celery_app import celery_app
from multiprocessing import Process

def run():
    w = celery_app.Worker(
        loglevel="INFO",
        concurrency=2
    )
    w.start()

def main():
    w = Process(target=run)
    w.start()


if __name__ == "__main__":
    main()