# Git Fetch vs Pull

- `git fetch` downloads commits, files and refs from a remote repository into your local repository, but it does **not** change your working files or current branch. After `fetch`, you must merge (or rebase) the remote branch into your local branch to incorporate the changes (for example `git merge origin/master`).

- `git pull` is essentially `git fetch` followed by `git merge` (by default). It downloads remote changes and immediately tries to merge them into the current branch, updating your working tree automatically.

When to use:
- Use `git fetch` when you want to inspect changes first or avoid automatically merging into your current branch.
- Use `git pull` for convenience when you want to bring your branch up to date in one step.

Potential pitfalls:
- `git pull` can create merge conflicts you did not inspect ahead of time.
- Using `git fetch` + `git merge` gives you the opportunity to review changes before merging.
