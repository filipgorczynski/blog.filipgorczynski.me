Title: Deploy blog changes to FTP server on git push
Date: 2022-01-12 07:34:32
Modified: 2022-01-12 07:34:32
Category: Tech
Tags: #tech, #git, #github-actions, #automation, #blog
Slug: deploy-blog-changes-to-ftp-server-on-git-push
Author: filipgorczynski
Status: draft
meta_og_title: Deploy blog changes to FTP server on git push
meta_og_description: 
meta_og_url: https://blog.filipgorczynski.me/2022/01/deploy-blog-changes-to-ftp-server-on-git-push
<!-- meta_og_image: [https://](https://blog.filipgorczynski.me/images/post/2022/01/) -->
Summary: This blog was moved to Pelican Static Site Generator. One of the problems I've met was actually automation of updates on FTP server when things were added or changed.

This blog was moved to Pelican Static Site Generator. One of the problems I've met was actually automation of updates on FTP server when things were added or changed.

Firstly I decided to create some Docker container with Pelican installed in it that could be used to generate static content and perform all the Pelican tasks.
I've lost some time and failed (I haven't tried hard enough). But then another idea arrived. GitHub Actions was one of the available solutions and what I see right now - it works great. When I push `master` branch to GitHub it automatically build everything and transfer files to FTP.

Create a file `.github/workflows/main.yml` with following content:
[gist:id=ea68fa7f919da8b8c00a111d8ce17e11]

Go to GitHub repository settings to `Secrets` section. Then, create few new Action secrets with appropriate values:

- ftp_host
- ftp_password
- ftp_username
- localdir

For `localdir` I've used `./output` value as this one must be used as a source directory to copy from.

They're available in the `main.yml` under `${{ secrets.ftp_username }}` keys.
