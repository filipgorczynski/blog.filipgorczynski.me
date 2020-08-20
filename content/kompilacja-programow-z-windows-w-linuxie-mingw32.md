Title: Kompilacja programów z Windows w Linuxie - MinGW32
Date: 2019-04-25 13:07
Author: filipgorczynski
Category: Programowanie, Rozwiązania, Systemy Operacyjne
Slug: kompilacja-programow-z-windows-w-linuxie-mingw32
Status: draft

[![kali\_logo](https://filipgorczynski.files.wordpress.com/2015/05/kali_logo.png){.alignleft .wp-image-1048 .size-full width="128" height="128"}](https://filipgorczynski.files.wordpress.com/2015/05/kali_logo.png)sudo apt-get install wine

wget http://example.com/MinGW

wine /Downloaded/MingGW.exe

MinGW-base

MinGW-gcc

kopiujemy /root/.wine/MinGW/bin pliki \*.dll do katalogu /root/.wine/windows

Możemy już kompilować źródła wykorzystując kompilator gcc z pakietu MinGW działającego pod Windowsem.
