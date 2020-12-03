### Chapter6 – Monitor your app on the staging environment with Prometheus

- Reference: [Monitorez votre application](https://openclassrooms.com/fr/courses/2035736-mettez-en-place-lintegration-et-la-livraison-continues-avec-la-demarche-devops/6183162-monitorez-votre-application)

In order for GitLab to display metrics for the deployment, you have to indicate to GitLab where to retrieve these metrics.

- Go to `spring-petclinic-microservices > Settings > Integrations > Scroll down and click on Prometheus (Times-series monitoring service) > Check checkbox Active`

- In text box `API URL` > Paste Prometheus URL of your app (retrieve this URL by going to Playing with Docker with your app already deployed on Playing with Docker and click on 9091 and copy url), e.g. 

```
http://ip172-18-0-17-busf6h7p2ffg00ff9ed0-9091.direct.labs.play-with-docker.com
# WARNING: without /graph at the end of the url
```

- Click on `Save changes`

- Click on `Test settings`. You should get Connection successful.

- Cick on `Add new metric`

- Scroll down on Prometheus GitLab page > New metric:
- Name: `Requests per second`
- Choose radio button `Response`
- Query: `http_server_requests_seconds_count` # query is the request that GitLab will send to Prometheus
- Y-axis label: `Requests per second`
- Unit label: `req/seq`
- Click on `Create metric`
- Go to `spring-petclinic-microservices > Operations > Metrics > Response metrics (Custom)` to observe results

If you get `Connection failed`, reload page. I suspect that the connection between GitLab and the Prometheus container running in Play with Docker sometime fails.

- Go to `spring-petclinic-microservices > Operations > Environment > Monitoring > Response metrics (Custom)` to see metrics of a particular environment

You have put in place the supervision of your app in the staging with a metric thanks to Prometheus and GitLab.

If you are satisfied with the metrics given by Prometheus, you can now push your version into production.

#### Team productivity

- Go to `spring-petclinic-microservices > Analytics > Value Stream` to see metrics on new issues, commits, deploys, time bewteen opening of an issue and closing this issue, ...