Title: Robot Framework - zmiana rozmiaru okna i dokumentu
Date: 2019-12-04 08:47
Author: filipgorczynski
Category: Tech
Slug: robot-framework-zmiana-rozmiaru-okna-i-dokumentu
Status: draft

![Robot Framework](https://filipgorczynski.files.wordpress.com/2019/05/robot-framework-logo.png?w=128){.alignleft .size-thumbnail .wp-image-2234 width="128" height="128"}

 

Selenium: `https://www.testingexcellence.com/resize-browser-window-webdriver/`

`https://help.applitools.com/hc/en-us/articles/360007187871-Configuring-the-browser-viewport-size-for-your-visual-tests`

`https://www.guru99.com/maximize-resize-minimize-browser-selenium.html`

FILE: [tests/e2e/common.py](https://github.com/unhaggle/tier3/compare/qa_71?expand=1#diff-4b55feed0f2604f102be3c29098555aa "unhaggle/moto_dealer/tests/e2e/common.py"){.link-gray-dark}

from robot.libraries.BuiltIn import BuiltIn

def get\_webdriver\_instance():  
""""""  
se = BuiltIn().get\_library\_instance('SeleniumLibrary')  
return se.\_current\_browser()

def set\_viewport\_size(driver, width, height):  
""""""  
window\_size = driver.execute\_script("""  
return \[window.outerWidth - window.innerWidth + arguments\[0\],  
window.outerHeight - window.innerHeight + arguments\[1\]\];  
""", width, height)

driver.set\_window\_size(\*window\_size)

 

 

\*\*\* Settings \*\*\*  
Documentation Common Elements  
Library SeleniumLibrary  
Library ../common.py

\*\*\* Variables \*\*\*  
\${DISPLAY}= \${None}

\*\*\* Keywords \*\*\*  
Begin Web Test  
\[Arguments\] \${browser}=\${RF\_BROWSER}

Set Global Variable \${DISPLAY} \${RF\_DISPLAY}  
Log Execute using "\${browser}" browser on "\${DISPLAY}" screen size  
Open Browser about:blank \${browser}  
Delete All Cookies  
Set Screen Size

End Web Test  
\# Customer Web.Clear Cart  
Delete All Cookies  
Close Browser

Set Screen Size  
Run Keyword If "\${DISPLAY}" == "xs" Set XS Screen Size  
Run Keyword If "\${DISPLAY}" == "sm" Set SM Screen Size  
Run Keyword If "\${DISPLAY}" == "md" Set MD Screen Size  
Run Keyword If "\${DISPLAY}" == "lg" Set LG Screen Size  
Run Keyword If "\${DISPLAY}" == "xlg" Set XLG Screen Size

Set XLG Screen Size  
Set Window Size 1366 1024

Set LG Screent Size  
Set Window Size 1200 1024  
\# \${web\_driver}= Get Webdriver Instance  
\# Run Keyword If "\${is\_horizontal}" == "True" Set Viewport Size \${web\_driver} 768 1024  
\# Run Keyword If "\${is\_horizontal}" == "True" Set Window Size 768 1024  
\# Run Keyword If \${is\_horizontal} == False Set Viewport Size \${web\_driver} 1024 768

Set MD Screen Size  
Set Window Size 992 1024  
\# \${web\_driver}= Get Webdriver Instance  
\# Run Keyword If "\${is\_horizontal}" == "True" Set Viewport Size \${web\_driver} 768 1024  
\# Run Keyword If "\${is\_horizontal}" == "True" Set Window Size 768 1024  
\# Run Keyword If \${is\_horizontal} == False Set Viewport Size \${web\_driver} 1024 768

Set SM Screen Size  
\# \[Arguments\] \${is\_horizontal}=True

Set Window Size 768 1024  
\# \${web\_driver}= Get Webdriver Instance  
\# Run Keyword If "\${is\_horizontal}" == "True" Set Viewport Size \${web\_driver} 768 1024  
\# Run Keyword If "\${is\_horizontal}" == "True" Set Window Size 768 1024  
\# Run Keyword If \${is\_horizontal} == False Set Viewport Size \${web\_driver} 1024 768

Set XS Screen Size  
\# \[Arguments\] \${is\_horizontal}=True

Set Window Size 380 1024  
\# \${web\_driver}= Get Webdriver Instance  
\# Run Keyword If "\${is\_horizontal}" == "True" Set Viewport Size \${web\_driver} 768 1024  
\# Run Keyword If "\${is\_horizontal}" == "True" Set Window Size 768 1024  
\# Run Keyword If \${is\_horizontal} == False Set Viewport Size \${web\_driver} 1024 768
