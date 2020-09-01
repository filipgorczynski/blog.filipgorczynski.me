Title: Czysty projekt VueJS 2 i używanie średników a zgodność ze standardami ESLint
Date: 2018-02-22 09:23
Author: filipgorczynski
Category: Dobre praktyki, Programowanie, Rozwiązania
Tags: eslint, eslintrc, semi, vuejs, średnik
Slug: czysty-projekt-vuejs-2-i-uzywanie-srednikow-a-zgodnosc-ze-standardami-eslint
Status: archive

![vuejs logo](https://filipgorczynski.files.wordpress.com/2017/11/vuejs_logo-e1519284315108.png){.alignleft .wp-image-1359 .size-full width="64" height="64"}

JavaScript jako bardzo elastyczny język programowania nie wymaga używania średników na końcu instrukcji. Nie wymaga - i nawet zgodnie z zaproponowanym [standardem JavaScript](https://standardjs.com/rules.html#semicolons), nie zaleca się ich stosowania.

Jednak moim skromnym zdaniem - jako kogoś, kto kiedyś popełnił trochę kodu w C i Perlu - z jakiegoś powodu średniki zostały do składni wprowadzone, a ich stosowanie powoduje (ponownie - to tylko moje osobiste odczucie), że kod staje się też czytelniejszy i ładniejszy.

Utwórzmy zatem czysty projekt z ustawieniami jak poniżej - istotna jest linijka `"Pick an ESLint preset Standard"`, gdyż różne standardy mogą się czepiać nadmiarowych średników lub ich braku.

https://gist.github.com/filipgorczynski/cbca878c4b392dcead2bb6baa3de5b52

VueJS - podczas inicjowania czystego projektu pozwala wybrać standard ESLint, w ramach którego sprawdzana będzie zgodność kodu z tym standardem, m. in. po uruchomieniu serwera deweloperskiego. Przy wyborze `standardowego` sprawdzania składni, dodanie średników na końcach instrukcji będzie skutkowało następującym  błędem:

https://gist.github.com/filipgorczynski/c21c31889769eb822fe57a6c359725b8

Szczegóły błędu dostępne są pod adresem wskazanym w ramach ostrzeżenia: [Extra semicolon](http://eslint.org/docs/rules/semi).

Rozwiązaniem jest dodanie `'semi': [2, 'always']` do pliku `.eslintrc.js`:

https://gist.github.com/filipgorczynski/89860b14183d689acafb1142a9f4c430

Ponowne uruchomienie aplikacji będzie wymagało poprawienia (dodania) średników we wszystkich wskazanych miejscach, jednak nadal twierdzę, że nadmiarowy średnik jest lepszy niż jego pominięcie - gdyż próby zastępowania elementów składni wartościami domyślnymi mogą skutkować kodem podobnym do tego z Perla:

https://gist.github.com/filipgorczynski/1204d6d360114f0c25564ca609ff4db6

Całość dostępna w [repozytorium](https://github.com/filipgorczynski/vuesemicolon).

Dodatkowe źródła i (głównie) kontrargumenty:

1.  [JavaScript Style: Semicolons, or No?](https://adtmag.com/Blogs/Dev-Watch/2016/04/javascript-semicolons.aspx)
2.  [StandardJS\#Semicolons](https://standardjs.com/rules.html#semicolons)
3.  [JavaScript Semicolon Insertion. Everything you need to know](http://inimino.org/~inimino/blog/javascript_semicolons)
4.  [An Open Letter to JavaScript Leaders Regarding Semicolons](http://blog.izs.me/post/2353458699/an-open-letter-to-javascript-leaders-regarding)
5.  [Understanding Automatic Semicolon Insertion in JavaScript](http://www.bradoncode.com/blog/2015/08/26/javascript-semi-colon-insertion/)
