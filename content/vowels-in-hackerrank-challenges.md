Title: Vowels in HackerRank challenges
Date: 2022-08-31 13:55:42
Modified: 2022-08-31 13:55:42
Category: Tech
Tags: #hackerrank, #sql, #vowels, #english, #mysql, #regexp_like
Slug: vowels-in-hackerrank-challenges
Author: filipgorczynski
Status: published
Cover: https://blog.filipgorczynski.me/images/feature/uriel-sc-11KDtiUWRq4.jpg
meta_url: https://blog.filipgorczynski.me/2022/08/vowels-in-hackerrank-challenges
Summary: HackerRank is one of many good places to train our software craft. However challenges are not always clear enough.

![Photo by Uriel SC](https://blog.filipgorczynski.me/images/feature/uriel-sc-11KDtiUWRq4.jpg)

HackerRank is one of many good places to train our software craft. However challenges are not always clear enough.

While solving one of the challenges today I've learned that letter `y` is not a vowel in English language. Differently to Polish. Thus, the regular expression that includes English vowels should be:

```regex
/[aeiou]/
```

Furthermore I've learned, that MySQL has a great [regexp_like](https://dev.mysql.com/doc/refman/8.0/en/pattern-matching.html) function for matching patterns by regular expressions.

<small class="unsplash-reference">
    Photo by <a href="https://unsplash.com/@urielsc26?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Uriel SC</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</small>
