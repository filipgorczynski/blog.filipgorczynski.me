Title: Zmiana pierwszej litery na wielką z uwzględnieniem polskich znaków diakrytycznych
Date: 2014-10-18 21:13
Author: filipgorczynski
Category: Programowanie
Tags: ucfirst, utf8
Slug: zmiana-pierwszej-litery-na-wielka-z-uwzglednieniem-polskich-znakow-diakrytycznych
Status: published

[![PHP](http://filipgorczynski.files.wordpress.com/2014/09/php-logo-svg1-e1410978334544.png?w=150){.alignleft .wp-image-894 .size-thumbnail width="150" height="79"}](https://filipgorczynski.files.wordpress.com/2014/09/php-logo-svg1.png)Przykład prostej funkcji narzędziowej do zmiany pierwszej litery łańcucha znaków na wielką z uwzględnieniem polskich znaków diakrytycznych.

\[code language="php"\]  
function ucfirst\_utf8(\$str) {  
if (mb\_check\_encoding(\$str, 'UTF-8')) {  
\$first = mb\_substr(mb\_strtoupper(\$str, 'UTF-8'), 0, 1, 'UTF-8');  
return \$first . mb\_substr(mb\_strtolower(\$str, 'UTF-8'), 1, mb\_strlen(\$str), 'UTF-8');  
} else  
return \$str;  
}\[/code\]

Przykład użycia:

\[code language="php"\]  
var\_dump(ucfirst('żółty żółw'));  
var\_dump(ucfirst('zażółć gęślą jaźń'));  
var\_dump(ucfirst\_utf8('żółty żółw'));  
var\_dump(ucfirst\_utf8('zażółć gęślą jaźń'));  
\[/code\]

oraz wynik działania:

\[code language="text"\]  
string(16) "żółty żółw"  
string(26) "Zażółć gęślą jaźń"  
string(16) "Żółty żółw"  
string(26) "Zażółć gęślą jaźń"  
\[/code\]
