Title: Szybki swap dwóch zmiennych
Date: 2010-07-21 19:24
Author: filipgorczynski
Category: Programowanie
Slug: szybki-swap-dwoch-zmiennych
Status: published

Czasami spotykam się ze specjalnie pisaną funkcją swap zamieniająca wartości dwóch zmiennych między sobą.  
\[code language="php"\]  
function swap(&\$a, &\$b) {  
\$tmp = \$a;  
\$a = \$b;  
\$b = \$tmp;  
}  
\[/code\]  
Można to zrealizować troszkę szybciej (w sensie kodu):  
\[code language="php"\]  
list(\$b, \$a) = array(\$a, \$b);  
\[/code\]

Niestety nie sprawdzałem jeszcze jak bardzo różnią się te 2 sposoby pod względem wydajnościowym.
