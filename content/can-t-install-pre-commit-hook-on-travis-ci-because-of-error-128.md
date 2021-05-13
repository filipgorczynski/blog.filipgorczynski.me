Title: Can't install pre-commit hook on Travis CI because of error 128
Date: 2021-05-07 15:33
Modified: 2021-05-07 15:33
Author: filipgorczynski
Category: Tech
Tags: #travis-ci, #pre-commit, #return-code-128, #pre-commit-config.yml
Slug: can-t-install-pre-commit-hook-on-travis-ci-because-of-error-128
Status: draft
Summary: Problem with

Problem was with redirection on gitlab repository when trying to fetch tags:

```bash
λ git fetch origin --tags
warning: redirecting to https://gitlab.com/pycqa/flake8.git/
```

So the change I've made was from this:
<script src="https://gist.github.com/filipgorczynski/5862085f4e67fbab331cff5d7b00caa8.js"></script>
to this:
<script src="https://gist.github.com/filipgorczynski/8f43e377b10def2556a7d4151042cace.js"></script>

