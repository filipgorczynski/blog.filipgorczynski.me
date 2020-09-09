Title: Metoda format()
Date: 2015-04-18 10:15
Author: filipgorczynski
Category: Programowanie
Tags: format, Python, string
Slug: metoda-format
Status: draft

\[code language="python"\]

\>\>\> print "\[{:20.5f}\]".format(1.0/3)  
\[ 0.33333\]  
\>\>\> print "\[{:\>20.5f}\]".format(1.0/3)  
\[ 0.33333\]  
\>\>\> print "\[{:\^20.5f}\]".format(1.0/3)  
\[ 0.33333 \]  
\>\>\> print "\[{:\<20.5f}\]".format(1.0/3)  
\[0.33333 \]  
\>\>\> print "\[{:\_\<20.5f}\]".format(1.0/3)  
\[0.33333\_\_\_\_\_\_\_\_\_\_\_\_\_\]  
\>\>\> print "\[{:x\<20.5f}\]".format(1.0/3)  
\[0.33333xxxxxxxxxxxxx\]  
\>\>\> print "\[{:-\<20.5f}\]".format(1.0/3)  
\[0.33333-------------\]  
\>\>\> print "\[{:+\<20.5f}\]".format(1.0/3)  
\[0.33333+++++++++++++\]  
\>\>\> print "\[{:+\>20.5f}\]".format(1.0/3)  
\[+++++++++++++0.33333\]  
\>\>\> print "\[{:-\>20.5f}\]".format(1.0/3)  
\[-------------0.33333\]  
\>\>\> print "\[{:x\>20.5f}\]".format(1.0/3)  
\[xxxxxxxxxxxxx0.33333\]  
\>\>\> print "\[{:\_\>20.5f}\]".format(1.0/3)  
\[\_\_\_\_\_\_\_\_\_\_\_\_\_0.33333\]  
\[/code\]

Źródła warte przeczytania:  
http://pyformat.info/

</pre>
