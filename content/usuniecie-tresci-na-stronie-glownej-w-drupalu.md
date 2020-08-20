Title: Usunięcie treści na stronie głównej w Drupalu
Date: 2012-12-14 11:45
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Slug: usuniecie-tresci-na-stronie-glownej-w-drupalu
Status: draft

Tworzymy lub włączamy widok "Frontpage", określamy mu co ma wyświetlać, zapisujemy. W sites configuration określamy frontpage jako ścieżkę. W pliku page--front.tpl.php renderujemy poprawnie echo render(\$page\['content'\]);
