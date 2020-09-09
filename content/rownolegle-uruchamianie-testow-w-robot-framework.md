Title: Równoległe uruchamianie testów w Robot Framework
Date: 2019-12-04 08:47
Author: filipgorczynski
Category: Programowanie
Slug: rownolegle-uruchamianie-testow-w-robot-framework
Status: draft

![Robot Framework](https://filipgorczynski.files.wordpress.com/2019/05/robot-framework-logo.png?w=128){.alignleft .size-thumbnail .wp-image-2234 width="128" height="128"}Robot Framework jako pośrednik i narzędzie spajające różne biblioteki testujące sam z siebie niestety nie oferuje możliwości uruchamiania testów równolegle.

Można to jednak osiągnąć wykorzystując bibliotekę `robotframework-pabot` oraz wykorzystać wbudowany w Robot Framework system tagowania. Nie jest to może najwygodniejszy (ani najbardziej oczywisty czy czytelny) sposób, ale daje radę.

Jak się do tego zabrać w praktyce?

pabot \\  
--processes 4 \\  
--argumentfile1 ./dev\_docker/e2e/args/xlg.firefox.txt \  

--argumentfile2 ./dev\_docker/e2e/args/xlg.chrome.txt \\  
--argumentfile3 ./dev\_docker/e2e/args/lg.firefox.txt \\  
--argumentfile4 ./dev\_docker/e2e/args/lg.chrome.txt \\  
--argumentfile5 ./dev\_docker/e2e/args/md.firefox.txt \\  
--argumentfile6 ./dev\_docker/e2e/args/md.chrome.txt \\  
--argumentfile7 ./dev\_docker/e2e/args/sm.firefox.txt \\  
--argumentfile8 ./dev\_docker/e2e/args/sm.chrome.txt \\  
--argumentfile9 ./dev\_docker/e2e/args/xs.firefox.txt \\  
--argumentfile10 ./dev\_docker/e2e/args/xs.chrome.txt \  

--verbose \\  
-d ./logs/results \\  
unhaggle/moto\_dealer/tests/e2e/test-suites

rm ./logs/results/metrics-\*-\*.html  
robotmetrics -I ./logs/results --logo motoinsight-squarelogo.png  
mv ./logs/results/metrics-\*-\*.html ./logs/results/metrics.html

 

 

\*\*lg.chrome.txt\*\*

--exclude skip  
--include develop  
--variable RF\_DISPLAY:lg  
--variable RF\_PRODUCT:usa  
--variable RF\_BROWSER:chrome  
--variable RF\_SERVER:test-{}.localhost.com:8000  
--doc Using Chrome browser on LG screen size

 

import os  
import re  
import sys

class InvalidConfigurationException(Exception):  
pass

def get\_env\_variable(var\_name):  
"""Get the environment variable or return exception."""  
try:  
return os.environ\[var\_name\]  
except KeyError:  
error\_msg = "Set the {} environment variable".format(var\_name)  
raise InvalidConfigurationException(error\_msg)

def parse\_argv\_variables():  
args = {}  
argv = sys.argv  
for index, arg in enumerate(argv):  
if arg == '--argumentfile':  
argumentfile = argv\[index + 1\]  
with open(argumentfile) as argfile:  
for line in argfile.readlines():  
line = line.strip()  
if (  
re.match(r'\^(-v)\|(--variable)', line)  
and ":" in line  
):  
parameter = line.split()\[1\]  
key, value = parameter.split(":", 1)  
args.update({key: value})

return args

RF\_AUTH\_USER = get\_env\_variable("RF\_AUTH\_USER")  
RF\_AUTH\_PASSWORD = get\_env\_variable("RF\_AUTH\_PASSWORD")

default\_params = {  
"RF\_DISPLAY": "xlg",  
"RF\_PRODUCT": "usa",  
"RF\_BROWSER": "chrome",  
"RF\_SERVER": "test-{}.www.test-unhaggle.com:8000",  
"RF\_CUSTOMER\_USER": "super@{}.t3dr.com",  
"RF\_DEALER\_USER": "dealer@{}.t3dr.com",  
"RF\_CUSTOMER\_PASSWORD": "super",  
"RF\_DEALER\_PASSWORD": "super",  
}  
default\_params.update(parse\_argv\_variables())

def get\_argv(params, var\_name):  
try:  
return params\[var\_name\]  
except KeyError:  
error\_msg = "Set the {} command line variable".format(var\_name)  
raise InvalidConfigurationException(error\_msg)

RF\_DISPLAY = get\_argv(default\_params, "RF\_DISPLAY")  
RF\_PRODUCT = get\_argv(default\_params, "RF\_PRODUCT")  
RF\_BROWSER = get\_argv(default\_params, "RF\_BROWSER")  
RF\_CUSTOMER\_USER = get\_argv(default\_params, "RF\_CUSTOMER\_USER")  
if "{}" in RF\_CUSTOMER\_USER:  
RF\_CUSTOMER\_USER = RF\_CUSTOMER\_USER.format(RF\_PRODUCT)  
RF\_CUSTOMER\_PASSWORD = get\_argv(default\_params, "RF\_CUSTOMER\_PASSWORD")  
RF\_DEALER\_USER = get\_argv(default\_params, "RF\_DEALER\_USER")  
if "{}" in RF\_DEALER\_USER:  
RF\_DEALER\_USER = RF\_DEALER\_USER.format(RF\_PRODUCT)  
RF\_DEALER\_PASSWORD = get\_argv(default\_params, "RF\_DEALER\_PASSWORD")  
RF\_SERVER = get\_argv(default\_params, "RF\_SERVER").format(RF\_PRODUCT)  
RF\_AUTH = ""  
RF\_ROOT\_URL = "http://{}{}/".format(RF\_AUTH, RF\_SERVER)
