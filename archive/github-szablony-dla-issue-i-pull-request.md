Title: GitHub - szablony dla Issue i Pull Request
Date: 2018-03-12 17:04
Author: filipgorczynski
Category: Dobre praktyki
Tags: GitHub, issu, issue_template, pull request, pull request_template, templates
Slug: github-szablony-dla-issue-i-pull-request
Status: archive

![Octocat](https://filipgorczynski.files.wordpress.com/2018/03/octocat.png){.alignleft .wp-image-1742 .size-full width="128" height="128"}

Ciekawą funkcją GitHuba - szczególnie przydatną w przypadku wieloosobowych zespołów są szablony dla nowo tworzonych Pull Requestów lub Issue.

Jeśli zależy nam na fajnej kulturze pracy z kodem możemy sobie takie szablony zaaplikować w swoich repozytoriach i na szczęście nie jest to skomplikowane i kończy się w momencie utworzenia plików o odpowiednich nazwach: `issue_template.md` oraz `pull_request_template.md`, na przykład w katalogu `.github`, który także tworzymy w naszym projekcie.

Jak widać po rozszerzeniu, pliki te to po prostu najzwyklejsze dokumenty [Markdown](https://pl.wikipedia.org/wiki/Markdown), więc w ich treść można wrzucić wszystko, co Markdown jest w stanie obsłużyć: nagłówki, pogrubienie tekstu, kursywę, dowolne typy list, kawałki kodu czy co najfajniejsze - pola do zaznaczenia.

Prosty Issue Template:

https://gist.github.com/filipgorczynski/200da45e7c4a3cc7268cf1ba6ba75525

oraz Pull Request Template:

https://gist.github.com/filipgorczynski/b5ee73ffacad094b9dac00d1cc3cb8fb

W przypadku automatyzacji Pull Requestów można nasz szablon rozdzielić na kilka różnych plików i przekazując odpowiednie parametry w adresie - sterować wybieranym szablonem. Szczegóły można znaleźć na w dokumentacji [GitHub](https://help.github.com/articles/about-automation-for-issues-and-pull-requests-with-query-parameters/).

Więcej przykładów oraz informacji znaleźć można w następujących repozytoriach: [github-issue-templates](https://github.com/stevemao/github-issue-templates) i [awesome-github-templates](https://github.com/devspace/awesome-github-templates).

 
