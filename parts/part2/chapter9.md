### Chapter9 – Inspect Docker Images and Docker Containers

#### Build Dockerfile to obtain docker image

```bash
$ docker build -f cypress/Dockerfile -t my_docker_image .
```


#### Inspect content of docker image (not container)

```bash
$ docker image ls
# copy image id
$ docker run -it IMAGE_ID sh
```

#### Inspect content of container

```bash
$ docker run -dt my_docker_image
$ docker ps
# copy container id
$ docker exec -it CONTAINER_ID bash
```
