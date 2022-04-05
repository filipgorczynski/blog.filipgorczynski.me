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

However after some time of using it I've met a problem, when entering directory with `.git` repository. It freezes and allowed for `Ctrl+C` only - and displaying "raw" part of the prompt.

After some digging into the problem the problem I've found was not exactly in the `.oh-my-zsh` itself but in the `spaceship` theme I've used. My bad :). So the solution was pretty simple - just go to the theme directory and pull the latest changes or simply reinstall it.

<small class="unsplash-reference">
    Photo by <a href="https://unsplash.com/@jakewalker?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jake Walker</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</small>
