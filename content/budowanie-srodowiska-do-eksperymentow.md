Title: Budowanie środowiska do eksperymentów
Date: 2019-04-25 13:42
Author: filipgorczynski
Category: Programowanie
Slug: budowanie-srodowiska-do-eksperymentow
Status: draft

https://www.osboxes.org/virtualbox-images/

https://www.osboxes.org/fedora/

Pobrać konkretną wersję na Virtualboxa

W oknie VirtualBox dodajemy nową maszynę wirtualną, wpisujemy Fedora-template, wybieramy konkretne wersje systemu z dropdownów (other linux 65bit) , "DALEJ", ustawiamy RAM na 2048MB, DALEJ, "Hard disk" Use an existing virtual hard disk drive  i wybrać odpowiedni - dopiero co pobrany dysk.

Przed włączeniem konfigurujemy maszynę wirtualną:

Ustawienia > System > Processor na 2

Ustawienia > Sieci > Bridged Adapter

Uruchamiamy: login i hasło to domyślnie osboxes:osboxes.org, aktualna informacja na zakładce Info podczas pobierania obrazu

Uruchamiamy terminal, wpisujemy ifconfig żeby sprawdzić adres IP (przyda się przy łączeniu przez SSH)

Wyłączyć maszynę.

Na podstawie szablonu tworzymy nowe maszyny: klikamy prawym na maszynie i wybieramy Clone. Przy pierwszym klonie nazywamy go Fedora-controller (to będzie nasz sterujący system) i zaznaczamy "Reinitialize the MAC address of all network cards". Na następnym ekranie wybieramy Linked Clone

Pobieramy dla nowo utworzonych maszyn adresy IP (jak wcześniej) do połączeń SSH.

W utworzonych maszynach edytujemy /etc/hostname nadając nazwy pozwalające odróżnić nasze maszyny.

Także modyfikujemy plik /etc/hosts na maszynie, i zmieniamy:

127.0.0.1 localhost \*

::1 localhost \*

na

127.0.0.1 localhost nowanazwahosta

localhost localhost nowanazwahosta

 

 

Vagrant (init, itp) do zarządzania maszynami wirtualnymi
