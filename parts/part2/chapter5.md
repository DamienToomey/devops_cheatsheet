### Chapter5 – Push and pull images on Docker Hub

- Reference: [Utilisez des images grâce au partage sur le Docker Hub](https://openclassrooms.com/fr/courses/2035766-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker/6211567-utilisez-des-images-grace-au-partage-sur-le-docker-hub)

#### Push your image on DockerHub.

- Sign up / Sign in to [DockerHub](https://hub.docker.com)
- Create a repository
- Name the repository my_first_docker_image
- Click Create
- Create link between image you have created and image you want to push on Docker Hub

```
sudo docker tag my_first_docker_image:latest damientoomey/my_first_docker_image:my_tag
# damientoomey is my username
# :latest to use lastest version of the image, which is also the default
# or
# sudo docker tag ID_OF_IMAGE damientoomey/my_first_docker_image:my_tag
```

```
sudo docker login
# enter Docker Hub credentials
sudo docker push damientoomey/my_first_docker_image:my_tag
```

#### Pull my image from Docker Hub and run it

```
sudo docker run damientoomey/my_first_docker_image:my_tag
```

#### Explore [Docket Hub](https://hub.docker.com/search?q=&type=image)

There are two types of images:
- store images
- official images

Docker CLI (command-line interface)

##### Search for Nginx image on Docker Hub

- With command line
    - `sudo docker search nginx`

- With web interface:
    - https://hub.docker.com/search?q=nginx&type=image