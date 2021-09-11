Title: Global .gitignore
Date: 2021-09-09 09:52
Modified: 2021-09-09 09:52
Category: Tech
Tags: #git, #gitignore
Slug: global-gitignore
Author: filipgorczynski
Status: draft
Summary: From time to time I see editors or IDEs settings pushed to GitHub repositiories. Sometimes they're put there intentionally - and that's fine. But more often they're not. So how can we preven't ourselves from putting all IDEs and editors into every projects .gitignore?

From time to time I see editors or IDEs settings pushed to GitHub repositiories. Sometimes they're put there intentionally - and that's fine. But more often they're not. So how can we preven't ourselves from putting all IDEs and editors into every projects .gitignore?

There are certain files created by particular editors, IDEs, operating systems, etc., that do not belong in a repository. But adding system-specific files to the repo's .gitignore is considered a poor practice. This file should only exclude files and directories that are a part of the package that should not be versioned (such as the node_modules directory) as well as files that are generated (and regenerated) as artifacts of a build process.

All other files should be in your own global gitignore file:

Create a file called .gitignore in your home directory and add any filepath patterns you want to ignore.
Tell git where your global gitignore file is.
Note: The specific name and path you choose aren't important as long as you configure git to find it, as shown below. You could substitute .config/git/ignore for .gitignore in your home directory, if you prefer.

The solution is actually pretty easy:

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

If you want to exclude files on a per-repo basis without modifying .gitignore, you can directly edit .git/info/exclude in the repo. Nothing under the local .git directory is committed.

I find myself often creating "scratch" code that I don't want to commit. I do this enough that I found it useful to add scratch/ to my global ignore. I've personally never worked on a project where this is an issue because a directory called scratch should not be a ignored, but if this is a concern, try using __scratch__ or something similar.

You might find useful ignore patterns for your projects here on GitHub: https://github.com/github/gitignore

Now, it doesn't matter if I work with VS Code or JetBrains IDEs, they're configurations will be exluded from project repository.

- [Configuring ignored files for a single repository](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files#configuring-ignored-files-for-all-repositories-on-your-computer)
