### Chapter2 – What is Continuous Integration (CI) and Continuous Delivery (CD)?

####  What is Continuous Integration (CI)?

- Reference: [Qu'est-ce que l'intégration continue ?](https://openclassrooms.com/fr/courses/2035736-mettez-en-place-lintegration-et-la-livraison-continues-avec-la-demarche-devops/6182691-quest-ce-que-lintegration-continue)

Integrate, Test and Compile the code.

- make sure not to add bugs during integration of the code
- be able to iterate quickly on the code that is already present while keeping high standards
- Steps:
    - plan development (based on the backlog, share features among developpers)
    - development
    - compile
    - test (unit tests and integration tests)
    - measure quality of code
    - store versioned code and manage artefacts (generated binaries of the app)

####  What is Continuous Delivery (CD)?

- Reference: [Qu'est-ce que la livraison continue ?](https://openclassrooms.com/fr/courses/2035736-mettez-en-place-lintegration-et-la-livraison-continues-avec-la-demarche-devops/6183043-quest-ce-que-la-livraison-continue)

Test app in a staging environment, i.e. a production-like environment.

Continuous Delevery (CD) allows to deploy an app on different environments in an automated manner.

Steps:
- Infrastructure as code (automate creation of infrastructure and environment)
- Deploy app (demo for client or for testing)
- Test (test app functionnalites that could not be tested without a production-like environment)
- Supervision (supervise app behaviour and check for bugs that appear only in a production-like environment (staging environment))
- Fast feedback (live feedback (notifications) about app in production)


