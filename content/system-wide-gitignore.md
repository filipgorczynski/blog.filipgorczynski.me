Title: Global .gitignore
Date: 2021-09-17 14:39
Modified: 2021-09-17 14:39
Category: Tech
Tags: #git, #gitignore
Slug: global-gitignore
Author: filipgorczynski
Status: published
Summary: From time to time I see code editors or IDEs settings pushed to GitHub repositiories. Sometimes they're put there intentionally - and that's fine. But more often they're not. So how can we preven't ourselves from putting all IDEs and editors into every projects `.gitignore`?

From time to time I see code editors or IDEs project settings pushed to GitHub repositiories. Sometimes they're put there intentionally - and that's fine. But more often they're not. So how can we preven't ourselves from putting all IDEs and editors into every projects `.gitignore`?

There are certain files created by particular code editors, IDEs, operating systems, etc., that do not belong in a repository. But adding system-specific files to the repo's `.gitignore` is considered a poor practice. This file should only exclude files and directories that are a part of the package that should not be versioned (such as the node_modules directory) as well as files that are generated (and regenerated) as artifacts of a build process.

All other files should be in your own global gitignore file.

The solution is actually pretty easy. Create a file called `.gitignore` in your home directory (also read note below) and add any filepath patterns you want to ignore. Next, tell git where your global gitignore file is.

**Note:** The specific name and path you choose aren't important as long as you configure git to find it. You could substitute `.config/git/ignore` for `.gitignore` file in your home directory, if you prefer.

```bash
echo ".vs_code" >> ~/.gitignore_global
git config --global core.excludesfile ~/.gitignore_global
```

Mine is:

```text
➜ cat ~/.gitignore_global 
# IDEs & Editors
.idea
.vscode
.project
outputs/
*.env
dump.rdb
*.code-workspace

.favorites.json
.pabotsuitenames
pip-wheel-metadata/*

venv/
```

Moreover, if you want to exclude files on a per-repo basis without modifying `.gitignore`, you can directly edit `.git/info/exclude` in the repo. Nothing under the local `.git` directory is committed.

Now, it doesn't matter if I work with VS Code or JetBrains IDEs, they're configurations will be exluded from project repository on a higher level.

For more details, jump to related documentation: [Configuring ignored files for a single repository](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files#configuring-ignored-files-for-all-repositories-on-your-computer)

Also, you might find useful [ignore patterns](https://github.com/github/gitignore) for your projects directly on GitHub.
