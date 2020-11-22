## Continuous Integration (CI)

### Chapter3 – Configure a CI pipeline with Gitlab CI

- Reference: [Intégrez votre code en continu](https://openclassrooms.com/fr/courses/2035736-mettez-en-place-lintegration-et-la-livraison-continues-avec-la-demarche-devops/6182908-integrez-votre-code-en-continu)

```
# create an empty GitLab repository named `spring-petclinic-microservices`
```

```
git clone https://gitlab.com/DamienToomey/spring-petclinic-microservices.git
cd spring-petclinic-microservices
git remote add upstream https://github.com/spring-petclinic/spring-petclinic-microservices.git # Spring Boot example code to test our pipeline
git pull upstream master
git push origin master
```

#### Activate CI/CD for your project on GitLab

- On the GitLab web interface, go to project `spring-petclinic-microservices` > Click on `Set up CI/CD`

#### Create `.gitlab-ci.yml` with automated build and tests

- In the GitLab web interface, create `.gitlab-ci.yml`. It will contain a description of the CI/CD pipeline.

- Append the following code to `.gitlab-ci.yml`:

```
# ===== Indicate to GitLab in which order to run each job =====
stages:
  - build
  - test
# ===== =====

# ===== Add cache to reduce app compilation time =====
cache:
  paths:
    - .m2/repository
  key: "$CI_JOB_NAME"

# In the case of Java compilation with Maven (our case), this compilation
# downloads a lot of external librairies which are stored in the folder .m2

# With the keyword cache and the predefined GitLab variable $CI_JOB_NAME, 
# the .m2 folder is shared across all jobs in the pipeline.
# ===== =====

# Compilation
build_job: # new job
  stage: build # job build_job with build as stage
  script: # write script you want to run
    # download Maven (compilation tool), app dependencies and run project compilation
    - ./mvnw compile
      -Dhttps.protocols=TLSv1.2
      -Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository
      -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=WARN
      -Dorg.slf4j.simpleLogger.showDateTime=true
      -Djava.awt.headless=true
      --batch-mode --errors --fail-at-end --show-version -DinstallAtEnd=true -DdeployAtEnd=true
  image: openjdk:8-alpine

# Test
test_job:
  stage: test
  script:
    - ./mvnw test
      -Dhttps.protocols=TLSv1.2
      -Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository
      -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=WARN
      -Dorg.slf4j.simpleLogger.showDateTime=true
      -Djava.awt.headless=true
      --batch-mode --errors --fail-at-end --show-version -DinstallAtEnd=true -DdeployAtEnd=true
  image: openjdk:8-alpine
```

- Commit changes
- Go to  `spring-petclinic-microservices > CI/CD > Pipelines`
- You can see that your pipeline in currently running
- Wait until it is done running (`passed`)

The code will systematically go through the pipeline at every push.

The pipeline stops in there is a error.

#### Add code quality to `.gitlab-ci.yml`

- Reference: [Garantissez la qualité de votre code](https://openclassrooms.com/fr/courses/2035736-mettez-en-place-lintegration-et-la-livraison-continues-avec-la-demarche-devops/6182962-garantissez-la-qualite-de-votre-code)

####

- Add `- quality` after `- test` in `stages`
- Append the following code to `.gitlab-ci.yml`:

```
# Quality
code_quality_job:
  stage: quality
  image: docker:stable # docker image stable that analyses code
  allow_failure: true
  # allow_failure: true: indicate that pipeline will continue even if the quality stage fails
  services: # add service to start docker image
    - docker:stable-dind
  script: # script to run inside container
    - mkdir codequality-results # create folder codequality-results/ that will contain the analysis
    - docker run
        --env CODECLIMATE_CODE="$PWD"
        --volume "$PWD":/code
        --volume /var/run/docker.sock:/var/run/docker.sock
        --volume /tmp/cc:/tmp/cc
        codeclimate/codeclimate analyze -f html > ./codequality-results/index.html
  # --volume "$PWD":/code: transfer code to folder /code located in container
  # script is executed inside image docker:stable
  # ===== Store result of quality analysis on GitLab =====
  artifacts:
    paths:
      - codequality-results/ # the result will be accesssible in the job code_quality_job
  # ===== =====
```

- Go to `spring-petclinic-microservices > CI/CD > Pipelines > code_quality_job > Browse > codequality-results > index.html`
- You can see code quality

#### Add step to `.gitlab-ci.yml` in order to package app in Docker images and save them in GitLab registry

- Add `- package` after `- quality` in `stages`

- Append the following code to `.gitlab-ci.yml`:

```
# Package
package_job:
  stage: package
  services:
    - docker:stable-dind
  variables:
    DOCKER_HOST: tcp://docker:2375
  script:
    - apk add --no-cache docker # install Docker client inside image openjdk:8-alpine
    - docker login -u gitlab-ci-token -p $CI_JOB_TOKEN $CI_REGISTRY # connec to GitLab registry to get the right to save generated images
    # $CI_JOB_TOKEN (password to connect) and $CI_REGISTRY (address to registry) are GitLab variables
    - ./mvnw install -PbuildDocker -DskipTests=true -DpushImage
      -Dhttps.protocols=TLSv1.2
      -Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository
      -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=WARN
      -Dorg.slf4j.simpleLogger.showDateTime=true
      -Djava.awt.headless=true
      --batch-mode --errors --fail-at-end --show-version -DinstallAtEnd=true -DdeployAtEnd=true
    # Maven compiles project, creates Docker image (`-PbuildDocker`) and stores image in the GitLab registry (`-DpushImage`)
  image: openjdk:8-alpine
```

**WARNING**: `package_job` above will not work because you must indicate to Maven where the Docker registry is located. This information must be inserted in `pom.xml` located at the root of the project by replacing:

`<imageName>${docker.image.prefix}/${project.artifactId}</imageName>`
with
`<imageName>${env.CI_REGISTRY_IMAGE}/${docker.image.prefix}/${project.artifactId}</imageName>`

The variable `CI_REGISTRY_IMAGE` is a GitLab variable which gives the address of the registry.

- Launch pipeline (either with a push from your local repository or with a commit on the GitLab web interface)

- Go to `spring-petclinic-microservices > Container Registry` to check if images have been pushed on the Docker Registry

GitLab comes with a Docker registry which allows you to store Docker images within GitLab.