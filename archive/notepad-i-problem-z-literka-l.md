Title: Notepad++ i problem z literką ł
Date: 2011-11-26 20:34
Author: filipgorczynski
Category: Rozwiązania
Tags: literka ł, Notepad++, NppScripting, NppScripting.dll, plugin, Zen Coding, Zen Coding Python
Slug: notepad-i-problem-z-literka-l
Status: hidden

Natknąłem się na dziwną przypadłość Notepad++, której niestety nie udało się skonfigurować. Instalacja pluginu Zen Coding spowodowała brak możliwości wprowadzenia literki ł. Rozwiązaniem niestety okazało się usunięcie tego pluginu poprzez usunięcie z katalogu C:\\Program Files (x86)\\Notepad++\\plugins  NppScripting.dll i katalogu NppScripting. Nie zauważyłem jeszcze ubocznych efektów po usunięciu tego rozszerzenia.

Wysłanie maila do autorów poskutkowało poniższą odpowiedzią:

1\. Otwórz plik %Notepad++%\\plugins\\NppScripting\\includes\\Zen Coding.js  
a. Jeśli plik nie istnieje użyj %Notepad++%\\plugins\\NppScripting\\start.js  
2. Znajdź następujący tekst "addMenuItem('Klucz', 'wartość', 'Ctrl+Alt+L');"  // linijka 8003  
3. Dokonaj odpowiednich zmian i zapisz
