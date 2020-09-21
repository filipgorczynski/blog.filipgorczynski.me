Title: Grzebiemy w interpreterze Pythona - moduł sys
Date: 2019-04-25 13:38
Author: filipgorczynski
Category: Tech
Slug: grzebiemy-w-interpreterze-pythona-modul-sys
Status: draft

![Python Logo](https://filipgorczynski.files.wordpress.com/2015/04/python1.png){.alignleft .size-full .wp-image-1002 width="128" height="128"}

\>\>\> print(sys.\_\_doc\_\_)  
This module provides access to some objects used or maintained by the  
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv\[0\] is the script pathname if known  
path -- module search path; path\[0\] is the script directory, else ''  
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session  
excepthook -- called to handle any uncaught exception other than SystemExit  
To customize printing in an interactive session or to install a custom  
top-level exception handler, assign other functions to replace these.

stdin -- standard input file object; used by input()  
stdout -- standard output file object; used by print()  
stderr -- standard error object; used for error messages  
By assigning other file objects (or objects that behave like files)  
to these, it is possible to redirect all of the interpreter's I/O.

last\_type -- type of last uncaught exception  
last\_value -- value of last uncaught exception  
last\_traceback -- traceback of last uncaught exception  
These three are only available in an interactive session after a  
traceback has been printed.

Static objects:

builtin\_module\_names -- tuple of module names built into this interpreter  
copyright -- copyright notice pertaining to this interpreter  
exec\_prefix -- prefix used to find the machine-specific Python library  
executable -- absolute path of the executable binary of the Python interpreter  
float\_info -- a struct sequence with information about the float implementation.  
float\_repr\_style -- string indicating the style of repr() output for floats  
hash\_info -- a struct sequence with information about the hash algorithm.  
hexversion -- version information encoded as a single integer  
implementation -- Python implementation information.  
int\_info -- a struct sequence with information about the int implementation.  
maxsize -- the largest supported length of containers.  
maxunicode -- the value of the largest Unicode code point  
platform -- platform identifier  
prefix -- prefix used to find the Python library  
thread\_info -- a struct sequence with information about the thread implementation.  
version -- the version of this interpreter as a string  
version\_info -- version information as a named tuple  
\_\_stdin\_\_ -- the original stdin; don't touch!  
\_\_stdout\_\_ -- the original stdout; don't touch!  
\_\_stderr\_\_ -- the original stderr; don't touch!  
\_\_displayhook\_\_ -- the original displayhook; don't touch!  
\_\_excepthook\_\_ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in builtins.\_  
excepthook() -- print an exception and its traceback to sys.stderr  
exc\_info() -- return thread-safe information about the current exception  
exit() -- exit the interpreter by raising SystemExit  
getdlopenflags() -- returns flags to be used for dlopen() calls  
getprofile() -- get the global profiling function  
getrefcount() -- return the reference count for an object (plus one :-)  
getrecursionlimit() -- return the max recursion depth for the interpreter  
getsizeof() -- return the size of an object in bytes  
gettrace() -- get the global debug tracing function  
setcheckinterval() -- control how often the interpreter checks for events  
setdlopenflags() -- set the flags to be used for dlopen() calls  
setprofile() -- set the global profiling function  
setrecursionlimit() -- set the max recursion depth for the interpreter  
settrace() -- set the global debug tracing function
