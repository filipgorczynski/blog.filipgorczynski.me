Title: Obsługa kodowania UTF-8 w edytorze gVim
Date: 2011-11-28 22:25
Author: filipgorczynski
Category: Rozwiązania
Slug: obsluga-kodowania-utf-8-w-edytorze-gvim
Status: published

Jednym z popularniejszych edytorów dla programistów jest gVim. Jednak sama jego instalacja nie wystarczy, by zapisywać pliki w kodowaniu UTF-8 bez znacznika BOM. Rozwiązanie zawdzięczam użytkownikowi devgreg ze strony [devPytania.pl](devPytania.pl). Należy dodać poniższy kawałek kodu

\[code language="text"\]  
if has("multi\_byte")  
if &termencoding == ""  
let &termencoding = &encoding  
endif  
set encoding=utf-8  
setglobal fileencoding=utf-8  
"setglobal bomb  
set fileencodings=ucs-bom,utf-8,latin1  
endif  
\[/code\]

do pliku c:\\Program Files (x86)\\Vim\\\_vimrc.

Źródło: <http://devpytania.pl/questions/6708/gvim-i-poprawna-obsuga-utf-8>
