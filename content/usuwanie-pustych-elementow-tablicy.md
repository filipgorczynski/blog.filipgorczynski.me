Title: Usuwanie pustych elementów tablicy
Date: 2010-12-08 14:44
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Slug: usuwanie-pustych-elementow-tablicy
Status: published

Szybki sposób na usunięcie elementów będących fałszem znajdujących się w tablicy:  
\[code language="php"\]  
\<?php  
\$arr = array('jeden', '2', 'trzy', 4, 'pięć', '', 6, 0);  
print\_r(array\_filter(\$arr));  
\[/code\]
