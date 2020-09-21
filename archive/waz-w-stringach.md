Title: Wąż w stringach
Date: 2018-04-20 13:26
Author: filipgorczynski
Category: Dobre praktyki, Programowanie
Tags: f-string, format, interpolacja, pep-0798, string
Slug: waz-w-stringach
Status: archive

![Python Logo](https://filipgorczynski.files.wordpress.com/2015/04/python1.png){.alignleft .wp-image-1002 .size-full width="128" height="128"}

Jednym z pierwszych typów danych o których uczymy się w ramach najróżniejszych kursów programowania jest **typ łańcuchowy** - często określany jako `string`. Nie bez powodu jest to jeden z najczęściej używanych w programowaniu typów. A dlaczego? Ponieważ jako ludzie głównie działamy na tekście: czytamy książki, piszemy listy, ostrzegamy o wysokim napięciu, opisujemy substancje chemiczne, gryzmolimy tagi na rozkładach jazdy (kto wracał komunikacją nocną i nie mógł odczytać rozkładu przez głupie tagi wie, że tego typu teksty są najmniej lubiane) - w dużym skrócie - tekstu używamy wszędzie.

Oczywiście ma to swoje konsekwencje -w programowaniu wykorzystujemy tekst aby wyświetlić cokolwiek na ekranie, do logowania aktualnego stanu aplikacji, gdy prosimy użytkownika o podanie informacji, przesyłamy informacje przez sieć.

Łańcuch znaków jest po prostu kolekcją... znaków. Mogą to być zarówno znaki `drukowalne`, jak np. litery alfabetu, cyfry czy znaki interpunkcyjne lub `niedrukowalne` - znaki o specjalnym znaczeniu - spacje, tabulacje, "dzwonek systemowy".  
Stringi mogą mieć długość od zera do... prawie rozmiaru pamięci zainstalowanej w komputerze. Oczywiście, mają tutaj jeszcze ogromne znaczenie inne czynniki - np. wersja Pythona czy architektura komputera, jednak dla codziennych zastosowań nie powinniśmy się tym aż tak bardzo przejmować. Gdybyśmy jednak chcieli zrobić kopię zapasową Internetu możemy w pewnym momencie zderzyć się z błędem `MemoryError`.

Długość (między innymi) łańcuchów określa się wbudowaną w Pythona funkcją `len` jednak należy mieć na uwadze, że ilość znaków, którą widzimy to nie zawsze rzeczywista długość łańcucha trzymana w pamięci. Posiłkując się [StackOverflow](https://stackoverflow.com/a/2247236/273283):

https://gist.github.com/filipgorczynski/65757e7f1c8402f5b8006d16c3cbeb21

Dla Pythona 2 wyniki są jeszcze bardziej zaskakujące (w odpowiedzi na StackOverflow został właśnie użyty Python 2).

Stringi w Pythonie możemy zapisywać w kodzie na kilka różnych sposobów:

https://gist.github.com/filipgorczynski/7aa4c5f63661cfdbfa365973af72d2e6

Jednak wyświetlanie na ekranie prostych łańcuchów znaków może w pewnym momencie stać się dość nudne - na szczęście wynaleziono `interpolację`.

Interpolacja to wg Słownika Języka Polskiego: *"wstawienie wyrazów, zwrotów, zdań do pierwotnego tekstu; też: takie wstawione wyrazy, zwroty, zdania"*.  
W naszej sytuacji chodzi o podstawienie wartości ze zmiennych w konkretne miejsca w łańcuchu znaków.  
Przykładowo jeśli posiadamy szablon z informacją o uczniu i jego ocenie: `"Cześć {imię i nazwisko ucznia}. Uzyskałeś {ilość punktów} punktów z egzaminu."` to każde nasze wystąpienie `{coś tam}` będziemy mogli podmienić konkretnymi wartościami.  
Do uzyskania konkretnego łańcucha znaków - z już podmienionymi wartościami możemy podejść (ponownie) na kilka sposobów - lepszych lub gorszych.  
I tak na przykład, jednym z nich - niezbyt fajnym ani wygodnym - będzie po prostu łączenie łańcuchów znaków:

https://gist.github.com/filipgorczynski/f8189939c9d5c5d920bc390d7793a1a7

Nie da się chyba tego lubić. Przy okazji warto zwrócić uwagę, że pamiętać musimy o rzutowaniu na odpowiedni typ funkcją `str` albo zderzymy się z błędem `TypeError`.

Inny ciekawy (dla masochistów) sposób, to zapisanie wszystkiego jako lista i jej połączenie pustym łańcuchem:

https://gist.github.com/filipgorczynski/880c17d22d041d600c0d84d581fa85ca

Kod tak wspaniały, że aż oczy bolą... No dobra, są sytuacje, gdzie podobne podejście będzie akceptowalne, całkiem zwięzłe i czytelne... ale to nie jest ten przypadek.

Zmierzamy powoli w kierunku lepszego jutra - rozwiązanie dość popularne jeszcze do niedawna:

https://gist.github.com/filipgorczynski/23d0569db527940b7f469086d81baa18

Plusem tego sposobu interpolowania łańcucha jest to, że korzysta on z wielu dostępnych [specyfikatorów formatowania](https://docs.python.org/3.6/library/string.html#format-specification-mini-language) - co pozwala nam z kolei przyoszczędzić na jawnym konwertowaniu wartości zmiennych na łańcuchowy typ danych - musimy jednak zadbać o odpowiedni specyfikator w stringu.

Pierwszy z zalecanych (moim zdaniem) sposobów interpolowania to wykorzystanie metody `format` obiektu string:

https://gist.github.com/filipgorczynski/e586b7eed78103c8248727933dddf3e5

Sposób ten jest tak fajny, że aż dorobił się [własnej strony internetowej](https://pyformat.info/) z najróżniejszymi przykładami.

Drugim zalecanym (znów, moim zdaniem) sposobem jest użycie tzw `f-stringów` - dostępnych niestety dopiero od Pythona 3.6:

https://gist.github.com/filipgorczynski/cfcb6427456b52cece57576b4696e731

Jeszcze innym sposobem interpolowania o którym warto wspomnieć jest użycie klasy `Template` z modułu `string`:

https://gist.github.com/filipgorczynski/0660c0e88504f25a4b87438e14f2530b

jednak nie spotykałem się z nim zbyt często - warto jednak wiedzieć, że coś takiego jest.

Więcej o samej interpolacji w Pythonie poczytać możemy w oficjalnych dokumentach [PEP-0215](https://www.python.org/dev/peps/pep-0215/), [PEP-0498](https://www.python.org/dev/peps/pep-0498/), [PEP-0501](https://www.python.org/dev/peps/pep-0501/) oraz [PEP-0502](https://www.python.org/dev/peps/pep-0502/).

Dodatkowo, sam łańcuch znaków jako obiekt ma całkiem sporo metod pozwalających operować na danym łańcuchu, przytaczając kilka takich metod:

https://gist.github.com/filipgorczynski/a726ec6e8753eb0689d963e702000dd9

**UWAGA:** Wywołanie takiej metody na stringu nie powoduje jej zmiany w pamięci.

I tym oto sposobem przechodzimy do faktu, że łańcuchy znaków są **niezmiennym** typem danych (tzw. `immutable`). Cool. I co to znaczy?  
W dużym skrócie chodzi o to, że jeśli zmienimy łańcuch znaków to zmieni się jego lokalizacja w pamięci - zostanie utworzony nowy, zmodyfikowany obiekt. Najlepiej zaobserwujemy to na przykładzie:

https://gist.github.com/filipgorczynski/d3cc653ab7bb43f2c82c9a19f3dda772

Dla wygody skorzystałem z wbudowanych funkcji [hex](https://docs.python.org/3/library/functions.html#hex) i [id](https://docs.python.org/3/library/functions.html#id).

Na koniec warto wspomnieć o dostarczanym ze standardową biblioteką Pythona modułem `string`, który głównie może okazać się przydatny jeśli będziemy potrzebowali kolekcji znaków: małych lub dużych liter, cyfr (także ósemkowych lub szesnastkowych) czy białych znaków, itp.

**Dodatkowe źródła:**  
\[1\] [A string of unexpected lengths](https://www.recurse.com/blog/74-a-string-of-unexpected-lengths)  
\[2\] [Moduł string](https://docs.python.org/3/library/string.html)
