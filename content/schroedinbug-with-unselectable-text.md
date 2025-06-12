Title: Schrödinbug with unselectable text
Date: 2025-06-12 10:55:21
Modified: 2025-06-12 10:55:21
Category: Tech
Tags: #tech, #chakra-ui, #web, #bug
Slug: schroedinbug-with-unselectable-text
Author: filipgorczynski
Status: published
Cover: https://blog.filipgorczynski.me/images/feature/igor-omilaev-xvHl_X9Ojrg.jpg
meta_url: https://blog.filipgorczynski.me/2025/06/schroedinbug-with-unselectable-text
Summary: If text in a web component seems unselectable, your first instinct might be to check the CSS user-select property. So you pop open your browser's developer tools, inspect the elements...

![Photo by Igor Omilaev](https://blog.filipgorczynski.me/images/feature/igor-omilaev-xvHl_X9Ojrg.jpg)

If text in a web component seems unselectable, your first instinct might be to check the CSS user-select property. So you pop open your browser's developer tools, inspect the elements... and find that none of them are using `user-select: none`.

What gives?

In my case, the issue was much simpler: it wasn't a CSS property at all - it was a color illusion.

I was using Chakra UI's gray.200 (#e4e4e7) as the background, and the default text selection highlight color happened to match it almost exactly.
So when I tried selecting text, it was actually being highlighted - it just looked like nothing was happening.

No real bug here - just a case of indistinguishable colors. Crisis averted. Carry on.

<small class="unsplash-reference">
    Photo by <a href="https://unsplash.com/@omilaev?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Igor Omilaev</a> on <a href="https://unsplash.com/photos/a-close-up-of-a-text-bubble-with-the-word-wft-on-it-xvHl_X9Ojrg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
</small>
