A set of git hooks

## post-checkout
Keeps track of checked out branches (except master and develop) and saves them to a file

### Requirements
- Python3

### To use
  - Place git_reminder in your $PATH
  - link post-checkout to the `.git/hooks` directory of your repo
  - To see last a list of your checked out branches, run `git_reminder <your repo name>`
