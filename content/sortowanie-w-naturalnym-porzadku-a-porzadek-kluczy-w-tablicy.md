Title: Sortowanie w naturalnym porządku a porządek kluczy w tablicy
Date: 2011-02-04 11:35
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Slug: sortowanie-w-naturalnym-porzadku-a-porzadek-kluczy-w-tablicy
Status: published

Sortowanie tablicy w naturalnym porządku z uwzględnieniem przebudowania kolejności kluczy:  
\[code language="php"\]  
\$a=array('1 dzień', '17 dni', '3 dni', '33 dni', '2 dni', '100 dni', '3 dni', '12 dni', '45 dni', '11 dni');  
natcasesort(\$a);  
print\_r(array\_values(\$a));  
\[/code\]
