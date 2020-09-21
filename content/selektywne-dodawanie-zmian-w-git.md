Title: Selektywne dodawanie zmian w Git
Date: 2018-04-11 09:33
Author: filipgorczynski
Category: Tech
Tags: commit, git, git add, interactive, patch
Slug: selektywne-dodawanie-zmian-w-git
Status: draft

![Git](https://filipgorczynski.files.wordpress.com/2014/09/gitlogo.png?w=128){.alignleft .wp-image-886 .size-thumbnail width="128" height="128"}Nie będę ukrywał, że kiedyś zdarzało mi się traktować system kontroli wersji Git jako narzędzie, którego warto używać bo wszyscy go używają. Bez zagłębiania się w szczegóły i możliwości, jakie to narzędzie oferuje: dodaj i zatwierdź zmiany, wyślij do repozytorium, odpocznij.

Jeśli jednak chcemy być coraz lepsi w tym co robimy i aby nasza praca sprawiała nam jeszcze więcej radości a inni programiści patrzyli na nas z zazdrością to jednym z najważniejszych aspektów pracy jako programista jest możliwie najlepsze poznanie swoich narzędzi - a system kontroli wersji, jeśli to możliwe - jeszcze głębiej.

Staram się wyrobić sobie nawyk uważniejszego dodawania zmian do repozytorium.

Do tej pory sprawa najczęściej wyglądała następująco:

Wprowadzam zmiany w różnych plikach. Dodaję je do index (staging) - wszystko jak leci - najczęściej poprzez `git add .`. Zatwierdzam zmiany: git commit -m "super opisowy komunikat". No i wypchnięcie `git push`. Pełny zaciesz, wszystko super - przecież korzystam z systemu kontroli wersji i w dowolnym momencie mogę wrócić do KAŻDEJ wersji kodu źródłowego, jaką kiedykolwiek napisałem.

**No nie do końca.** I spróbujmy to przedstawić na przykładzie. W dalszej części wykorzystam projekt flaskr z repozytorium frameworka Flask - wybór taki motywuję swoim lenistwem do wymyślania kodu i wszelakie zmiany związane są tylko i wyłącznie z prezentacją kilku wartościowych argumentów `git add`.

https://gist.github.com/filipgorczynski/7dd097b4a7b9fa67e75acb8eb9b77236

Wprowadzamy zmiany w kilku plikach i ponownie sprawdzamy status zmian:

https://gist.github.com/filipgorczynski/45196d3ca36a280dcdbb1c2b3fce1410

Szczegółowe zmiany jakie wprowadziliśmy:

https://gist.github.com/filipgorczynski/09912d6d80638d77bc4ce06fc5173f49

Trochę tego jest...

Na pierwszy rzut oka widać, że są to zmiany często ze sobą nie powiązane. Tu domknęliśmy tagi HTML, tam usunęliśmy komentarz, zmieniliśmy rozmiar literek w zapytaniach SQL, rozgrzebaliśmy trochę w importach modułów, w innym jeszcze miejscu zmieniliśmy strukturę sterującą. (I jeszcze raz informuję, że wprowadzone zmiany nie muszą być prawidłowe a chodziło mi o jakiekolwiek zmiany w plikach)

I w tym momencie dochodzimy do celu niniejszego wpisu, argumentów: *-i* (*--interactive*) oraz *-p* (*--patch*) polecenia git add.

Możecie mi wierzyć lub nie, ale te 2 krótkie parametry naprawdę potrafią zatroszczyć się o piękną historię zmian w wypuszczanym na świat kodzie.

git\@github.com:filipgorczynski/git-selective-add.git

[Flaskr Examples](https://github.com/mitsuhiko/flask/tree/master/examples/flaskr)
