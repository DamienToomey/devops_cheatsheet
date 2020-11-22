### Chapter7 – Create a docker-compose.yml file and ochestrate containers

- Reference: [Créez un fichier docker-compose pour orchestrer vos conteneurs](https://openclassrooms.com/fr/courses/2035766-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker/6211677-creez-un-fichier-docker-compose-pour-orchestrer-vos-conteneurs)

#### Create docker-compose.yml (at project root)

```
cd devops_cheatsheet
touch docker-compose.yml
gedit docker-compose.yml
```

Copy/paste the following code:

```
version: '3' # docker-compose version
services:
  db: # db is the name of the service that we choose to the give to the MySQL server
    image: mysql:5.7 # choose docker image we want to use # 5.7 is the mysql version
    volumes: # indicates where to save data from the mysql server (stateful)
      #- db_data:/var/lib/mysql # db_data is a volume created by Docker which writes the data from /var/lib/mysql at an unspecified location of the host disk
      - /data/mysql:/var/lib/mysql # path to data on host machine:path to data in container
      # WARNING: if /data/mysql already exists on host disk, the content of the folder will be copied into /var/lib/mysql of the container
      # WARNING: if the content of /data/mysql on the host disk or the content of /var/lib/mysql in the container is modified, the modification will also be applied on the other /data/mysql or /var/lib/mysql
    restart: always # define policy in case of failure # the container will restart when there is a problem
    environment: # environment variables
      MYSQL_ROOT_PASSWORD: somewordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress

  wordpress: 
    depends_on: # the wordpress container must start after MySQL
      - db
    image: wordpress:latest # Choose docker image we want to use
    ports:
      - "8000:80" # link port of host machine and container to display website in browser
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress

# Uncomment when using db_data instead of /data/mysql
# volumes:
#   db_data: {}

# Why {} after db_data: ?
# "In yaml a map can be represented with a JSON-like form: 
# {fee: fie, foe: foo}. So {} is simply an empty map - i.e. there are no volumes mounted."
# https://stackoverflow.com/questions/62066663/what-does-means-in-services-section-of-docker-compose-yml
```

```
# save docker-compose.yml
```

```
# close docker-compose.yml
```

##### Build images in docker-compose.yml

(Unecessary here as we are only pulling images from Docker Hub in the docker-compose.yml above)

```
sudo docker-compose build
```

##### Start a Docker Compose stack

```
sudo docker-compose up -d
```

Go to app: http://localhost:8000 (wait a couple of seconds (up to 30 seconds) and referesh several times if necessary) or do `sudo docker-compose logs -f` and wait until server is ready.

`/data/mysql` has been created on the local machine

We could also have used the `build` argument instead of `image` by specifying the path to our Dockerfile. When running `sudo docker-compose up -d`, it would have built the container through the Dockerfile before running it.

Docker containers are not made to run stateful services and a database (e.g. MySQL) is by definition a stateful service. However, you can use the `volumes` argument which allows you to store the entire content of the `/var/lib/mysql` folder on the host disk at `/data/mysql`.