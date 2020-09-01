Title: Windows 7, Git, SSH agent - Could not open a connection to your authentication agent.
Date: 2014-09-17 20:14
Author: filipgorczynski
Category: Programowanie, Rozwiązania, Systemy Operacyjne
Slug: windows-7-git-ssh-agent-could-not-open-a-connection-to-your-authentication-agent
Status: archive

[![Git](http://filipgorczynski.files.wordpress.com/2014/09/gitlogo.png?w=150){.alignleft .wp-image-886 width="125" height="125"}](https://filipgorczynski.files.wordpress.com/2014/09/gitlogo.png)Po zainstalowaniu Git, stworzeniu nowych kluczy prywatnego i publicznego oraz dodaniu ich do Bitbucketa, mimo wykonania polecenia:

\[code language="text"\]git clone \[url-repozytorium\]\[/code\]

otrzymujemy komunikat:

\[code language="text"\]Could not open a connection to your authentication agent.\[/code\]

W sieci znalazłem kilka propozycji rozwiązania problemu, ale większość działa jedynie na środowiskach nie Windowsowych i kończy się wykonaniem polecenia eval `ssh-agent`, które na Windowsie oczywiście nie działa.

Moja propozycja rozwiązania.  
Pobieramy i instalujemy PuTTY, szczególnie będzie nas interesował PuTTY i Pageant. Jeśli już posiadamy zainstalowaną wersję PuTTY mogliśmy wykorzystywać PuTTYgen do stworzenia pary naszych kluczy.

Uruchamiamy PuTTY, w pole adresu wpisujemy *[bitbucket.org](http://bitbucket.org/) (*lub [*github.com*](http://github.com/) - w zależności od tego, który host nas interesuje*)*, port zostawiamy domyślny, możemy zaznaczyć opcję, aby nie zamykał okienka, ale to raczej nie ma wielkiego znaczenia.  
Próbujemy się połączyć z tym hostem, przed połączeniem poprosi nas o potwierdzenie, czy klucz danego hosta ma zostać dodany do zaufanych. Klikamy **TAK**. I tutaj już za wiele nam nie będzie potrzebne więc można wszystko pozamykać.  
Uruchamiamy Pageant i ładujemy do niego nasz klucz - plik \*.ppk, znajdujący się przykładowo w *\~/.ssh/id\_rsa.ppk*).

Po załadowaniu klucza do Pageant powinniśmy już bezproblemowo móc wykonać wszelakie operacje na repozytorium: push, pull, itd.
