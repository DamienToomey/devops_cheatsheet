## Part 2 – Docker / Docker Compose

### Chapter1 – Docker overview

- Reference: [Découvrez ce qu'est Docker](https://openclassrooms.com/fr/courses/2035766-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker/6211349-decouvrez-ce-quest-docker)

#### Overview

Docker is one tool, among others, that allows you to do containerization.

You should run only one process per container, e.g. in a LAMP stack (Linux, Apache, MySQL, PHP), you would create 3 containers: one for Apache, one for MySQL and one for PHP.

A Docker container is originally stateless but can be stateful if necessary. (stateful: e.g. MySQL database, stateless: e.g. HTTP)

A Docker container is immutable. In order to modify the configuration of a container, one must create a new image and re-deploy it.

#### Versions

- Docker Community Edition (Linux only) (**free**) (also called docker-ce)
- Docker Desktop (Mac or Windows) (**free**)
- Docker Enterprise (Linux seulement)