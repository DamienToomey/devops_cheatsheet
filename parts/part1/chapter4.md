### Chapter4 – Correct errors on local repository

- Reference: [Corrigez vos erreurs sur votre dépôt local](https://openclassrooms.com/fr/courses/5641721-utilisez-git-et-github-pour-vos-projets-de-developpement/6112481-corrigez-vos-erreurs-sur-votre-depot-local)

#### Undo modification done on master branch and move modification to branch `my_new_branch` BEFORE commit being done on this modification

- Create scenario

```
git status # make sure you are on master branch and that branch is clean
echo hello >> temp.txt
```

- Solution

```
git stash
git status # nothing to commit, working directory clean
git checkout -b my_new_branch
git status # you are on branch my_new_branch
git stash list
git stash apply stash@{0} # WARNING: replace stash@{0} with the correct stash given in stash list
git status
```

#### Undo modification done on master branch and move modification to branch `my_new_branch` AFTER commit being done on this modification BEFORE push

- Create scenario

```
git status # make sure you are on master branch and that branch is clean
echo hello >> temp.txt
git commit -m "Append hello to temp.txt"
```

- Solution

```
git log # copy first 8 characters of commit id to remove
git reset --hard HEAD^
git checkout -b my_new_branch
git reset --hard ca83a6df # WARNING: replace ca83a6df with first 8 characters of commit id stored in clipboard 
```

#### Update erroneous commit message

- Create scenario

```
git status # make sure you are on master branch and that branch is clean
echo hello >> temp.txt
git add temp.txt
git commit -m "This is a stupid commit message"
git log
```

- Solution

```
git commit --amend -m "New commit message"
git log
```

#### Add file forgotten to be added before committing

- Create scenario

```
git status # make sure you are on master branch and that branch is clean
touch temp1.txt
touch temp2.txt
git add temp1.txt
git commit -m "Adding temp1.txt and temp2.txt"
```

- Solution

```
git add temp2.txt
git commit --amend --no-edit
```

#### Remove file from commit

- Create scenario

```
git status # make sure you are on master branch and that branch is clean
touch temp1.txt
touch temp2.txt
git add temp1.txt
git add temp2.txt
git commit -m "Adding temp1.txt"
```

- Remove file temp2.txt from commit

```
git reset --soft HEAD~1
```

- Unstage file temp2.txt

```
git reset HEAD temp2.txt
```

```
git status
```

```
git commit -m "Adding temp1.txt"
```