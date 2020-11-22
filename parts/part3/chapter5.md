### Chapter5 – Deploy Docker images in [Play with Docker](https://labs.play-with-docker.com)

- Reference: [Déployez et testez votre code sur différents environnements](https://openclassrooms.com/fr/courses/2035736-mettez-en-place-lintegration-et-la-livraison-continues-avec-la-demarche-devops/6183137-deployez-et-testez-votre-code-sur-differents-environnements)

You need an environment to deploy the app.

[Play with Docker](https://labs.play-with-docker.com) is a website that allows you to deploy Docker containers easily.

- Go to https://labs.play-with-docker.com
- Sign in (with Docker Hub credentials)
- Click on the spanner
- Choose template `3 Managers and 2 Workers` (creates a cluster Docker Swarm to deploy images)
- A template is created by the website
- You will find an SSH command of the form

```
ssh ip172-18-0-88-busioknp2ffg00ff9m20@direct.labs.play-with-docker.com
```

- Copy address before the @, i.e. `ip172-18-0-88-busioknp2ffg00ff9m20`

- Go to `.gitlab-ci.yml` and edit file

- Add `- deploy` after `- package` in `stages`

- Under

```
cache:
  paths:
    - .m2/repository
  key: "$CI_JOB_NAME"
```

copy/paste:

```
variables:
  PLAYWD: ip172-18-0-88-busioknp2ffg00ff9m20
```

- Append the following code to `.gitlab-ci.yml`:

```
# Deploy staging
deploy_staging_job:
  stage: deploy
  image: docker:stable
  script:
    # ===== Install Docker Compose to deploy app on Play with Docker =====
    - apk add --no-cache openssh-client py-pip python3-dev libffi-dev openssl-dev gcc libc-dev make # use python3-dev instead of python-dev for python2 that is no longer supported
    - pip install docker-compose
    # ===== =====
    - export DOCKER_HOST=tcp://$PLAYWD.direct.labs.play-with-docker.com:2375 # indicates where Docker daemon is located and where to deploy app
    # ===== Deploy app described in docker-compose.yml =====
    - docker-compose down
    - docker-compose up -d
    # ===== =====
  # ===== Add environment in GitLab to see result =====
  environment:
    name: staging
    url: http://$PLAYWD-8080.direct.labs.play-with-docker.com
  # ===== =====
```

- Go to `spring-petclinic-microservices > Operations > Environments > Open live environment` to check if environment is deployed:

- Wait and refresh until page appears (wait up to 30 seconds or more)

#### Run tests on staging environment (production-like environment)

Test perfomance on app that is deployed in Play with Docker (see previous section)

- **Acceptance testing**: determine if backlog requirements are met
- **Performance testing**: test stability and availibity of app (e.g. response time when executing a large number of queries)
- **Smoke test**: test basic features of app
- **Manual tests**

####

- Go to `.gitlab-ci.yml` and edit file
- Add `- performance` after `- deploy` in `stages`
- Append the following code in `.gitlab-ci.yml`

```
# Performance
performance_job:
  stage: performance
  image: docker:git
  variables:
    URL: http://$PLAYWD-8080.direct.labs.play-with-docker.com/ # add new variable to indicate on which environment, performance tests should be run
  services:
    - docker:stable-dind
  script:
    - apk add --no-cache curl
    - x=1; while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' http://$PLAYWD-8080.direct.labs.play-with-docker.com/)" != "200" || $x -le 60 ]]; do sleep 5; echo $(( x++ )); done || false # loop to wait until app is running
    - mkdir gitlab-exporter
    - wget -O ./gitlab-exporter/index.js https://gitlab.com/gitlab-org/gl-performance/raw/master/index.js # download performance binary
    - mkdir sitespeed-results
    - docker run --shm-size=1g --rm -v "$(pwd)":/sitespeed.io sitespeedio/sitespeed.io:14.1.0 --plugins.add ./gitlab-exporter --outputFolder sitespeed-results $URL # execute binary with Docker
    - mv sitespeed-results/data/performance.json performance.json # store result
  artifacts:
    paths:
      - sitespeed-results/ # export result folder to GitLab
    reports:
      performance: performance.json
```

- Go to `spring-petclinic-microservices > CI/CD > Pipelines > code_quality_performance > Browse > sitespeed-results > index.html` to see sitespeed results

**WARNING**: I had to replace `sitespeedio/sitespeed.io:6.3.1` with `sitespeedio/sitespeed.io:14.1.0` where `sitespeedio/sitespeed.io:14.1.0` is a Docker image and `6.3.1` is the version of that image. Without this version update, the job would fail

- sitespeed version issue:
  - [GitLab sitespeed example](https://repository.prace-ri.eu/git/help/user/project/merge_requests/browser_performance_testing.md)
  - [Browser-Performance.gitlab-ci.yml](https://gitlab.com/gitlab-org/gitlab/blob/master/lib/gitlab/ci/templates/Verify/Browser-Performance.gitlab-ci.yml)
  - [sitespeed version problem](https://gitlab.com/gitlab-org/gitlab/-/issues/251083)

#### Deploy to a production environment

We still use Play with Docker to deploy the app.

We use the already present `- deploy` in `stages`.

- Append the following code to `.gitlab-ci.yml`:

```
# Deploy production
deploy_prod_job:
  stage: deploy
  image: docker:stable
  script:
    - apk add --no-cache openssh-client py-pip python3-dev libffi-dev openssl-dev gcc libc-dev make # use python3-dev instead of python-dev for python2 that is no longer supported
    - pip install docker-compose
    - export DOCKER_HOST=tcp://$PLAYWD.direct.labs.play-with-docker.com:2375
    - docker-compose down
    - docker-compose up -d
  environment:
    name: prod
    url: http://$PLAYWD-8080.direct.labs.play-with-docker.com
  when: manual # production deployment requires a human intervention
```

#### Canary Release

Let only a part of the users be redirected to the new production version (Canary Release) and leave the rest of the users on current production version (Production environment). Then, if something goes wrong on the new version, only a small part of the users will be impacted.

- Go to `.gitlab-ci.yml` and edit file

- Add `- canary` before `- deploy` in `stages`

- Append the following code to `.gitlab-ci.yml`:

```
# Canary Release
canary_job:
  stage: canary
  image: docker:stable
  script:
    - apk add --no-cache openssh-client py-pip python3-dev libffi-dev openssl-dev gcc libc-dev make # use python3-dev instead of python-dev for python2 that is no longer supported
    - pip install docker-compose
    - export DOCKER_HOST=tcp://$PLAYWD.direct.labs.play-with-docker.com:2375
    - docker-compose down
    - docker-compose up -d
  environment:
    name: prod
    url: http://$PLAYWD-8080.direct.labs.play-with-docker.com
  when: manual
  only:
    - master # run job only when the pipeline is run on master branch
```

**PROBLEM**: how are users redirected to the Canary Release or the production environment??? (To be understood)

#### Final `stages` section in `.gitlab-ci.yml`

```
stages:
  - build
  - test
  - quality
  - package
  - canary
  - deploy
  - performance
```

