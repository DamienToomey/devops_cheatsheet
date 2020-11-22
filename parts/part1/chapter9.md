### Chapter9 – Detect a bug with `git bisect`

Move from one commit to another withing a range of commits in order to find where a bug first appeared in the repository.

To do this with `git bisect`, you have to give an initial commit id that does not present the bug and a final commit id that contains the bug. `git bisect` now knows the range of commits to go through.

```
git log
git bisect start <id of commit with the bug> <id of commit without the bug>
```

`git bisect` will now move to every commit within the range and you can test the code for each commit.

If the code for a commit does not present the bug, enter:

```
git bisect good
```

If the code for a commit presents the bug, enter:

```
git bisect bad
```

`git bisect` will stop when `git bisect bad` is entered for the first time.