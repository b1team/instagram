# Instagram Downloader

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Python Version: python3.6**

## Installation
  
Clone this project and run following commands

```bash
cd instagram
make virtualenv
source .venv/bin/activate
make deploy
```

## Executing

Just run:

```bash
$ instagram_download
```

or

```bash
$ python -m instagram_download
```


## Deploying using docker-compose

```bash
docker-compose up -d --build
```