Title: Jedna z głównych zasad programowania - nigdy nie zakładaj, że coś działa
Date: 2019-04-26 09:31
Author: filipgorczynski
Category: Life
Slug: jedna-z-glownych-zasad-programowania-nigdy-nie-zakladaj-ze-cos-dziala
Status: draft

TL;DR: Bez względu na informacje jakie docierają do Ciebie z otoczenia, nigdy, ale to przenigdy nie zakładaj, że kod działa prawidłowo, dopóki nie sprawdzisz linijka po linijce, że tak właśnie jest (dla najróżniejszych danych)

Po deploy-u - to działało, więc zakładamy, że cały czas działa - błąd.

Dziedziczymy z klasy bazowej, która została zmieniona? Nasz kod może nie działać

 

Mamy testy dla tej bazy kodu i 100% pokrycia. Odpalamy, testy przechodzą. Skąd mamy gwarancję, że testy są prawidłowo napisane? Brak asercji to nadal przechodzący test. Paranoicznie, możemy mieć napisane testy do testów. A czy piszemy testy testy dla bibliotek, których używamy? Jeśli nie blokujemy wersji bibliotek, z których korzystamy - nie mamy gwarancji, że po zainstalowaniu świeżego środowiska biblioteka, która u programisty była w wersji 1.0, doczekała się aktualizacji i na produkcji ma wersję 2.0 z odmiennym API. Oczekujemy, że metoda zwróci nam tablicę a zwraca słownik - no nie byliśmy przygotowani na taką sytuację.

 

 
