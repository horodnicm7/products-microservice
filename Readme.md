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
#### 2.1 comment out:
```
depends_on:
      postgres_database:
        condition: service_healthy
```

from the *docker-compose.yaml* file. This is used to run only the database container,
 and setup it with all the required permissions. Then run:
```
# change directory to root project. This will also build the docker images
docker-compose up
```

#### 2.2 uncomment the above piece of config from *docker-compose.yaml* and run:
```
docker-compose up
```
Now you should be able to run the project with volumes and the server will be 
restarted each time you make a code change.
