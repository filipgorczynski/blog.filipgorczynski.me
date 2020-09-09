Title: Dzielenie łańcucha znaków na sensowne słowa
Date: 2017-12-30 11:26
Author: filipgorczynski
Category: Programowanie
Slug: dzielenie-lancucha-znakow-na-sensowne-slowa
Status: draft

[![Python Logo](https://filipgorczynski.files.wordpress.com/2015/04/python1.png){.alignleft .size-full .wp-image-1002 width="128" height="128"}](https://filipgorczynski.files.wordpress.com/2015/04/python1.png)

Dzielenie dłuższego łańcucha znaków na pojedyncze (w miarę sensowne) słowa to działanie całkiem popularne w trakcie programowania. Rozwiązanie wydaje się całkiem proste:

\[code language="python"\]

print("\\t\\tTutaj     bardzo \\n  długi łańcuch znaków.   ".split())

\# \['Tutaj', 'bardzo', 'długi', 'łańcuch', 'znaków.'\]

\[/code\]

Wygląda dobrze. jak to w życiu - skomplikujmy trochę:

\[code language="python"\]

print("\\t,;\\tTutaj ;\\'\[    bardzo \\n  długi\^łańcuch\$znaków.   ".split())

\# \[',;', 'Tutaj', ";'\[", 'bardzo', 'długi\^łańcuch\$znaków.'\]

\[/code\]

Taka forma - choć ma sens - nie do końca jest zadowalająca. split() dzieli domyślnie po białych znakach. Jako jej parametr/argument możemy przekazać dodatkowy łańuch znaków, po którym ma się odbywać cięcie dłuższego łańcucha. Nie możemy przekazać kolekcji \[łańcuchów\] znaków, po których ma się odbywać dzielenie.

Jedno z rozwiązań to wykorzystanie pętli i/lub list comprehension i budowanie listy słów krok po kroku na przykład w taki sposób:

\[code language="python"\]  
import string  
long\_string = r"\\t,;\\tTutaj ;\\'\[    bardzo \\n  długi\^łańcuch\$znaków.   "  
separators = string.punctuation + string.whitespace\</pre\>  
\<pre\>list\_of\_words = \[\]  
word = ''  
for letter in long\_string:  
if letter in separators and len(word):  
list\_of\_words.append(word)  
word = ''  
else:  
word += letter  
print(list\_of\_words)  
\# \['\\t', ';', 'Tutaj', ';', '\[', '\\xa0', '\\xa0bardzo', '\\n', '\\xa0długi', 'łańcuch', 'znaków', ' \\xa0'\]  
\[/code\]

Masa energii na pisanie kodu, jeszcze więcej energii na debugowanie.

 
