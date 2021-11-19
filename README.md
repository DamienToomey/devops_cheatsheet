# devops_cheatsheet

The name of this repository is `devops_cheatsheet`.

It has the following tree structure:

```
.
├── .gitignore   <-- make git ignore certain files
├── images       <-- contains images used in the cheatsheet 
├── parts        <-- contains the different parts and chapters of the cheatsheet in markdown
├── README.md    <-- file you are reading    
└── temp.txt     <-- empty text file used in the examples
```

Every example assumes a clean initial repository in both local and remote repositories, i.e.
- no staged files
- no commits
- empty `temp.txt` file

### Parts

#### Part1 – Github

- [Chapter1](parts/part1/chapter1.md) – Overview
- [Chapter2](parts/part1/chapter2.md) – SSH keys
- [Chapter3](parts/part1/chapter3.md) – Git graph
- [Chapter4](parts/part1/chapter4.md) – Correct errors on local repository
- [Chapter5](parts/part1/chapter5.md) – `git log`, `git reflog`, `git blame`, `git cherry-pick`
- [Chapter6](parts/part1/chapter6.md) – `git reset` vs `git revert`
- [Chapter7](parts/part1/chapter7.md) – Clean commit history and branches with `git rebase`
- [Chapter8](parts/part1/chapter8.md) – Integrate other people's repositories into yours with `git submodule` and `git subtree`
- [Chapter9](parts/part1/chapter9.md) – Detect a bug with `git bisect`
- [Chapter10](parts/part1/chapter10.md) – Git workflow 
- [Chapter11](parts/part1/chapter11.md) – Continuous integration (CI) vs Continuous Delivery vs Continuous Deployment
- [Chapter11](parts/part1/chapter12.md) – Multiple GitHub Accounts - SSH vs HTTPS

##### Reference

This part is heavily based on the following OpenClassrooms course:
- [Utilisez Git et GitHub pour vos projets de développement](https://openclassrooms.com/fr/courses)

#### Part 2 – Docker / Docker Compose

- [Chapter1](parts/part2/chapter1.md) – Docker overview
- [Chapter2](parts/part2/chapter2.md) – Install Docker
- [Chapter3](parts/part2/chapter3.md) – Start your first container
- [Chapter4](parts/part2/chapter4.md) – Create your first Dockerfile and Docker image
- [Chapter5](parts/part2/chapter5.md) – Push and pull images on Docker Hub
- [Chapter6](parts/part2/chapter6.md) – Docker Compose
- [Chapter7](parts/part2/chapter7.md) – Start a Docker Compose stack
- [Chapter8](parts/part2/chapter8.md) – Start another Docker Compose stack

##### Reference

This part is heavily based on the following OpenClassrooms course:
- [Optimisez votre déploiement en créant des conteneurs avec Docker](https://openclassrooms.com/fr/courses/2035766-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker)

#### Part 3 – Gitlab CI/CD

- [Chapter1](parts/part3/chapter1.md) – Introduction to DevOps
- [Chapter2](parts/part3/chapter2.md) – What is Continuous Integration (CI) and Continuous Delivery (CD)?
- [Chapter3](parts/part3/chapter3.md) – Configure a CI pipeline with Gitlab CI
- [Chapter4](parts/part3/chapter4.md) – Codify your infrastructure
- [Chapter5](parts/part3/chapter5.md) – Deploy Docker images in [Play with Docker](https://labs.play-with-docker.com)
- [Chapter6](parts/part3/chapter6.md) – Monitor your app on the staging environment with Prometheus
- [Chapter7](parts/part3/chapter7.md) – Get live updates of your app during development and in production

##### Reference

This part is heavily based on the following OpenClassrooms courses:
- [Découvrez la méthodologie DevOps](https://openclassrooms.com/fr/courses/6093671-decouvrez-la-methodologie-devops)
- [Mettez en place l'intégration et la livraison continues avec la démarche DevOps](https://openclassrooms.com/fr/courses/2035736-mettez-en-place-lintegration-et-la-livraison-continues-avec-la-demarche-devops)