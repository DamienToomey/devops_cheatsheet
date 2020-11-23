### Chapter8 – Build a small Python app and create a CI pipeline with GitLab CI

#### Create project on GitLab

https://gitlab.com/DamienToomey/devops_cheatsheet_ci

The Python code to be processed in the CI pipeline is located in the folder named `python_app`.

Let's use SonarCloud to measure code quality.

#### SonarCloud

SonarQube = on premise option of SonarCloud.

- Go to https://sonarcloud.io
- Sign in with GitLab
- Click on `Import my personal GitLab group`
- Follow instructions

#### Summary

In order to create the CI pipeline, we had to modify information in:
- the GitLab web interface (create project and add SonarCloud variables)
- create `gitlab-ci.yml`
- create `sonar-project.properties`

#### References

- [Create SonarCloud project](https://sonarcloud.io/documentation/integrations/gitlab)
- [Set up CI/CD pipeline for SonarCloud](https://sonarcloud.io/project/configuration?analysisMode=GitLabPipeline&id=DamienToomey_devops_cheatsheet_ci)