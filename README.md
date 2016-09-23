A set of git hooks

## post-checkout
Keeps track of checked out branches (except master and develop) and saves them to a file

To use:
  1. link post-checkout to your `.git/hooks` directory
  1. link git_reminder somewhere in your `$PATH$`
  1. to remind yourself of checkout out branches, call `git_reminder <your repo name>` 
