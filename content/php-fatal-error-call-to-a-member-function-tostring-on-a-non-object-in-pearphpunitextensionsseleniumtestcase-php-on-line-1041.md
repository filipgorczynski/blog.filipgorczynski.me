Title: Błąd podczas testów - PHP Fatal error: Call to a member function toString() on a non-object in ./PEAR/PHPUnit/Extensions/SeleniumTestCase.php on line 1041
Date: 2012-01-07 11:46
Author: filipgorczynski
Category: Dobre praktyki, Programowanie, Rozwiązania
Slug: php-fatal-error-call-to-a-member-function-tostring-on-a-non-object-in-pearphpunitextensionsseleniumtestcase-php-on-line-1041
Status: published

\[code language="text"\]  
H:\\htdocs\\demo\\protected\\tests\>phpunit functional/SiteTest.php

PHPUnit 3.6.3 by Sebastian Bergmann.

Configuration read from H:\\htdocs\\demo\\protected\\tests\\phpunit.xml

.PHP Fatal error: Call to a member function toString() on a non-object in C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Extensions\\SeleniumTestCase.php on line 1041  
PHP Stack trace:  
PHP 1. {main}() C:\\wamp\\bin\\php\\php5.3.4\\phpunit:0  
PHP 2. PHPUnit\_TextUI\_Command::main() C:\\wamp\\bin\\php\\php5.3.4\\phpunit:44  
PHP 3. PHPUnit\_TextUI\_Command-\>run() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\TextUI\\Command.php:125  
PHP 4. PHPUnit\_TextUI\_TestRunner-\>doRun() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\TextUI\\Command.php:187  
PHP 5. PHPUnit\_Framework\_TestSuite-\>run() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\TextUI\\TestRunner.php:325  
PHP 6. PHPUnit\_Framework\_TestSuite-\>run() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestSuite.php:705  
PHP 7. PHPUnit\_Framework\_TestSuite-\>runTest() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestSuite.php:745  
PHP 8. PHPUnit\_Extensions\_SeleniumTestCase-\>run() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestSuite.php:772  
PHP 9. PHPUnit\_Framework\_TestResult-\>run() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Extensions\\SeleniumTestCase.php:527  
PHP 10. PHPUnit\_Framework\_TestCase-\>runBare() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestResult.php:649  
PHP 11. PHPUnit\_Extensions\_SeleniumTestCase-\>onNotSuccessfulTest() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestCase.php:888

Fatal error: Call to a member function toString() on a non-object in C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Extensions\\SeleniumTestCase.php on line 1041

Call Stack:  
0.0009 633648 1. {main}() C:\\wamp\\bin\\php\\php5.3.4\\phpunit:0  
0.1198 1189176 2. PHPUnit\_TextUI\_Command::main() C:\\wamp\\bin\\php\\php5.3.4\\phpunit:44  
0.1199 1189760 3. PHPUnit\_TextUI\_Command-\>run() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\TextUI\\Command.php:125  
1.2804 7611776 4. PHPUnit\_TextUI\_TestRunner-\>doRun() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\TextUI\\Command.php:187  
1.3653 8098120 5. PHPUnit\_Framework\_TestSuite-\>run() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\TextUI\\TestRunner.php:325  
1.3654 8098680 6. PHPUnit\_Framework\_TestSuite-\>run() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestSuite.php:705  
12.7230 8521360 7. PHPUnit\_Framework\_TestSuite-\>runTest() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestSuite.php:745  
12.7230 8521360 8. PHPUnit\_Extensions\_SeleniumTestCase-\>run() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestSuite.php:772  
12.7230 8521408 9. PHPUnit\_Framework\_TestResult-\>run() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Extensions\\SeleniumTestCase.php:527  
12.7230 8522416 10. PHPUnit\_Framework\_TestCase-\>runBare() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestResult.php:649  
22.3495 8661592 11. PHPUnit\_Extensions\_SeleniumTestCase-\>onNotSuccessfulTest() C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestCase.php:888  
\[/code\]

W pliku C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Extensions\\SeleniumTestCase.php linijkę 1041 zmieniamy z:

\[code language="php"\]  
\$message = \$e-\>getComparisonFailure()-\>toString();  
\[/code\]

na

\[code language="php"\]  
\$message = \$e-\>getComparisonFailure()-\>exceptionToString;  
\[/code\]  
Powinno zadziałać:  
\[code language="text"\]\</pre\>  
H:\\htdocs\\demo\\protected\\tests\>phpunit functional/Sitetest.php  
PHPUnit 3.6.3 by Sebastian Bergmann.

Configuration read from H:\\htdocs\\demo\\protected\\tests\\phpunit.xml

..E

Time: 37 seconds, Memory: 8.50Mb

There was 1 error:

1\) SiteTest::testLoginLogout  
Trying to get property of non-object

C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Extensions\\SeleniumTestCase.php:1042  
C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestCase.php:888  
C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestResult.php:649  
C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Extensions\\SeleniumTestCase.php:527  
C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestSuite.php:772  
C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestSuite.php:745  
C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\Framework\\TestSuite.php:705  
C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\TextUI\\TestRunner.php:325  
C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\TextUI\\Command.php:187  
C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\PHPUnit\\TextUI\\Command.php:125  
C:\\wamp\\bin\\php\\php5.3.4\\phpunit:44

FAILURES!  
Tests: 3, Assertions: 6, Errors: 1.  
\[/code\]


