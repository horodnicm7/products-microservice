python3 -m venv products-venv
source products-venv/bin/activate

pip install -r requirements-development.txt
pip install "uvicorn[standard]"  # it will install the uvicorn server


# to connect to the postgres container
docker exec -it products-microservice_postgres_database_1 /bin/bash

# to remove all images related to the project
docker rmi -f $(docker image ls | grep "products-microservice" | awk '{print $3}'); docker rmi -f $(docker image ls | grep "products-database" | awk '{print $3}'); docker rm -f $(docker container ls --all | grep "products-microservice_products_microservice_1" | awk '{print $1}'); docker rm -f $(docker container ls --all | grep "products-microservice_postgres_database_1" | awk '{print $1}')
