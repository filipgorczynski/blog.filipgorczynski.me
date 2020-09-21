Title: SSH w Windows i komunikat "The server's host key is not cached in the registry"
Date: 2014-10-18 21:28
Author: filipgorczynski
Category: Tech, Systemy Operacyjne
Tags: clone, git, GitHub, keys, pageant, plink, ssh
Slug: ssh-w-windows-i-komunikat-the-servers-host-key-is-not-cached-in-the-registry
Status: archive

[![Git](https://filipgorczynski.files.wordpress.com/2014/09/gitlogo.png?w=150){.alignleft .wp-image-886 .size-thumbnail width="150" height="150"}](http://filipgorczynski.wordpress.com/2014/09/17/windows-7-git-ssh-agent-could-not-open-a-connection-to-your-authentication-agent/gitlogo/)

Git mimo utworzenia poprawnych kluczy, dodania ich do agenta (*pageant.exe*) i dodania klucza SSH w konfiguracji GitHub, przy próbie np.: klonowania projektu, wyświetla komunikat:

\[code language="text"\]

The server's host key is not cached in the registry. You  
have no guarantee that the server is the computer you  
think it is.  
The server's rsa2 key fingerprint is:  
ssh-rsa 2048 xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx  
Connection abandoned.  
fatal: The remote end hung up unexpectedly

\[/code\]

Ponieważ wszystko co należało zrobić - zostało zrobione, zaczęło się grzebanie i próbowanie wszystkiego co tylko mogło przyjść do głowy.

Dopiero po wykonaniu poniższego polecenia wszystko zaczęło działać jak należy:

\[code language="text"\]plink.exe git\@github.com\[/code\]

*plink.exe* instalowany jest np. z pakietem PuTTY.
