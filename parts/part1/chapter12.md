### Chapter12 – Multiple GitHub Accounts

- References:
    - [Create SSH Key](https://www.inmotionhosting.com/support/server/ssh/how-to-add-ssh-keys-to-your-github-account)
    - [Clone Repository Using SSH in Git](https://www.toolsqa.com/git/clone-repository-using-ssh)
    - [GitHub - Error: Permission denied (publickey)](https://docs.github.com/en/authentication/troubleshooting-ssh/error-permission-denied-publickey)
    - [using-multiple-github-accounts-with-ssh-keys.md](https://gist.github.com/oanhnn/80a89405ab9023894df7)


Let's consider that you have two github accounts:
- professional account, i.e. GitHub account for work
- personal account, i.e. GitHub account for your personal projects

#### Via `SSH` (strongly recommended)

#### Account 1: create a private and public SSH key on your PC

```bash
$ ssh-keygen -t rsa -b 4096 -C "username.account1@gmail.com"
# click enter
# click enter
# click enter
$ cat ~/.ssh/id_rsa.pub
```

#### Account 1: Add the public SSH key to GitHub

- copy the output of the previous command
- go to https://github.com/settings/ssh/new
- click on new SSH key
- Title: My PC
- paste the output of the cat command

##### Account 2: Create a second ssh key for a second GitHub Account

```bash
$ ssh-keygen -t rsa -b 4096 -C "username.account2@gmail.com"
# type ~/.ssh/id_rsa_account2
# click enter
# click enter
$ cat ~/.ssh/id_rsa_account2.pub
```

"Tip: On most systems the default private keys (~/.ssh/id_rsa and ~/.ssh/identity) are automatically added to the SSH authentication agent. You shouldn't need to run ssh-add path/to/key unless you override the file name when you generate a key." ([GitHub - Error: Permission denied (publickey)](https://docs.github.com/en/authentication/troubleshooting-ssh/error-permission-denied-publickey))

For this second SSH key, we have changed the default filename in order not overwrite the first SSH key we created.

```bash
$ ssh-add ~/.ssh/id_rsa_account2
# Output: Identity added: ...
```

#### Account 2: Add the public SSH key to GitHub

Do as previously.

##### How wll `git` know which GitHub account to use?

```bash
$ cd ~/.ssh
$ touch config
$ gedit config
```

- paste the following

```
# Default github account: UsernameAccount1 (username.account1@gmail.com)
Host github.com
   HostName github.com
   IdentityFile ~/.ssh/id_rsa
   IdentitiesOnly yes
   
# Other github account: UsernameAccount2 (username.account2@gmail.com)
Host github-account2
   HostName github.com
   IdentityFile ~/.ssh/id_rsa_account2
   IdentitiesOnly yes
```

##### Clone

- go to your project homepage on GtiHub
- click `Code`
- click `SSH`
- copy the URL 

Let's say that the URL you copied is `git@github.com:UsernameAccount1/my-project-name.git`

**Clone with account 1**

```bash
git clone git@github.com:UsernameAccount1/my-project-name.git
```

**Clone with account 2**

```bash
git clone git@github-account2:UsernameAccount2/my-project-name.git

Notice that `github-account2` replaces `github.com` in the url.

```

- `cd` inside your project

```bash
$ cd .git
$ gedit config
```

The `config` contains

```
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = git@github-account2:UsernameAccount2/my-project-name.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
```

In the snippet above, notice that the `url`contains the `github-account2` alias.

You now push and pull in your repository and `~/.ssh/config` will take care of providing the ssh key for the correct account.

#### Via `HTTPS`

<!--
How to clone this GitHub repository over HTTPS?

  - Create a Personal Access Token:
    - Follow the steps in the documentation: https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token
      - At step 8, select the repo checkbox
      - Click Generate token
      - Copy the token and store it safely because it is like a password

  - Open a terminal to clone the empty repository

```bash
$ git clone https://github.com/DamienToomey/my-project-name.git
```

- Enter username when prompted
- Enter Personal Access Token when prompted for password
-->

If you decide to clone your repository via `HTTPS`, `git` will ask you to enter your username and password ([Personal Access Token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)) each time you `clone`, `pull`, `push`. It is possible to cache your credentials but you might run into issues if you have two GitHub accounts on your computer (e.g. personal and professional accounts).

For example, in VS Code, if you have cached your credentials for one account, you will not be prompted for your credentials when you want to push some changes with your second account. To overcome this, in VS Code, do 

```bash
File > Preferences > Settings > Type `Git` > Scroll down and look for Git: Enabled > Uncheck the box
```

VS Code will now prompt for username and password.
