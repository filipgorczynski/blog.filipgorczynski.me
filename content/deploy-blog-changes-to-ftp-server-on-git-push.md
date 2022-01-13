Title: Deploy blog changes to FTP server on git push
Date: 2022-01-13 08:08:59
Modified: 2022-01-13 08:08:59
Category: Tech
Tags: #tech, #git, #github-actions, #automation, #blog
Slug: deploy-blog-changes-to-ftp-server-on-git-push
Author: filipgorczynski
Status: published
meta_og_title: Deploy blog changes to FTP server on git push
meta_og_description: This blog moved to Pelican Static Site Generator some time ago. One of the problems was automation of updates on FTP server when things are added or changed.
meta_og_url: https://blog.filipgorczynski.me/2022/01/deploy-blog-changes-to-ftp-server-on-git-push
meta_og_image: https://blog.filipgorczynski.me/images/post/2022/01/photo-1556075798-4825dfaaf498.jpg
Summary: This blog moved to Pelican Static Site Generator some time ago. One of the problems was automation of updates on FTP server when things are added or changed.

![Photo by Yancy Min](https://blog.filipgorczynski.me/images/post/2022/01/photo-1556075798-4825dfaaf498.jpg)

This blog moved to Pelican Static Site Generator some time ago. One of the problems was automation of updates on FTP server when things are added or changed.

I decided to create some Docker image with Pelican pre-installed. That way I could call all pelican tasks on GNU Linux and Windows systems.
I've lost some time and failed (I haven't tried hard enough). But then another idea arrived. GitHub Actions was one of them. What I see right now - it works pretty well. When I push `master` branch to GitHub it builds everything and transfer files to FTP.

Create a file `.github/workflows/main.yml` with following content:

[gist:id=ea68fa7f919da8b8c00a111d8ce17e11]

Go to GitHub repository settings to `Secrets` section. Create few new Action secrets with appropriate values: ftp_host, ftp_password, ftp_username, localdir.

For `localdir` I've used `./output` value as a source directory to copy files from.

Those secrets are available in the `main.yml` under `${{ secrets.ftp_username }}` keys.

<small class="unsplash-reference">
    Photo by <a href="https://unsplash.com/@yancymin?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Yancy Min</a> on <a href="https://unsplash.com/s/photos/github-actions?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</small>
