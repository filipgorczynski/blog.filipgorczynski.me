Title: Instalacja pylibmc - fatal error: Python.h: Nie ma takiego pliku ani katalogu
Date: 2019-04-25 13:48
Author: filipgorczynski
Category: Tech
Slug: instalacja-pylibmc-fatal-error-python-h-nie-ma-takiego-pliku-ani-katalogu
Status: draft

\~/Pobrane/pylibmc-1.4.1\$ sudo python setup.py install  
running install  
running build  
running build\_py  
creating build  
creating build/lib.linux-x86\_64-2.7  
creating build/lib.linux-x86\_64-2.7/pylibmc  
copying src/pylibmc/\_\_init\_\_.py -\> build/lib.linux-x86\_64-2.7/pylibmc  
copying src/pylibmc/pools.py -\> build/lib.linux-x86\_64-2.7/pylibmc  
copying src/pylibmc/consts.py -\> build/lib.linux-x86\_64-2.7/pylibmc  
copying src/pylibmc/client.py -\> build/lib.linux-x86\_64-2.7/pylibmc  
copying src/pylibmc/\_\_main\_\_.py -\> build/lib.linux-x86\_64-2.7/pylibmc  
copying src/pylibmc/test.py -\> build/lib.linux-x86\_64-2.7/pylibmc  
running build\_ext  
building '\_pylibmc' extension  
creating build/temp.linux-x86\_64-2.7  
creating build/temp.linux-x86\_64-2.7/src  
gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -DUSE\_ZLIB -I/usr/include/python2.7 -c src/\_pylibmcmodule.c -o build/temp.linux-x86\_64-2.7/src/\_pylibmcmodule.o -fno-strict-aliasing  
In file included from src/\_pylibmcmodule.c:34:0:  
src/\_pylibmcmodule.h:41:20: fatal error: Python.h: Nie ma takiego pliku ani katalogu  
compilation terminated.  
error: command 'gcc' failed with exit status 1

\~/Pobrane/pylibmc-1.4.1\$ sudo apt-get install python2.7-dev

\~/Pobrane/pylibmc-1.4.1\$ sudo python setup.py install  
running install  
running build  
running build\_py  
running build\_ext  
building '\_pylibmc' extension  
gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -DUSE\_ZLIB -I/usr/include/python2.7 -c src/\_pylibmcmodule.c -o build/temp.linux-x86\_64-2.7/src/\_pylibmcmodule.o -fno-strict-aliasing  
gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-z,relro build/temp.linux-x86\_64-2.7/src/\_pylibmcmodule.o -lmemcached -lz -o build/lib.linux-x86\_64-2.7/\_pylibmc.so  
running install\_lib  
copying build/lib.linux-x86\_64-2.7/\_pylibmc.so -\> /usr/local/lib/python2.7/dist-packages  
creating /usr/local/lib/python2.7/dist-packages/pylibmc  
copying build/lib.linux-x86\_64-2.7/pylibmc/\_\_init\_\_.py -\> /usr/local/lib/python2.7/dist-packages/pylibmc  
copying build/lib.linux-x86\_64-2.7/pylibmc/pools.py -\> /usr/local/lib/python2.7/dist-packages/pylibmc  
copying build/lib.linux-x86\_64-2.7/pylibmc/consts.py -\> /usr/local/lib/python2.7/dist-packages/pylibmc  
copying build/lib.linux-x86\_64-2.7/pylibmc/client.py -\> /usr/local/lib/python2.7/dist-packages/pylibmc  
copying build/lib.linux-x86\_64-2.7/pylibmc/\_\_main\_\_.py -\> /usr/local/lib/python2.7/dist-packages/pylibmc  
copying build/lib.linux-x86\_64-2.7/pylibmc/test.py -\> /usr/local/lib/python2.7/dist-packages/pylibmc  
byte-compiling /usr/local/lib/python2.7/dist-packages/pylibmc/\_\_init\_\_.py to \_\_init\_\_.pyc  
byte-compiling /usr/local/lib/python2.7/dist-packages/pylibmc/pools.py to pools.pyc  
byte-compiling /usr/local/lib/python2.7/dist-packages/pylibmc/consts.py to consts.pyc  
byte-compiling /usr/local/lib/python2.7/dist-packages/pylibmc/client.py to client.pyc  
byte-compiling /usr/local/lib/python2.7/dist-packages/pylibmc/\_\_main\_\_.py to \_\_main\_\_.pyc  
byte-compiling /usr/local/lib/python2.7/dist-packages/pylibmc/test.py to test.pyc  
running install\_egg\_info  
Writing /usr/local/lib/python2.7/dist-packages/pylibmc-1.4.1.egg-info
