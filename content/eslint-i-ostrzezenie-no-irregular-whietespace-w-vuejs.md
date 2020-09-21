Title: ESLint i ostrzeżenie no-irregular-whietespace w VueJS
Date: 2019-04-26 09:37
Author: filipgorczynski
Category: Tech
Slug: eslint-i-ostrzezenie-no-irregular-whietespace-w-vuejs
Status: draft

Aby ograniczyć regułę ESling w ramach pliku, w znaczniku template dodajemy

```html
<template>
<!-- eslint-disable no-irregular-whitespace -->
```
i przed zakończeniem

```html
<!-- eslint-enable no-irregular-whitespace -->
```
