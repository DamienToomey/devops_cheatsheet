### Chapter4 – Create your first Dockerfile and Docker image

- Reference: [Créez votre premier Dockerfile](https://openclassrooms.com/fr/courses/2035766-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker/6211517-creez-votre-premier-dockerfile)

#### Common commands

- `FROM` defines the base image to be used to create our image. `FROM` can be used only once in a Dockerfile. We can now personalize this image in our dockerfile
- `RUN` executes commands in the container. **WARNING**: this instruction should not be used to many times in the Dockerfile in order to limit the number of layers created in the image and thus the disk space of the final image
- `ADD` copies content from local machine (e.g. source code) to the Docker image.
- `WORKDIR` "sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile." ([WORKDIR docs](https://docs.docker.com/engine/reference/builder/#workdir)). This command is equivalent to `cd` in bash.
- `EXPOSE` (optional) indicates on which port the app is listening to
- `VOLUME` (optional) "Without the VOLUME command the write speed to the specified folder will be very slow" ([stackoverflow](https://stackoverflow.com/questions/41935435/understanding-volume-instruction-in-dockerfile))
- `CMD` corresponds to the command that the container should run as the container starts

#### Build your own Docker image

Let's understand the Dockerfile and .dockerignore files in the github repository [ghost-cms](https://github.com/OpenClassrooms-Student-Center/ghost-cms)

```
git clone https://github.com/OpenClassrooms-Student-Center/ghost-cms.git
```

In this example, we will install Node.js and other dependencies in the image.

##### Dockerfile

Each command (`FROM`, `RUN`, ...) in the Dockerfile is called a **layer**. There should be few layers in the Dockerfile so that the image runs fast and takes up little disk space.

```
cd ghost-cms
cat Dockerfile
```

Output:

```
FROM debian:9

RUN apt-get update -yq \
   && apt-get install curl gnupg -yq \
   && curl -sL https://deb.nodesource.com/setup_10.x | bash \
   && apt-get install nodejs -yq \
   && apt-get clean -y

ADD . /app/
WORKDIR /app
RUN npm install

EXPOSE 2368
VOLUME /app/logs

CMD npm run start
```

##### .dockerignore

.dockerignore acts as a .gitignore and prevents some files to be copied into the image when doing `ADD`.

```
cd ghost-cms
cat .dockerignore
```

Output:

```
node_modules
.git
```

##### Information

Docker creates a container for every instruction in the Dockerfile, which corresponds to a layer. The final result, the Docker image, corresponds to a set of layers.

Advantages: when bulding an image from a Dockerfile, only the layers located after a rebuilt layer will also be rebuilt. Re-building an image after a modification can thus be fast.

##### Build the image from the Dockerfile

```
sudo docker build -t ocr-docker-build .
# -t, --tag list: Name and optionally a tag in the 'name:tag' format
# Here we chose to name the image ocr-docker-build
# . corresponds to the path to the Dockerfile
```

##### Launch container

```
sudo docker run -d -p 2368:2368 ocr-docker-build
```

Go to app: http://127.0.0.1:2368

### Build another Docker image

Reference: https://riptutorial.com/fr/docker/example/10772/helloworld-dockerfile#exemple

#### Create Dockerfile (at project root)

```
cd git_cheatsheet
touch Dockerfile
gedit Dockerfile
```

Copy/paste the following code:

```
FROM ubuntu
RUN mkdir /myvol
RUN echo "This is my Hello world example!" > /myvol/greeting
CMD cat /myvol/greeting
```

```
# save Dockerfile
```

```
# close Dockerfile
```

##### Create image

```
sudo docker system prune --all
sudo docker build -t my_first_docker_image .
```

##### Run image

```
sudo docker run my_first_docker_image
```

Output:

```
This is my Hello world example!
```