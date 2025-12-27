Title: Parental control in Windows is completely broken, like the entire Windows system
Date: 2025-12-27 15:25:55
Modified: 2025-12-27 15:25:55
Category: Tech
Tags: #tech, #windows, #linux, #hardware
Slug: parental-control-in-windows-is-completely-broken-like-the-entire-windows-system
Author: filipgorczynski
Status: published
Cover: https://blog.filipgorczynski.me/images/feature/igor-omilaev-xvHl_X9Ojrg.jpg
meta_url: https://blog.filipgorczynski.me/2025/12/parental-control-in-windows-is-completely-broken-like-the-entire-windows-system
Summary: We've decided to buy a computer for our kid. Because of the main purpose - gaming - I've ended up choosing Windows 11, as it was the latest OS version.

We've decided to buy a computer for our kid. Because of the main purpose - gaming - I've ended up choosing Windows 11, as it was the latest OS version.
I've never thought we get to place where Linux installation is easier that Windows.

One problem I've already mentioned few posts ago - creating installable USB media with Windows is a nightmare - requires downloading some tool from Microsoft website, which then downloads the OS image and creates the media. No simple ISO download. So, you need to have Windows to create Windows USB device.

Installation process itself was "smooth" until at some point Windows required internet connection to proceed. No offline installation possible. Of course nowadays not all computers have DVD drive, so no option to insert installation media and continue offline or just to install wifi drivers. I've finally solved the problem by connecting to ethernet, but still - ridiculous. Also, hardware provider decided to include DVD with drivers but for wrong motherboard chipset.

Installation continuted, but stuck on the screen where (probably) some updates were pulled. No progress for ages. No information if it is still working, how long it take, nothing. On 1GB ethernet connection it took something about 30 minutes and I've accidentally discovered it was making some updates behind my back as it showed next step at some point. During that time I've spend some time searching information about possible issues and after returning to PC (to maybe do some restart and retry installation) I figured out it finished.

I've created administrator account for myself, just to be able to create Basic user account for kid. Setting up parental control has been quite a challenge. I've decided to create user account for family member. Windows wanted me to create a new Microsoft email account, with passwords and so on. I've failed. So I removed partially created account and decided to create Basic User account. Easy. I was able to login to that account without problems. However, still neeeded to create email account (for kid).

As administrator I've installed most of the drivers and software for the hardware. Also, installed the proper wifi drivers from the Internet. Of course, not from the original provider, because I've hit "too many downloads" error on their website. Doesn't matter if I was there once and clicked download once.

CPU cooler has a temperature sensor and display, but drivers require installation of .NET framework and passing UAC permission with my (Administrator) account. And yeah, running this software on system start require Administrator privileges too. No easy/simple way to bypass UAC for that software. So, kid can't run it without my permission. And there is no simple wayt o "mark" that software as trusted to be run without UAC prompt.

Trying to start anything on the system by starting to write program name and press Enter? Nope, not that easy without knowing the complete name. Windows will search Internet for that program instead of starting it if you made a typo. With Edge, which I decided not to use.

So, finally I had to make my kid Administrator too. But at least I was able to run game on this "OS" (of course I still need to enter password for Steam every time kid want to play as "Remember me" option doesn't work for some reason).
