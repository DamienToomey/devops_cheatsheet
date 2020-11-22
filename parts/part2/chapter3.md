### Chapter3 – Start your first container

- Reference: [Lancez votre premier conteneur en local](https://openclassrooms.com/fr/courses/2035766-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker/6211458-lancez-votre-premier-conteneur-en-local)

#### Run a docker image (see output in terminal)

```
sudo docker run hello-world
```

#### Run another docker image (see output in browser)

```
sudo docker run -d -p 8080:80 alexwhen/docker-2048
# docker run --help
# -d --detach: Run container in background and print container ID
# -p, --publish list: Publish a container's port(s) to the host
# 8080:80 transfer network traffic from port 8080 to the port 80 of the container. You can then access the app from the container on  http://127.0.0.1:8080
# alexwhen/docker-2048: name of docker image we want to use and which is downloaded from Docker Hub
```

#### List containers that are running

```
sudo docker ps
```

#### Stop container

```
sudo docker stop a0dbb5196b10
# a0dbb5196b10 is the id of the container found doing `sudo docker ps`
# or use ID_RETURNED_BY_DOCKER_RUN
```

#### Delete container after stopping it

```
sudo docker container rm ID_RETURNED_BY_DOCKER_RUN
```

#### Delete image

```
sudo docker image rm ID_RETURNED_BY_DOCKER_RUN
```

#### Delete stopped containers and unused images

```
sudo docker system prune --all
# WARNING! This will remove:
#   - all stopped containers
#   - all networks not used by at least one container
#   - all images without at least one container associated to them
#   - all build cache
```

#### Modify / Execute commands inside a Docker container

```
sudo docker exec -it ID_RETURNED_BY_DOCKER_RUN bash
# docker exec --help
# exec: Run a command in a running container
# -i, --interactive: Keep STDIN open even if not attached
# -t, --tty: Allocate a pseudo-TTY
```

```
cd /usr/share/nginx/html
cat index.html
# type exit or ctrl+d to exit container
```

#### Retrieve Docker image on Docker Hub without running the container

```
docker pull hello-world
```

#### List local docker images

```
sudo docker images -a
```

#### List local containers

```
sudo docker container ls -a
```

#### Remove all stopped containers

```
sudo docker container prune
```

#### Remove all images

```
sudo docker images prune --all
```