### Chapter8 – Start another Docker Compose stack

Let's use a custom Dockerfile inside docker-compose.yml (i.e. use `build` instead of `image`) for the service named ghost.

```
cd devops_cheatsheet
git clone https://github.com/OpenClassrooms-Student-Center/ghost-cms
cd ghost-cms # already contains a Dockerfile and .dockerignore
touch docker-compose.yml
gedit docker-compose.yml
```

Copy/paste the following code:

```
version: '3'
services:
  db:
    image: mysql:5.7
    volumes:
      - /data/mysql:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: monPassword # chosen arbitrarily
      MYSQL_DATABASE: ghost # found in ghost-cms/config.production.json
      MYSQL_USER: ghostuser # found in ghost-cms/config.production.json
      MYSQL_PASSWORD: ocrpassword # found in ghost-cms/config.production.json

  ghost: 
    depends_on:
      - db
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:2368"
    restart: always
    environment:
    environment:
      database__client: mysql
      database__connection__host: db
      database__connection__user: ghostuser
      database__connection__password: ocrpassword
      database__connection__database: ghost
      NODE_ENV: production # given in the [OpenClassrooms course](https://openclassrooms.com/fr/courses/2035766-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker/6770816-entrainez-vous-en-orchestrant-vos-images-docker-avec-docker-compose#/id/r-6770853)
```

```
# save docker-compose.yml
```

```
# close docker-compose.yml
```

##### Build images in docker-compose.yml

```
sudo docker-compose stop
sudo docker-compose down
sudo docker volume prune # might be necessary according to [Docker-compose, MySQL, ghost](https://openclassrooms.com/forum/sujet/docker-compose-mysql-ghost)
sudo docker system prune --all
sudo docker-compose build
```

##### Start a Docker Compose stack

```
sudo docker-compose up -d
```

Go to app: http://localhost:8000 (wait a couple of seconds (up to 30 seconds) and referesh several times if necessary) or do `sudo docker-compose logs -f` and wait until server is ready.

`/data/mysql` has been created on the local machine

#### Enter container and check if MySQL is working

- Reference: [Docker-compose, MySQL, ghost](https://openclassrooms.com/forum/sujet/docker-compose-mysql-ghost)

```
sudo docker ps # get id of mysql container
sudo docker exec -it ID_OF_CONTAINER bash
mysql --user ghostuser --password ghost
# Enter password: ocrpassword
# Enter SQL commands
```

If the above does not work:

```
mysql --user root --password ghost # log in as root user
# Enter password: monPassword
# Change user
system mysql -u ghostuser -p
# Enter password: ocrpassword
# Enter SQL commands
```

#### Check if `/var/lib/mysql` folder in container is updated when `/data/mysql` folder on host is updated and vice versa

- Terminal 1

```
sudo docker ps
sudo docker exec -it ID_OF_MySQL_CONTAINER bash
ls /var/lib/mysql
```

- Terminal 2

```
ls /data/mysql
touch /data/mysql/hello1.txt # dummy file
ls /data/mysql
```

- Terminal 1

```
sudo docker ps
sudo docker exec -it ID_OF_MySQL_CONTAINER bash
ls /var/lib/mysql
```

As you can see, `/var/lib/mysql` in the container now contains the file `hello1.txt` that was created in `/data/mysql` on the host.

- Terminal 1

```
sudo docker ps
sudo docker exec -it ID_OF_MySQL_CONTAINER bash
touch /var/lib/mysql/hello2.txt
```

- Terminal 2

```
ls /data/mysql
```

As you can see, `/data/mysql` on the host now contains the file `hello2.txt` that was created in `/var/lib/mysql` in the container.