Title: graft - kopiowanie zmian z innych gałęzi do aktualnej gałęzi w mercurialu
Date: 2019-04-25 13:07
Author: filipgorczynski
Category: Programowanie, Rozwiązania, Systemy Operacyjne
Tags: hg branches, hg graft, hg histedit, hg strip, mercurial, transplant
Slug: graft-kopiowanie-zmian-z-innych-galezi-do-aktualnej-galezi-w-mercurialu
Status: draft

![mercurial](https://filipgorczynski.files.wordpress.com/2015/05/mercurial.png){.alignleft .wp-image-1050 .size-full width="128" height="125"}Poniższy przypadek miał miejsce gdy wprowadzając zmiany zapomniałem utworzyć nowej gałęzi (branch) pod kątem zamierzanych zmian. Zmiany wprowadziłem na gałęzi default, zamiast na przykładowo task-10 i w ramach zmian wprowadziłem 2 commity.

W zależności od dotychczasowej konfiguracji Mercuriala Na początku dodajemy 2 wymagane rozszerzenia Mercuriala: histedit oraz strip. Od wersji 2.0 Mercuriala zostało wbudowane polecenie graft w miejsce wcześniejszego rozszerzenia - transplant. Podstawowa różnica pomiędzy transplant a graft jest taka, że graft wykorzystuje wewnętrzne mechanizmy łączenia (merge) Mercuriala, natomiast transplant polega na mechanizmie patchowania.

W ramach przykładu często wykorzystywane będzie polecenie

hg log -b . -l 5 -G

które powoduje wydrukowanie ostatnich zmian w przyjazny dla użytkownika sposób:

hg log  pokazuje historię rewizji dla repozytorium lub plików

-b .  jawnie określamy, że chodzi nam o bieżący branch; możemy oczywiście podać odpowiedni branch zamiast .

-l 5  informujemy, że interesuje nas ostatnich 5 wpisów w historii

-G życzymy sobie wyświetlenia dodatkowej formy graficznej; z lewej strony pojawią się branche; nasza aktualna pozycja określona będzie znakiem @

Dodatkowo plik .hg/hgrc w projekcie zawiera przede wszystkim takie linijki (sytuacja dla Windows 7, nie weryfikowałem konfiguracji na Linuxie):

\[extensions\]  
histedit =  
strip =  
color =

\[histedit\]  
defaultedit = \# set this to make histedit withoud arguments work

w celu włączenia odpowiednich rozszerzeń Mercuriala.

c:\\dev\\projects\\graft\_demo

λ hg init

c:\\dev\\projects\\graft\_demo  
λ ls -al  
total 0  
drwxr-xr-x 3 filip Administ 0 May 7 18:46 .  
drwxr-xr-x 4 filip Administ 0 May 7 18:46 ..  
drwxr-xr-x 1 filip Administ 0 May 7 18:46 .hg

c:\\dev\\projects\\graft\_demo  
λ hg graft  
abort: no revisions specified

c:\\dev\\projects\\graft\_demo  
λ hg branches

c:\\dev\\projects\\graft\_demo  
λ hg branch default  
marked working directory as branch default  
(branches are permanent and global, did you want a bookmark?)

c:\\dev\\projects\\graft\_demo  
λ hg branches

c:\\dev\\projects\\graft\_demo  
λ touch hello.py

c:\\dev\\projects\\graft\_demo  
λ hg branches

c:\\dev\\projects\\graft\_demo  
λ hg st  
? hello.py

c:\\dev\\projects\\graft\_demo  
λ hg add .  
adding hello.py

c:\\dev\\projects\\graft\_demo  
λ hg st  
A hello.py

c:\\dev\\projects\\graft\_demo  
λ hg branches

c:\\dev\\projects\\graft\_demo  
λ hg ci -m "Initial commit"

c:\\dev\\projects\\graft\_demo  
λ hg st

c:\\dev\\projects\\graft\_demo  
λ hg branches  
default 0:96756849ee0a

c:\\dev\\projects\\graft\_demo  
λ hg branch mybranch\_1  
marked working directory as branch mybranch\_1  
(branches are permanent and global, did you want a bookmark?)

c:\\dev\\projects\\graft\_demo  
λ hg branches  
default 0:96756849ee0a

c:\\dev\\projects\\graft\_demo  
λ hg st

c:\\dev\\projects\\graft\_demo  
λ vim hello.py

c:\\dev\\projects\\graft\_demo  
λ hg st  
M hello.py

c:\\dev\\projects\\graft\_demo  
λ hg ci -m "Dodano napis"

c:\\dev\\projects\\graft\_demo  
λ vim hello.py

c:\\dev\\projects\\graft\_demo  
λ hg st  
M hello.py

c:\\dev\\projects\\graft\_demo  
λ hg ci -m "Dodano napis pożegnania"

c:\\dev\\projects\\graft\_demo  
λ hg st

c:\\dev\\projects\\graft\_demo  
λ hg log -G -b .  
@ changeset: 2:9327770477c8  
\| branch: mybranch\_1  
\| tag: tip  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:47 2015 +0200  
\| summary: Dodano napis po┐egnania  
\|  
o changeset: 1:bf1a7a1c19e0  
\| branch: mybranch\_1  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:12 2015 +0200  
\| summary: Dodano napis  
\|

c:\\dev\\projects\\graft\_demo  
λ hg histedit  
hg: unknown command 'histedit'  
Mercurial Distributed SCM

basic commands:

add add the specified files on the next commit  
annotate show changeset information by line for each file  
clone make a copy of an existing repository  
commit commit the specified files or all outstanding changes  
diff diff repository (or selected files)  
export dump the header and diffs for one or more changesets  
forget forget the specified files on the next commit  
init create a new repository in the given directory  
log show revision history of entire repository or files  
merge merge working directory with another revision  
pull pull changes from the specified source  
push push changes to the specified destination  
remove remove the specified files on the next commit  
serve start stand-alone webserver  
status show changed files in the working directory  
summary summarize working directory state  
update update working directory (or switch revisions)

use "hg help" for the full list of commands or "hg -v" for details

c:\\dev\\projects\\graft\_demo  
λ ls -al  
total 3  
drwxr-xr-x 4 filip Administ 0 May 7 18:49 .  
drwxr-xr-x 4 filip Administ 0 May 7 18:46 ..  
drwxr-xr-x 1 filip Administ 4096 May 7 19:09 .hg  
-rw-r--r-- 1 filip Administ 52 May 7 19:09 hello.py

c:\\dev\\projects\\graft\_demo  
λ gvim .hg/hgrc

c:\\dev\\projects\\graft\_demo  
λ hg histedit  
abort: histedit requires exactly one ancestor revision

c:\\dev\\projects\\graft\_demo  
λ hg st

c:\\dev\\projects\\graft\_demo  
λ hg branch  
mybranch\_1

c:\\dev\\projects\\graft\_demo  
λ hg branches  
mybranch\_1 2:9327770477c8  
default 0:96756849ee0a (inactive)

c:\\dev\\projects\\graft\_demo  
λ hg log -b default -G  
o changeset: 0:96756849ee0a  
user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
date: Thu May 07 20:49:43 2015 +0200  
summary: Initial commit

c:\\dev\\projects\\graft\_demo  
λ hg log -b . -G  
@ changeset: 2:9327770477c8  
\| branch: mybranch\_1  
\| tag: tip  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:47 2015 +0200  
\| summary: Dodano napis po┐egnania  
\|  
o changeset: 1:bf1a7a1c19e0  
\| branch: mybranch\_1  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:12 2015 +0200  
\| summary: Dodano napis  
\|

c:\\dev\\projects\\graft\_demo  
λ hg branch mybranch\_2  
marked working directory as branch mybranch\_2  
(branches are permanent and global, did you want a bookmark?)

c:\\dev\\projects\\graft\_demo  
λ hg ci -m "Trash commit"

c:\\dev\\projects\\graft\_demo  
λ hg log -b .  
changeset: 3:b23eb7025048  
branch: mybranch\_2  
tag: tip  
user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
date: Thu May 07 21:21:00 2015 +0200  
summary: Trash commit

c:\\dev\\projects\\graft\_demo  
λ hg graft --help  
hg graft \[OPTION\]... \[-r\] REV...

copy changes from other branches onto the current branch

This command uses Mercurial's merge logic to copy individual changes from  
other branches without merging branches in the history graph. This is  
sometimes known as 'backporting' or 'cherry-picking'. By default, graft  
will copy user, date, and description from the source changesets.

Changesets that are ancestors of the current revision, that have already  
been grafted, or that are merges will be skipped.

If --log is specified, log messages will have a comment appended of the  
form:

(grafted from CHANGESETHASH)

If a graft merge results in conflicts, the graft process is interrupted so  
that the current merge can be manually resolved. Once all conflicts are  
addressed, the graft process can be continued with the -c/--continue  
option.

Note:  
The -c/--continue option does not reapply earlier options.

See "hg help revisions" and "hg help revsets" for more about specifying  
revisions.

Returns 0 on successful completion.

options:

-r --rev REV \[+\] revisions to graft  
-c --continue resume interrupted graft  
-e --edit invoke editor on commit messages  
--log append graft info to log message  
-D --currentdate record the current date as commit date  
-U --currentuser record the current user as committer  
-d --date DATE record the specified date as commit date  
-u --user USER record the specified user as committer  
-t --tool VALUE specify merge tool  
-n --dry-run do not perform actions, just print output

\[+\] marked option can be specified multiple times

use "hg -v help graft" to show more complete help and the global options

c:\\dev\\projects\\graft\_demo  
λ hg log -b mybranch\_1 -G  
o changeset: 2:9327770477c8  
\| branch: mybranch\_1  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:47 2015 +0200  
\| summary: Dodano napis po┐egnania  
\|  
o changeset: 1:bf1a7a1c19e0  
\| branch: mybranch\_1  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:12 2015 +0200  
\| summary: Dodano napis  
\|

c:\\dev\\projects\\graft\_demo  
λ hg graft -r 1  
skipping ancestor revision 1

c:\\dev\\projects\\graft\_demo  
λ hg graft -n -r 1  
skipping ancestor revision 1

c:\\dev\\projects\\graft\_demo  
λ hg graft -n -r 2  
skipping ancestor revision 2

c:\\dev\\projects\\graft\_demo  
λ hg st

c:\\dev\\projects\\graft\_demo  
λ hg branch  
mybranch\_2

c:\\dev\\projects\\graft\_demo  
λ hg log  
changeset: 3:b23eb7025048  
branch: mybranch\_2  
tag: tip  
user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
date: Thu May 07 21:21:00 2015 +0200  
summary: Trash commit

changeset: 2:9327770477c8  
branch: mybranch\_1  
user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
date: Thu May 07 21:09:47 2015 +0200  
summary: Dodano napis po┐egnania

changeset: 1:bf1a7a1c19e0  
branch: mybranch\_1  
user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
date: Thu May 07 21:09:12 2015 +0200  
summary: Dodano napis

changeset: 0:96756849ee0a  
user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
date: Thu May 07 20:49:43 2015 +0200  
summary: Initial commit

c:\\dev\\projects\\graft\_demo  
λ hg log -b .  
changeset: 3:b23eb7025048  
branch: mybranch\_2  
tag: tip  
user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
date: Thu May 07 21:21:00 2015 +0200  
summary: Trash commit

c:\\dev\\projects\\graft\_demo  
λ hg graft -n -r 2 mybranch\_1  
skipping ancestor revision 2

c:\\dev\\projects\\graft\_demo  
λ hg graft --help  
hg graft \[OPTION\]... \[-r\] REV...

copy changes from other branches onto the current branch

This command uses Mercurial's merge logic to copy individual changes from  
other branches without merging branches in the history graph. This is  
sometimes known as 'backporting' or 'cherry-picking'. By default, graft  
will copy user, date, and description from the source changesets.

Changesets that are ancestors of the current revision, that have already  
been grafted, or that are merges will be skipped.

If --log is specified, log messages will have a comment appended of the  
form:

(grafted from CHANGESETHASH)

If a graft merge results in conflicts, the graft process is interrupted so  
that the current merge can be manually resolved. Once all conflicts are  
addressed, the graft process can be continued with the -c/--continue  
option.

Note:  
The -c/--continue option does not reapply earlier options.

See "hg help revisions" and "hg help revsets" for more about specifying  
revisions.

Returns 0 on successful completion.

options:

-r --rev REV \[+\] revisions to graft  
-c --continue resume interrupted graft  
-e --edit invoke editor on commit messages  
--log append graft info to log message  
-D --currentdate record the current date as commit date  
-U --currentuser record the current user as committer  
-d --date DATE record the specified date as commit date  
-u --user USER record the specified user as committer  
-t --tool VALUE specify merge tool  
-n --dry-run do not perform actions, just print output

\[+\] marked option can be specified multiple times

use "hg -v help graft" to show more complete help and the global options

c:\\dev\\projects\\graft\_demo  
λ hg graft -n -r 2  
skipping ancestor revision 2

c:\\dev\\projects\\graft\_demo  
λ hg log -b mybranch\_1  
changeset: 2:9327770477c8  
branch: mybranch\_1  
user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
date: Thu May 07 21:09:47 2015 +0200  
summary: Dodano napis po┐egnania

changeset: 1:bf1a7a1c19e0  
branch: mybranch\_1  
user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
date: Thu May 07 21:09:12 2015 +0200  
summary: Dodano napis

c:\\dev\\projects\\graft\_demo  
λ hg log -b mybranch\_1 -G  
o changeset: 2:9327770477c8  
\| branch: mybranch\_1  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:47 2015 +0200  
\| summary: Dodano napis po┐egnania  
\|  
o changeset: 1:bf1a7a1c19e0  
\| branch: mybranch\_1  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:12 2015 +0200  
\| summary: Dodano napis  
\|

c:\\dev\\projects\\graft\_demo  
λ hg log -b mybranch\_2 -G  
@ changeset: 3:b23eb7025048  
\| branch: mybranch\_2  
\| tag: tip  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:21:00 2015 +0200  
\| summary: Trash commit  
\|

c:\\dev\\projects\\graft\_demo  
λ hg branches  
mybranch\_2 3:b23eb7025048  
mybranch\_1 2:9327770477c8 (inactive)  
default 0:96756849ee0a (inactive)

c:\\dev\\projects\\graft\_demo  
λ hg graft -r 2  
skipping ancestor revision 2

c:\\dev\\projects\\graft\_demo  
λ hg graft -r 2  
skipping ancestor revision 2

c:\\dev\\projects\\graft\_demo  
λ hg graft -r 1  
skipping ancestor revision 1

c:\\dev\\projects\\graft\_demo  
λ hg graft bf1a7a1c19e0  
skipping ancestor revision 1

c:\\dev\\projects\\graft\_demo  
λ hg up default  
1 files updated, 0 files merged, 0 files removed, 0 files unresolved

c:\\dev\\projects\\graft\_demo  
λ hg st

c:\\dev\\projects\\graft\_demo  
λ hg up mybranch\_2  
1 files updated, 0 files merged, 0 files removed, 0 files unresolved

c:\\dev\\projects\\graft\_demo  
λ hg ci --close-brach  
hg commit: option --close-brach not recognized  
hg commit \[OPTION\]... \[FILE\]...

commit the specified files or all outstanding changes

options:

-A --addremove mark new/missing files as added/removed before  
committing  
--close-branch mark a branch as closed, hiding it from the branch  
list  
--amend amend the parent of the working dir  
-s --secret use the secret phase for committing  
-e --edit invoke editor on commit messages  
-I --include PATTERN \[+\] include names matching the given patterns  
-X --exclude PATTERN \[+\] exclude names matching the given patterns  
-m --message TEXT use text as commit message  
-l --logfile FILE read commit message from file  
-d --date DATE record the specified date as commit date  
-u --user USER record the specified user as committer  
-S --subrepos recurse into subrepositories

\[+\] marked option can be specified multiple times

use "hg help commit" to show the full help text

c:\\dev\\projects\\graft\_demo  
λ hg ci --close-branch  
System nie może odnaleźć określonej ścieżki.  
abort: edit failed: Notepad2.exe exited with status 1

c:\\dev\\projects\\graft\_demo  
λ vim .hg/hgrc

c:\\dev\\projects\\graft\_demo  
λ hg ci --close-branch  
System nie może odnaleźć określonej ścieżki.  
abort: edit failed: Notepad2.exe exited with status 1

c:\\dev\\projects\\graft\_demo  
λ vim .hg/hgrc

c:\\dev\\projects\\graft\_demo  
λ hg ci --close-branch

c:\\dev\\projects\\graft\_demo  
λ hg branches  
mybranch\_1 2:9327770477c8 (inactive)  
default 0:96756849ee0a (inactive)

c:\\dev\\projects\\graft\_demo  
λ hg up default  
1 files updated, 0 files merged, 0 files removed, 0 files unresolved

c:\\dev\\projects\\graft\_demo  
λ hg branch mybranch\_2  
abort: a branch of the same name already exists  
(use 'hg update' to switch to it)

c:\\dev\\projects\\graft\_demo  
λ hg branch mybranch\_correct  
marked working directory as branch mybranch\_correct  
(branches are permanent and global, did you want a bookmark?)

c:\\dev\\projects\\graft\_demo  
λ hg branches  
mybranch\_1 2:9327770477c8 (inactive)  
default 0:96756849ee0a (inactive)

c:\\dev\\projects\\graft\_demo  
λ ls  
hello.py

c:\\dev\\projects\\graft\_demo  
λ vim hello.py

c:\\dev\\projects\\graft\_demo  
λ hg ci -m "Temporary commit"

c:\\dev\\projects\\graft\_demo  
λ hg log -b . -G  
@ changeset: 5:805524829a19  
\| branch: mybranch\_correct  
\| tag: tip  
\| parent: 0:96756849ee0a  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:34:13 2015 +0200  
\| summary: Temporary commit  
\|

c:\\dev\\projects\\graft\_demo  
λ hg log -b mybranch\_1 -G  
o changeset: 2:9327770477c8  
\| branch: mybranch\_1  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:47 2015 +0200  
\| summary: Dodano napis po┐egnania  
\|  
o changeset: 1:bf1a7a1c19e0  
\| branch: mybranch\_1  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:12 2015 +0200  
\| summary: Dodano napis  
\|

c:\\dev\\projects\\graft\_demo  
λ hg graft -r 1  
grafting revision 1

c:\\dev\\projects\\graft\_demo  
λ hg graft -r 2  
grafting revision 2

c:\\dev\\projects\\graft\_demo  
λ hg st

c:\\dev\\projects\\graft\_demo  
λ hg log -b . -G  
@ changeset: 7:f67109e8488d  
\| branch: mybranch\_correct  
\| tag: tip  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:47 2015 +0200  
\| summary: Dodano napis po┐egnania  
\|  
o changeset: 6:7bb5a587d6f8  
\| branch: mybranch\_correct  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:12 2015 +0200  
\| summary: Dodano napis  
\|  
o changeset: 5:805524829a19  
\| branch: mybranch\_correct  
\| parent: 0:96756849ee0a  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:34:13 2015 +0200  
\| summary: Temporary commit  
\|

c:\\dev\\projects\\graft\_demo  
λ hg histedit  
abort: histedit requires exactly one ancestor revision

c:\\dev\\projects\\graft\_demo  
λ hg histedit --outgoing  
comparing with default-push  
abort: repository default-push not found!

c:\\dev\\projects\\graft\_demo  
λ hg st

c:\\dev\\projects\\graft\_demo  
λ hg histedit  
abort: histedit requires exactly one ancestor revision

c:\\dev\\projects\\graft\_demo  
λ hg up -r 5  
1 files updated, 0 files merged, 0 files removed, 0 files unresolved

c:\\dev\\projects\\graft\_demo  
λ hg histedit  
abort: histedit requires exactly one ancestor revision

c:\\dev\\projects\\graft\_demo  
λ hg log -G -b .  
o changeset: 7:f67109e8488d  
\| branch: mybranch\_correct  
\| tag: tip  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:47 2015 +0200  
\| summary: Dodano napis po┐egnania  
\|  
o changeset: 6:7bb5a587d6f8  
\| branch: mybranch\_correct  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:12 2015 +0200  
\| summary: Dodano napis  
\|  
@ changeset: 5:805524829a19  
\| branch: mybranch\_correct  
\| parent: 0:96756849ee0a  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:34:13 2015 +0200  
\| summary: Temporary commit  
\|

c:\\dev\\projects\\graft\_demo  
λ hg up -r 7  
1 files updated, 0 files merged, 0 files removed, 0 files unresolved

c:\\dev\\projects\\graft\_demo  
λ hg log -G -b .  
@ changeset: 7:f67109e8488d  
\| branch: mybranch\_correct  
\| tag: tip  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:47 2015 +0200  
\| summary: Dodano napis po┐egnania  
\|  
o changeset: 6:7bb5a587d6f8  
\| branch: mybranch\_correct  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:12 2015 +0200  
\| summary: Dodano napis  
\|  
o changeset: 5:805524829a19  
\| branch: mybranch\_correct  
\| parent: 0:96756849ee0a  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:34:13 2015 +0200  
\| summary: Temporary commit  
\|

c:\\dev\\projects\\graft\_demo  
λ hg histedit  
abort: histedit requires exactly one ancestor revision

c:\\dev\\projects\\graft\_demo  
λ hg st

c:\\dev\\projects\\graft\_demo  
λ hg histedit --help  
hg histedit ANCESTOR \| --outgoing \[URL\]

interactively edit changeset history

This command edits changesets between ANCESTOR and the parent of the  
working directory.

With --outgoing, this edits changesets not found in the destination  
repository. If URL of the destination is omitted, the 'default-push' (or  
'default') path will be used.

For safety, this command is aborted, also if there are ambiguous outgoing  
revisions which may confuse users: for example, there are multiple  
branches containing outgoing revisions.

Use "min(outgoing() and ::.)" or similar revset specification instead of  
--outgoing to specify edit target revision exactly in such ambiguous  
situation. See "hg help revsets" for detail about selecting revisions.

Returns 0 on success, 1 if user intervention is required (not only for  
intentional "edit" command, but also for resolving unexpected conflicts).

use "hg help -e histedit" to show help for the histedit extension

options:

--commands VALUE Read history edits from the specified file.  
-c --continue continue an edit already in progress  
-k --keep don't strip old nodes after edit is complete  
--abort abort an edit in progress  
-o --outgoing changesets not found in destination  
-f --force force outgoing even for unrelated repositories  
-r --rev VALUE \[+\] first revision to be edited

\[+\] marked option can be specified multiple times

use "hg -v help histedit" to show the global options

c:\\dev\\projects\\graft\_demo  
λ hg histedit --outgoing  
comparing with default-push  
abort: repository default-push not found!

c:\\dev\\projects\\graft\_demo  
λ hg out  
comparing with default-push  
abort: repository default-push not found!

c:\\dev\\projects\\graft\_demo  
λ vim .hg\\hgrc

c:\\dev\\projects\\graft\_demo  
λ hg histedit  
abort: histedit requires exactly one ancestor revision

c:\\dev\\projects\\graft\_demo  
λ hg log -G -b .  
@ changeset: 7:f67109e8488d  
\| branch: mybranch\_correct  
\| tag: tip  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:47 2015 +0200  
\| summary: Dodano napis po┐egnania  
\|  
o changeset: 6:7bb5a587d6f8  
\| branch: mybranch\_correct  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:12 2015 +0200  
\| summary: Dodano napis  
\|  
o changeset: 5:805524829a19  
\| branch: mybranch\_correct  
\| parent: 0:96756849ee0a  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:34:13 2015 +0200  
\| summary: Temporary commit  
\|

c:\\dev\\projects\\graft\_demo  
λ

 

c:\\dev\\projects\\graft\_demo  
λ hg diff -r .:default  
diff -r f67109e8488d -r 96756849ee0a hello.py  
--- a/hello.py Thu May 07 21:09:47 2015 +0200  
+++ b/hello.py Thu May 07 20:49:43 2015 +0200  
@@ -1,2 +0,0 @@  
-print "Witaj ┼Ťwiecie!"  
-print "┼╗egnaj ┼Ťwiecie!"

c:\\dev\\projects\\graft\_demo  
λ

c:\\dev\\projects\\graft\_demo  
λ hg diff -r .:default  
diff -r f67109e8488d -r 96756849ee0a hello.py  
--- a/hello.py Thu May 07 21:09:47 2015 +0200  
+++ b/hello.py Thu May 07 20:49:43 2015 +0200  
@@ -1,2 +0,0 @@  
-print "Witaj ┼Ťwiecie!"  
-print "┼╗egnaj ┼Ťwiecie!"

c:\\dev\\projects\\graft\_demo  
λ hg histedit  
abort: histedit requires exactly one ancestor revision

c:\\dev\\projects\\graft\_demo  
λ hg histedit -r 7  
0 files updated, 0 files merged, 0 files removed, 0 files unresolved

PRZENOSIMY ŚMIECIOWEGO COMMITA NA KONIEC.  
c:\\dev\\projects\\graft\_demo  
λ hg histedit -r 5  
1 files updated, 0 files merged, 0 files removed, 0 files unresolved  
0 files updated, 0 files merged, 0 files removed, 0 files unresolved  
0 files updated, 0 files merged, 0 files removed, 0 files unresolved  
0 files updated, 0 files merged, 0 files removed, 0 files unresolved  
saved backup bundle to c:\\dev\\projects\\graft\_demo\\.hg\\strip-backup/805524829a19-backup.hg

c:\\dev\\projects\\graft\_demo  
λ

 

c:\\dev\\projects\\graft\_demo  
λ hg branches  
mybranch\_correct 7:e362b38845e9  
mybranch\_1 2:9327770477c8 (inactive)  
default 0:96756849ee0a (inactive)

c:\\dev\\projects\\graft\_demo  
λ hg up mybranch\_correct  
0 files updated, 0 files merged, 0 files removed, 0 files unresolved

c:\\dev\\projects\\graft\_demo  
λ hg st

c:\\dev\\projects\\graft\_demo  
λ hg log -b . -G  
@ changeset: 7:e362b38845e9  
\| branch: mybranch\_correct  
\| tag: tip  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:34:13 2015 +0200  
\| summary: Temporary commit  
\|  
o changeset: 6:4a26832ba44d  
\| branch: mybranch\_correct  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:47 2015 +0200  
\| summary: Dodano napis po┐egnania  
\|  
o changeset: 5:aacc17df9445  
\| branch: mybranch\_correct  
\| parent: 0:96756849ee0a  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:12 2015 +0200  
\| summary: Dodano napis  
\|

c:\\dev\\projects\\graft\_demo  
λ hg strip -r 7  
0 files updated, 0 files merged, 0 files removed, 0 files unresolved  
saved backup bundle to c:\\dev\\projects\\graft\_demo\\.hg\\strip-backup/e362b38845e9-backup.hg

c:\\dev\\projects\\graft\_demo  
λ hg st

c:\\dev\\projects\\graft\_demo  
λ hg strip -r 7  
abort: unknown revision '7'!

c:\\dev\\projects\\graft\_demo  
λ hg log -b . -G  
@ changeset: 6:4a26832ba44d  
\| branch: mybranch\_correct  
\| tag: tip  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:47 2015 +0200  
\| summary: Dodano napis po┐egnania  
\|  
o changeset: 5:aacc17df9445  
\| branch: mybranch\_correct  
\| parent: 0:96756849ee0a  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:12 2015 +0200  
\| summary: Dodano napis  
\|

c:\\dev\\projects\\graft\_demo  
λ

 

 

c:\\dev\\projects\\graft\_demo  
λ hg st

c:\\dev\\projects\\graft\_demo  
λ hg strip -r 7  
abort: unknown revision '7'!

c:\\dev\\projects\\graft\_demo  
λ hg log -b . -G  
@ changeset: 6:4a26832ba44d  
\| branch: mybranch\_correct  
\| tag: tip  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:47 2015 +0200  
\| summary: Dodano napis po┐egnania  
\|  
o changeset: 5:aacc17df9445  
\| branch: mybranch\_correct  
\| parent: 0:96756849ee0a  
\| user: Filip Gorczynski \<filip.gorczynski\@gmail.com\>  
\| date: Thu May 07 21:09:12 2015 +0200  
\| summary: Dodano napis  
\|

c:\\dev\\projects\\graft\_demo  
λ notepad .hg/hgrc

c:\\dev\\projects\\graft\_demo  
λ
