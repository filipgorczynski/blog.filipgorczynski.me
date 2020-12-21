Title: Własne asercje w Robot Framework
Date: 2019-12-04 08:43
Author: filipgorczynski
Category: Tech
Slug: wlasne-asercje-w-robot-framework
Status: draft

![Robot Framework](https://filipgorczynski.files.wordpress.com/2019/05/robot-framework-logo.png?w=128){.alignleft .size-thumbnail .wp-image-2234 width="128" height="128"}

https://gist.github.com/filipgorczynski/7f8808d302118d8fac66408f40618884

https://gist.github.com/filipgorczynski/364a1d2efa2e8ae1cd4eb0e978657414

tests/e2e/Assertions.py

from collections import Counter

def unsorted\_arrays\_should\_be\_equal(array1, array2):  
if Counter(array1) != Counter(array2):  
raise Exception("Both arrays differs")
