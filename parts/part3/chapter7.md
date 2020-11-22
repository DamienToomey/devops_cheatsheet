### Chapter6 – Get live updates on app during development and in production

- Reference: [Monitorez votre application](https://openclassrooms.com/fr/courses/2035736-mettez-en-place-lintegration-et-la-livraison-continues-avec-la-demarche-devops/6183162-monitorez-votre-application)

You can get notifications on twitter, slack or email, ...

##### Set up notifications for slack:

- Go to `spring-petclinic-microservices > Settings > Integrations > Slack notifications`
- Check `Active` checkbox
- Click on `Add an incoming webhook`
- Click `Sign in to install`
- Sign in to your workplace
- Click on `Continue`
- Enter slack credentials
- Click on `Sign in`
- Cick on `Add Configuration`
- `Choose a channel... > #gitlab`
- Click on `Add Incoming Webhooks integration`
- Copy Webhook URL
- Go back to GitLab, scroll down and paste URL in field `Webhook`
- Click on `Test settings and save changes`

All updates in GitLab will now be sent to slack.

This feedback step with slack is the one that will allow us to make the link between developers (dev) and production (ops).