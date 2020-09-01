Title: PyCharm - jedna konfiguracja na wielu instancjach
Date: 2018-04-20 15:44
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: GitHub, PyCharm, repository, settings
Slug: pycharm-jedna-konfiguracja-na-wielu-instancjach
Status: archive

![PyCharm Logo](https://filipgorczynski.files.wordpress.com/2018/03/pycharm_logo.png){.alignleft .wp-image-1675 .size-full width="128" height="128"}Ponownie chciałbym pochwalić PyCharma - w sumie to wszystkie IDE od JetBrains.

Otóż narzędzie to pozwala nam na współdzielenie naszej ulubionej konfiguracji środowiska pomiędzy różnymi instancjami - jeśli używamy tego IDE w pracy i w domu to warto z tego skorzystać.  
Oczywiście ma to też ten plus, że w przypadku kradzieży/zniszczenia możemy w całkiem prosty sposób odzyskać poprzednią konfigurację.

A sprawa jest całkiem prosta:

1.  Zakładamy nowe repozytorium, np. w serwisie GitHub (tak, może być też GitLab albo jakiekolwiek inne - ja lubię GitHub)
2.  W PyCharm wybieramy kolejno `File` \> `Settings Repository` i ustawiamy konkretny `Upstream URL` na adres repozytorium  
   ![PyCharm Settings](https://filipgorczynski.files.wordpress.com/2018/04/pycharm-settings-repository.png){.aligncenter .wp-image-1845 .size-full width="427" height="128"}
3.  Nadpisujemy zdalne (Overwrite Remote)
4.  To samo robimy na pozostałych instancjach nadpisując ustawienia lokalne (Overwrite Local)

Gdy już mamy zsynchronizowane, każda zmiana powinna być automatycznie pobierana z i wysyłana do repozytorium - jednak opcja Merge też w niektórych sytuacjach może się przydać :)
