### Chapter7 – Clean commit history and branches with `git rebase`

**WARNING**: one should avoid using `git rebase` on commits than have already been pushed in order to keep the remote commit history coherent, especially when working with several people on the same repository.

- Reference: [Modifiez vos branches avec Rebase](https://openclassrooms.com/fr/courses/5641721-utilisez-git-et-github-pour-vos-projets-de-developpement/6113081-modifiez-vos-branches-avec-rebase)

#### `git merge` vs `git rebase`

- `git merge` creates a new commit that integrates the code from branch A into branch B

- `git rebase` combines two branches in a different way than `git merge`. `git rebase` takes all commits from branch A and moves them to branch B. `git rebase` makes the commit history cleaner, thus easier to follow

| Merge | Rebase|
|:---:|:---:|
| ![](../../images/merge/merge1.png) | ![](../../images//rebase/rebase1.png) |
| ![](../../images//merge/merge2.png) | ![](../../images//rebase/rebase2.png) |
| ![](..//images/merge/merge3.png) | ![](..//images/rebase/rebase3.png) |

- Image reference: [Modifiez vos branches avec Rebase](https://openclassrooms.com/fr/courses/5641721-utilisez-git-et-github-pour-vos-projets-de-developpement/6113081-modifiez-vos-branches-avec-rebase)

##### Git merge example

- Create scenario

```
git status # make sure you are on master branch and that branch is clean
git checkout -b my_new_branch
touch temp1.txt
git add temp1.txt
git commit -m "Adding temp1.txt"
```

- Merge my_new_branch on master branch

```
git checkout main
git merge my_new_branch # if conflict, resolve conflict by hand with gedit for example
```

##### Git rebase example

- Create scenario

```
git status # make sure you are on master branch and that branch is clean
git checkout -b my_new_branch
touch temp1.txt
git add temp1.txt
git commit -m "Adding temp1.txt"
```

- Rebase my_new_branch on master

```
git checkout main
git rebase my_new_branch
```

### Interactive rebase

- `git rebase -i 1f07f54d` (interactive rebase) allows us to alter the commit history 
    
Why would we want to alter the commmit history?
- Suppose you commited a little too early and you want to delete that commit
- Suppose you commited every 5 minutes and realize that the commit history is now illegible and you want to combine several commits into a single commit

One can use an interactive rebase to delete commits, change the order of commits and update commits in order to obtain a cleaner commit history.

| Interactive rebase (reorder example) | Interactive rebase (squash example) |
|:---:|:---:|
| ![](../../images/interactive_rebase/interactive_rebase1.png) | ![](../../images/interactive_rebase/interactive_rebase1.png) |
| ![](../../images/interactive_rebase/interactive_rebase_reorder1.png) | ![](../../images/interactive_rebase/interactive_rebase_squash1.png) |
| ![](../../images/interactive_rebase/interactive_rebase_reorder2.png) | ![](../../images/interactive_rebase/interactive_rebase_squash2.png) |

#### Interactive rebase options

```
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup <commit> = like "squash", but discard this commit's log message
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
# .       create a merge commit using the original merge commit's
# .       message (or the oneline, if no original merge commit was
# .       specified). Use -c <commit> to reword the commit message.
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out
```

**WARNING**: as said above, with interative rebase, lines "[...] are executed from top to bottom" thus updating the history in that order.

#### Git interactive rebase examples

##### Example1: Invert commits

- Create scenario

```
git status # make sure you are on master branch and that branch is clean
touch temp1.txt
git add temp1.txt
git commit -m "Adding temp1.txt"
touch temp2.txt
git add temp2.txt
git commit -m "Adding temp2.txt"
```

- Invert commits "Adding temp1.txt" and "Adding temp2.txt" with interactive rebase

```
git log # copy first 8 characters of commit id preceding commits you want to update
git rebase -i 1f07f54d # WARNING: replace 1f07f54d with first 8 characters of commit id stored in clipboard
# or do
# git rebase -i HEAD~2 # alter last 2 commits
```

A text editor will a appear

**WARNING**: commits appear in inverted order compared to `git log`

In the text editor, invert lines

> pick b61ed64 Adding temp1.txt  
pick 73e09c7 Adding temp2.txt

Now you have,

> pick 73e09c7 Adding temp2.txt  
pick b61ed64 Adding temp1.txt

```
# save content of text editor
```

```
# close text editor
```

```
git log
```

As you can see, commits `Adding temp1.txt` and `Adding temp2.txt` have been inverted.

##### Example2: Delete second to last commit

- Create scenario

```
git status # make sure you are on master branch and that branch is clean
touch temp1.txt
git add temp1.txt
git commit -m "Adding temp1.txt"
touch temp2.txt
git add temp2.txt
git commit -m "Adding temp2.txt"
```

- Delete second to last commit (i.e. "Adding temp1.txt") with interactive rebase

```
git rebase -i HEAD~2 # alter last 2 commits
```

A text editor will a appear

**WARNING**: commits appear in inverted order compared to `git log`

In the text editor, you have

> pick e7154bd Adding temp1.txt  
pick 18cfc02 Adding temp2.txt

On the first line replace `pick` with `drop`. Now you have,

> drop e7154bd Adding temp1.txt  
pick 18cfc02 Adding temp2.txt

```
# save content of text editor
```

```
# close text editor
```

```
git log
```

As you can see, commit `Adding temp1.txt` have been deleted.

##### Example3: Update commit message of last commit

- Create scenario

```
git status # make sure you are on master branch and that branch is clean
touch temp1.txt
git add temp1.txt
git commit -m "Adding temp1.txt"
```

- Update message of last commit

```
git rebase -i HEAD^ # HEAD^ is equivalent to HEAD^1 to alter last commit
```

A text editor will a appear

**WARNING**: commits appear in inverted order compared to `git log`

In the text editor, you have

> pick e7154bd Adding temp1.txt

Replace `pick` with `edit`. Now you have,

> edit e7154bd Adding temp1.txt

```
# save content of text editor
```

```
# close text editor
```

```
git commit --amend
```

A text editor will a appear

In the text editor, you have

> Adding temp1.txt

Replace "Adding temp1.txt" with "Adding file temp1.txt". Now you have,

> Adding file temp1.txt

```
# save content of text editor
```

```
# close text editor
```

```
git rebase --continue
```

```
git log
```

As you can see, the commit message of the last commit is now `Adding file temp1.txt` instead of `Adding temp1.txt`

##### Example4: Combine several commits into a single commit (squash commits)

- Create scenario

```
git status # make sure you are on master branch and that branch is clean
touch temp1.txt
git add temp1.txt
git commit -m "Adding temp1.txt"
touch temp2.txt
git add temp2.txt
git commit -m "Adding temp2.txt"
```

```
git rebase -i HEAD~2 # alter last 2 commits
```

A text editor will a appear

**WARNING**: commits appear in inverted order compared to `git log`

In the text editor, you have

> pick e7154bd Adding temp1.txt  
pick 18cfc02 Adding temp2.txt

On the second line replace `pick` with `squash`. Now you have,

> pick e7154bd Adding temp1.txt  
squash 18cfc02 Adding temp2.txt

```
# save content of text editor
```

```
# close text editor
```

A text editor will a appear

Replace the following lines

> Adding temp1.txt  
\#  
\# This is validation message number 2 :  
\#  
Adding temp2.txt

with your new commit message or leave them as is.

```
# save content of text editor
```

```
# close text editor
```

```
git log
```

As you can see, commits `Adding temp1.txt` and `Adding temp2.txt` have been combined into a single commit.