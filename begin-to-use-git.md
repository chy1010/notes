# Begin to use git

## new start

- create repository
```bash
> mkdir notes
> cd notes
> git init
Initialized empty Git repository in ~/notes/.git/
```

- may change default branch by `git config --global init.defaultBranch <name>`
- rename the just-created branch: `git branch -m <name>`

- set user name & email in local scale
    * `git config --local user.name chy1010`
    * `git config --local user.email andy1010@gmail.com`

- see the local config
    * `git config --local --list`
    ```text
    core.repositoryformatversion=0
    core.filemode=true
    core.bare=false
    core.logallrefupdates=true
    user.name=chy1010
    user.email=andy1010@gmail.com
    (END)
    ```

- see the status
    * `git status`

- add files into Git
    * `git add begin-to-use-git.md`
    * If this file is updated after being added into git, 
      then it should be added again to keep this modification.

- commit to the git repository
    * `git commit -m 'init commit'`
        + `-m`: commit with short comments
        + `--allow-empty`: if no comments.

## Create the github repository

- create remote repository on `github`.
- add remote:
    * `git remote add origin git@git-chy1010:chy1010/notes.git`
    * `git push origin main`
        + push master branch to origin
    * `git push -u origin main`
        + `-u`: set upstream that we push to

## Remove / Rename / Untrack file

- delete and add to git
    * `rm (filename)`
    * `git add (filename)`

- git remove
    * `git rm (filename)`

- only untrack file
    * `git rm (filename) --cached`

- rename file
    * `git mv (filename) (new filename)`

- rename file (remove and new-add file)
    * `mv (filename) (new filename)`
    * `git add --all`