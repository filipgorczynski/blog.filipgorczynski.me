Title: git - moduły zależne
Date: 2018-04-23 06:22
Author: filipgorczynski
Category: Tech
Tags: GitHub, moduły zależne, podrepozytoria, submodules
Slug: git-moduly-zalezne
Status: draft

![Octocat](https://filipgorczynski.files.wordpress.com/2018/03/octocat.png){.alignleft .wp-image-1742 .size-full width="128" height="128"}Nierzadko zdarza się, że projekty podzielone są na zależne od siebie części bądź zależą od bibliotek innych firm lub też po prostu chcemy wprowadzić separację pewnych części projektu między sobą. Submoduły, czy może inaczej - moduły zależne - to w GitHubie jeden ze sposobów organizowania takich zależności. Moduły zależne pozwalają nam na dołączanie w projekcie "relacji" do innych repozytoriów, dostępnych następnie w naszym projekcie pod konkretną ścieżką.

Tak jak sam git stara się możliwie najwięcej rzeczy uprościć, nie inaczej dzieje się w przypadku dodawania submodułów wewnątrz projektu (git-subrepositories):

https://gist.github.com/filipgorczynski/fc5ac95284f23ea6cf2ffc0210fbce96

I super, robota skończona :)

No dobra, prawie skończona.

Zwrócić warto uwagę na nowo powstały plik konfiguracyjny `.gitmodules` zawierający mapowanie pomiędzy adresami URL projektów i katalogami lokalnymi, do których projekty te zostały pobrane. Zmieniamy odrobinę ten plik poprzez dodanie informacji o branchu, który nas będzie interesował:

https://gist.github.com/filipgorczynski/7d59110fe8507ee19b7dc097961c594f

Mamy teraz projekty `frontend-subrepository` i `backend-subrepository` w podkatalogach o takich samych nazwach. Podczas dodawania submodułu możemy podać kolejny parametr, który zostanie użyty jako nazwa katalogu, w którym ten moduł miałby się znaleźć.

Ciekawe rzeczy zaczynają się gdy przejdziemy do tych katalogów i wyświetlimy informację o adresie repozytorium:

https://gist.github.com/filipgorczynski/ba63405a7f814722640ef8c9d79791c5

Gdy zmienimy coś w naszym submodule i wypchniemy zmiany (do repozytorium tego konkretnego modułu zależnego) do repozytorium, informacje o nowym commicie będą wskazane w katalogu głównego projektu:

https://gist.github.com/filipgorczynski/ed8da6128b95bc6b3cb398c5e4d65eb0

Klonowanie repozytorium z modułami zależnymi może się okazać nieintuicyjne:

`git clone git@github.com:filipgorczynski/git-subrepositories.git ~/src/submodules-test`

I jeśli teraz przejdziemy do katalogu modułu zależnego to możemy się delikatnie zdziwić - katalog będzie pusty. Smuteczek - trzeba będzie otworzyć zimno piwo by radość wróciła.

Gdy już otworzysz piwo musisz uruchomić dwie komendy w katalogu projektu: `git submodule init`, aby zainicjować lokalny plik konfiguracyjny, oraz `git submodule update`, aby pobrać wszystkie dane z tego projektu i nałożyć zmiany dotyczące tego modułu z projektu głównego:

https://gist.github.com/filipgorczynski/282a55b95f8f12f72d62b4df17daa7da

Jeśli teraz wprowadzimy zmiany i je zatwierdzimy w module zależnym, to po wejściu do katalogu projektu podczas próby uzyskania informacji o aktualnym statusie projektu otrzymamy komunikat zbliżony do poniższego:

https://gist.github.com/filipgorczynski/d5fa98f3b63dc0016a995d923460dbd9

Więc ostatecznie pozostanie nam wykonanie w katalogu projektu `git add backend-subrepository`, wpisanie sensownego opisu dla `commita` oraz

Dodatkowe źródła do poczytania:

1.  [Git Submodules: Adding, Using, Removing, Updating](https://chrisjean.com/git-submodules-adding-using-removing-and-updating/)
2.  [Mastering Git submodules](https://medium.com/@porteneuve/mastering-git-submodules-34c65e940407)
3.  [How to use Git submodules](http://blog.joncairns.com/2011/10/how-to-use-git-submodules/)

Podgląd jak to wygląda w praktyce na GitHubie:

1.  [GIT Submodules](https://github.com/filipgorczynski/git-subrepositories)
2.  [GIT Submodules Frontend](https://github.com/filipgorczynski/frontend-subrepository)
3.  [GIT Submodules Backend](https://github.com/filipgorczynski/backend-subrepository)

 

**UWAGA:** We wpisie została dodana ikonka GitHuba ponieważ podoba mi się bardziej niż ikonka Gita :)
