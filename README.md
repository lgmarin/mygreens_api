# mygreens_API
A REST API to provide vegetables growing information

## _Vegetables growing info API using Flask_

![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=blue)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
![](https://img.shields.io/badge/Framework-Flask-informational?style=flat&logo=flask&logoColor=white&color=blue)
![](https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=white&color=blue)
![](https://img.shields.io/badge/DB-MySQL-informational?style=flat&logo=mysql&logoColor=white&color=blue)

## Running the APP

### Build and Run the Docker Container

Build 

```sh
docker build -t mygreens-api ./app
```

Run

```sh
docker run -d -p 5000:5000 mygreens-api
```
 
### Dev environment with hot reload
```sh
docker-compose up --build
```