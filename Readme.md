## How to build the application through docker
```
docker build -t products-microservice -f docker/Dockerfile .
```

## How to run the application
### 1. On local machine
```
uvicorn app.controller:app --reload
```
### 2. Through docker
```
# change directory to root project
docker-compose up
```