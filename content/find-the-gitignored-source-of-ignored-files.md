Title: Find the gitignored source of ignored files
Date: 2022-08-04 07:36:36
Modified: 2022-08-04 07:36:36
Category: Tech
Tags: #tech, #git, #gitignore
Slug: find-the-gitignored-source-of-ignored-files
Author: filipgorczynski
Status: published
Cover: https://blog.filipgorczynski.me/images/feature/road-ahead-ibVdcAkGaaM.jpg
meta_url: https://blog.filipgorczynski.me/2022/08/find-the-gitignored-source-of-ignored-files
Summary: 

![Photo by Road Ahead](https://blog.filipgorczynski.me/images/feature/road-ahead-ibVdcAkGaaM.jpg)

Thanks to [Arthur's response](https://stackoverflow.com/a/49190672/273283) I've found the source

```bash
find . -type d | grep -v .git | awk '{print $1"/"}' | git check-ignore -v --stdin
```

<small class="unsplash-reference">
    Photo by <a href="https://unsplash.com/@roadahead_2223?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Road Ahead</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</small>
  