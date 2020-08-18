Title: Włączanie obsługi IPv6 w Windows XP
Date: 2010-12-23 09:42
Author: filipgorczynski
Category: Rozwiązania, Systemy Operacyjne
Slug: wlaczanie-obslugi-ipv6-w-windows-xp
Status: published

Szacowany czas do "końca internetu", czyli wyczerpania się puli adresów IPv4 na chwile obecną to około 55 dni.  
Żeby się nagle nie okazało, że "nie działa Internet" można zainstalować w Windows XP nowy protokół.  
Można to zrobić na 2 sposoby:

-   Dla klikatych
    -   Start
    -   Ustawienia
    -   Połączenia sieciowe
    -   Prawym przyciskiem myszy klikamy na naszym połączeniu
    -   Z menu wybieramy **właściwości**
    -   W otwartym okienku (właściwości połączenia) klikamy **Zainstaluj**
    -   Wybieramy **Protokół** i **OK**
    -   Wybieramy **Microsoft TCP/IP wersja 6**
    -   Zatwierdzamy
-   Dla nieklikatych
    -   Windows+R (wywołujemy okienko Uruchom)
    -   wpisujemy *cmd.exe*
    -   w otwartym oknie wpisujemy *ipv6 install*

We właściwościach połączenia powinna pojawić się nowa funkcja: *Microsoft TCP/IP wersja 6*.  
I pozostaje czekać. Jeśli nasz sprzęt nie będzie oponował, wszystko powinno śmigać.  
Jako dodatkową lekturę polecam [Windows XP IPv6](http://ipv6int.net/systems/windows_xp-ipv6.html)
