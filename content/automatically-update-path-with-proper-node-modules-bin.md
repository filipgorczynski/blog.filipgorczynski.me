Title: Automatically update $PATH with proper node_modules/.bin
Date: 2021-10-25 14:36
Modified: 2021-10-25 14:36
Category: Tech
Tags: #npm, #bash, #path, #bin
Slug: automatically-update-path-with-proper-node-modules-bin
Author: filipgorczynski
Status: draft
Summary:

- https://coderwall.com/p/i5z1cg/automatically-update-path-with-proper-node_modules-bin

```bash
__OLD_PATH=$PATH
function updatePATHForNPM() {
  export PATH=$(npm bin):$__OLD_PATH
}

function node-mode() {
  PROMPT_COMMAND=updatePATHForNPM
}

function node-mode-off() {
  unset PROMPT_COMMAND
  PATH=$__OLD_PATH
}

# node-mode # Uncomment to enable node-mode by default
```
