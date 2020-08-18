Title: Przeniesienie wybranych elementów z początku tablicy na jej koniec
Date: 2011-04-26 16:24
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Slug: przeniesienie-wybranych-elementow-z-poczatku-tablicy-na-jej-koniec
Status: published

\[code language="javascript"\]  
var t = \['jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć'\];  
var t2 = t.splice(0,2);  
console.log(t.concat(t2));  
// \["trzy", "cztery", "pięć", "sześć", "jeden", "dwa"\]  
\[/code\]
