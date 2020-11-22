### Chapter4 – Codify your infrastructure

- Reference: [Codifiez votre infrastructure](https://openclassrooms.com/fr/courses/2035736-mettez-en-place-lintegration-et-la-livraison-continues-avec-la-demarche-devops/6183070-codifiez-votre-infrastructure)

####

We will use Docker for Infrastructure as code.

In order not to overwrite current Docker images present in the Gitlab registry, you need to tag images with a new tag version by replacing the tag `<version>2.3.2</version>` with `<version>2.3.3</version>` in **every** `pom.xml` file in the project.

- Go to `spring-petclinic-microservices` > Container Registry` to check tag version in the registry

#### Deploy app with Docker Compose

##### Update registry address for every image in `docker-compose.yml`

`Docker Compose` ochestrastes Docker images.

`Kubernetes` is another image orchestrator that we do not use here.

- Go to `spring-petclinic-microservices > Container Registry` to find registry address

i.e. replace `springcommunity/spring-petclinic-admin-server` with `registry.gitlab.com/damientoomey/spring-petclinic-microservices/springcommunit/spring-petclinic-admin-server`

##### Update image versions in `docker-compose.yml`

e.g., replace

`registry.gitlab.com/damientoomey/spring-petclinic-microservices/springcommunit/spring-petclinic-admin-server`
with
`registry.gitlab.com/damientoomey/spring-petclinic-microservices/springcommunit/spring-petclinic-admin-server:2.0.7`