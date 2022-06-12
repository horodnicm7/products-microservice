## How to build the application through docker
### 1. Build the microservice image
```
docker build -t products-microservice -f docker/Dockerfile .
```
### 2. Build the database image
```
docker build -t products-database -f docker/Dockerfile-db .
```

## How to run the application
### 1. On local machine
```
uvicorn app.main:app --reload
```
### 2. Through docker
```
# change directory to root project. This will also build the docker images
docker-compose up
```