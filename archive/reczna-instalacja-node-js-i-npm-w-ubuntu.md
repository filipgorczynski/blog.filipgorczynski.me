Title: Ręczna instalacja Node.js i npm w Ubuntu
Date: 2018-02-26 17:00
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: instalacja, ln, node, Node.js, NodeJs, npm, PATH, Ubuntu
Slug: reczna-instalacja-node-js-i-npm-w-ubuntu
Status: hidden

![NodeJS Logo](https://filipgorczynski.files.wordpress.com/2017/03/nodejs-new-pantone-black-e1489221708700.png){.alignleft .wp-image-1281 .size-full width="150" height="92"}

Standardowa instalacja node.js w Ubuntu z dostępnych repozytoriów poprzez `sudo apt-get install nodejs` nie zawsze pozwala uzyskać nam najświeższą wersję. Dla Ubuntu 16.04 zapytanie o paczkę nodejs zwraca nam wersję `4.2.6`:

 

https://gist.github.com/filipgorczynski/0adc6858edd4ac62b63893066b42b0d5

Jednym słowem, smuteczek.  
Po wejściu na stronę projektu [nodejs.org](https://nodejs.org/en/) w oczy rzucają się od razu 2 wersje: `8.9.4` (Long Time Support, stabilna i zalecana dla większości użytkowników) oraz `9.6.1` - Current - PRAWIE najświeższa z możliwych, bo są jeszcze tzw. Nightly Build dla ludzi z dużą ilością czasu wolnego :).

Jednym ze sposobów sprawdzenia wersji paczki zainstalowanej aktualnie w systemie - oczywiście o ile jest zainstalowana - jest:

https://gist.github.com/filipgorczynski/5910c50601d20f98f8a54f4b3e345a9a

My jednak chcielibyśmy korzystać z najświeższej stabilnej wersji - `8.9.4`.

Z wcześniej podanej strony pobieramy archiwum i rozpakowujemy:

https://gist.github.com/filipgorczynski/f28575cb8e08eb8445d46a37f9edb0c1

Rozpakowany katalog `node-v8.9.4-linux-x64` wrzucamy na przykład do katalogu `/opt/`:

https://gist.github.com/filipgorczynski/f1bdf255f8f337218eac17beb6d33b8f

Opcjonalnie zmieniamy rekurencyjnie właściciela katalogów i plików w lokalizacji `/opt/node-v8.9.4-linux-x64`:

https://gist.github.com/filipgorczynski/ccc2da9b423cb47bf1db50c49fac150e

Może to być przydatne, gdybyśmy chcieli kiedyś w tym katalogu coś zapisywać (np. inne pliki binarne) oraz instalować pakiety z `npm`.  
Pozostaje nam utworzyć dowiązania symboliczne:

https://gist.github.com/filipgorczynski/54e959541cd404a01ef7254b2c8824c9

Jeśli próba uruchomienia poleceń `node` i `npm` się nie powiedzie jest dość prawdopodobne, że te ścieżki nie są dodane do naszej zmiennej środowiskowej PATH. Może to być przydatne w przyszłości, gdy w katalogu `bin` znajdzie się więcej plików wykonywalnych.  
Aktualną zawartość zmiennej PATH możemy wyświetlić poleceniem `echo $PATH` i aby rozszerzyć tą zmienną o nowe katalogi zmieniamy w pliku `~/.bashrc` zmienną środowiskową:

https://gist.github.com/filipgorczynski/7805951db9787e2a8315e9351d442d64

Żeby wprowadzone zmiany w ramach `~/.bashrc` odniosły skutek powinniśmy go "przeładować": `source ~/.bashrc`

Przydatny okazać się może poniższy skrypt, który w sumie spina wszystko w całość i pozwala prześledzić wykonane akcje krok po kroku:

https://gist.github.com/filipgorczynski/57fd51b267aecd2074281302aa2e7969
