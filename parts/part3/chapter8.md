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

#### WARNING: Block merge in GitLab if job fails in pipeline

- Reference: [Have a look at How to block the merge of Merge Requests when SonarQube Quality Gate is failed, with GitLab](https://community.sonarsource.com/t/how-to-block-the-merge-of-merge-requests-when-sonarqube-quality-gate-is-failed-with-gitlab/19530)

####

- Go to `devops_cheasheet_ci > Settings > General`
- Scoll down to `Merge Settings`
- Click on `Expand`
- Select radio button `Pipelines must succeed`

#### Summary

In order to create the CI pipeline, we had to modify information in:
- the GitLab web interface (create project and add SonarCloud variables)
- create `gitlab-ci.yml`
- create `sonar-project.properties`

#### References

- [Create SonarCloud project](https://sonarcloud.io/documentation/integrations/gitlab)
- [Set up CI/CD pipeline for SonarCloud](https://sonarcloud.io/project/configuration?analysisMode=GitLabPipeline&id=DamienToomey_devops_cheatsheet_ci)