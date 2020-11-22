### Chapter5 – `git log`, `git reflog`, `git blame`, `git cherry-pick`

- Reference: [Corrigez un commit raté](https://openclassrooms.com/fr/courses/5641721-utilisez-git-et-github-pour-vos-projets-de-developpement/6113066-corrigez-un-commit-rate)

#### `$ git log`

Displays commit history.

- Output example:

```
commit b309b9085aa7229b2dea83234c49438b2475be74 (HEAD -> main, origin/main, origin/HEAD)
Author: DamienToomey <damien.toomey@insa-rouen.fr>
Date:   Thu Nov 12 14:58:03 2020 +0100

    Modifs

commit a958c0808d57dba2c287501461c18685ed8b95d4
Author: DamienToomey <damien.toomey@insa-rouen.fr>
Date:   Thu Nov 12 14:57:16 2020 +0100

    Modifs
```

#### `$ git reflog`

Displays commit history.

- Output example:

```
b309b90 (HEAD -> main, origin/main, origin/HEAD) HEAD@{0}: commit: Modifs
a958c08 HEAD@{1}: commit: Modifs
da236d2 HEAD@{2}: commit: Modifs
```

#### `$ git blame README.md`

Display commit history for each line of a specified file. The author of the modification is also displayed.

- Output example:

```
7a01111c (DamienToomey      2020-11-08 17:42:51 +0100  1) # git_cheatsheet
7a01111c (DamienToomey      2020-11-08 17:42:51 +0100  2) 
ce5a897b (DamienToomey      2020-11-08 17:46:52 +0100  3) The name of this repository is `git_cheatsheet`.
```

#### `$ git cherry-pick 7fc9e224`

`7fc9e224` being the id of a chosen commit.

Sometimes, instead of merging an entire branch into another, you only want to choose one or two commits from that branch: this is cherry-picking.

##### Git cherry-pick example

- Create scenario

```
git status # make sure you are on master branch and that branch is clean
git checkout -b my_new_branch
git status # make sure you are on my_new_branch
echo "Hello" >> temp.txt
git add temp.txt
git commit -m "Adding string Hello to temp.txt on my_new_branch"
git push --set-upstream origin my_new_branch
```

- Go back to master branch and cherry pick this specific commit

```
git status # make sure you are on my_new_branch
git log # copy first 8 characters of commit id to keep
git checkout main
git cherry-pick 7fc9e224 # WARNING: replace 7fc9e224 with first 8 characters of commit id stored in clipboard
git push
```