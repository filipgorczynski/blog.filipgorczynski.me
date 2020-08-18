Title: Generator pseudolosowych literek
Date: 2010-09-22 12:19
Author: filipgorczynski
Category: Programowanie
Slug: generator-pseudolosowych-literek
Status: published

Nie wiem, do czego komu by się to mogło przydać, ale może ktoś potrzebuje generator spamu?  
\[code language="php"\]  
\<?php  
\$a = array('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z');  
while(1) {  
\$b = \$a\[array\_rand(\$a, 1)\];  
echo \$b;  
}  
\[/code\]
