### Chapter8 – Build small python app and create CI pipeline with GitLab CI

The Python code to be processed in pipeline is located in folder `python_app`.

#### Use GitLab only for CI purposes

Code is on GitHub.

CI pipeline will be run on GitLab.

- Go to https://gitlab.com
- Sign in / Sign up
- Click on `New project`
- Click on `Run CI/CD for external repository`
- Click on `Repo by URL`
- Paste `https://github.com/DamienToomey/devops_cheatsheet.git` into textbox
- Enter `Username (optional)`
- Enter `Password (optional)`
- Enter `Project name`: `devops_cheatsheet`
- Under `Visibility level`, choose `Public` radio button

#### Create `.gitlab-ci.yml`

Update GitHub mirror on GitLab: `devops_cheatsheet > Settings > Repository > Mirroring repositories > Expand > At the bottom of this section, click on the symbol for Update`