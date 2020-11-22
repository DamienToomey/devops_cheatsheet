## Part 3 – Gitlab CI/CD

### Chapter1 – Introcution to DevOps

#### DevOps origins

- Reference: [Découvrez les origines de la méthodologie DevOps](https://openclassrooms.com/fr/courses/6093671-decouvrez-la-methodologie-devops/6183233-decouvrez-les-origines-de-la-methodologie-devops)

####

- DevOps approach bridges the gap between the development (dev) team and the operations (ops) team.
- DevOps approach reduces time to market: time between the decicion to create a feature and that feature being pushed into production

#### DevOps caracteristics

- Reference: [Identifiez les caractéristiques de la méthodologie DevOps](https://openclassrooms.com/fr/courses/6093671-decouvrez-la-methodologie-devops/6183322-identifiez-les-caracteristiques-de-la-methodologie-devops)

####

CALMS (Culture, Automatisation, Lean, Mesure et Share)

- **Culture**: solve communication and responsability issues between dev and ops teams. Both teams have to work together
- **Automation**: automate processes (tests, deployment, creation of environments)
- **Lean**: reduce time and money consumption when creating a piece of software. A Value Stream Map (VSM) identifies where time is being lossed in the pipeline and thus where a DevOps approach would be a gain to optimize processes. With a VSM, we can identify the delay between two processes and the duration of each process.
- **Mesure**: what is not measured cannot be improved. One must determine if adding a DevOps approach would be a gain or not. KPIs (Key Point Indicator) should be but in place to measure improvements or regressions.
- **Share**: developpers and ops teams should have a global view of what both teams do. Dev and Ops teams should do the Daily Scrum together.

#### Site Reliability Engineer (SRE)

- References:
    -  [Mettez en place le DevOps en évitant les pièges](https://openclassrooms.com/fr/courses/6093671-decouvrez-la-methodologie-devops/6183392-mettez-en-place-le-devops-en-evitant-les-pieges)
    - [Recrutez un SRE pour assurer le DevOps dans votre entreprise](https://openclassrooms.com/fr/courses/6093671-decouvrez-la-methodologie-devops/6183459-recrutez-un-sre-pour-assurer-le-devops-dans-votre-entreprise)

A Site Reliability Engineer (SRE) studies 4 metrics (Golden signals):
- **Latency**: time necessary to send a request and receive a response
- **Trafic**: number of resquests on the network
- **Errors**: problems in the infrastruture (e.g. network is down, database is down, ...) or code bug
- **Saturation**: network load (e.g. degradation of the service)

A SRE is also responsible for other indicators:
- **Service Level Objective (SLO)**: defines metrics and thresholds that should be reached by the service provider (e.g. service availibility, latency, ...). They are defined in agreement between the provider and the client
- **Service Level Agreement (SLA)**: contract between the provider and the client. Defines financial penalties the provider should pay to the client in the SLO is not reached.
- **Service Level Indicator (SLI)**: current metrics of the service running. If SLI < SLO, penalties might have to be paid to the client with repsect to the SLA