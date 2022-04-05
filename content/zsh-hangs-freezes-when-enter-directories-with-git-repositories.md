Title: zsh hangs/freezes when enter directories with git repositories
Date: 2022-04-05 08:12
Modified: 2022-04-05 08:12
Category: Tech
Tags: #tech, #zsh, #oh-my-zsh, #git, #spaceship, #theme
Slug: zsh-hangs-freezes-when-enter-directories-with-git-repositories
Author: filipgorczynski
Status: published
Cover: https://blog.filipgorczynski.me/images/feature/jake-walker-MPKQiDpMyqU.jpg
meta_url: https://blog.filipgorczynski.me/2022/03/zsh-hangs-freezes-when-enter-directories-with-git-repositories
Summary: There is no doubt oh-my-zsh project is awesome. It can drastically improve your software development workflow. It even informs you, when new version was released.

![Photo by Jake Walker](https://blog.filipgorczynski.me/images/feature/jake-walker-MPKQiDpMyqU.jpg)

There is no doubt oh-my-zsh project is awesome. It can drastically improve your software development workflow. It even informs you, when new version was released.

After some time of using it I've met a problem. When entering directory with `.git` repository it freezes and allowed for `Ctrl+C` only - and displaying "raw" part of the prompt.

While debugging I've found the issue was not exactly in the `.oh-my-zsh` itself but in the `spaceship` theme I've used - `spaceship`. My bad :). The solution was pretty simple. Go to the individual theme directory and pull the latest changes or reinstall it.

<small class="unsplash-reference">
    Photo by <a href="https://unsplash.com/@jakewalker?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jake Walker</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</small>
