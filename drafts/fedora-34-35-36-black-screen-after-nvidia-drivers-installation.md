Title: Fedora 34/35/36 black screen after NVIDIA drivers installation
Date: 2022-06-06 08:49
Modified: 2022-06-06 08:49
Category: Tech
Tags: #tech, #fedora, #nvidia, #drivers, #geforce, #rtx
Slug: fedora-34-35-36-black-screen-after-nvidia-drivers-installation
Author: filipgorczynski
Status: draft
Cover: https://blog.filipgorczynski.me/images/feature/christian-wiediger-TErYPw4o1KM.jpg
meta_url: https://blog.filipgorczynski.me/2022/06/fedora-34-35-36-black-screen-after-nvidia-drivers-installation
Summary: Nvidia drivers are known from many issues on linux systems. Or maybe on mine only? Various drivers sources like official Nvidia releases and Fedora repositories were not helpful at all.

I've used official Nvidia drivers releases from their [website](https://www.nvidia.com/Download/index.aspx) for some time and it worked almost perfectly. I had some issues and when kernel updates/upgrades reinstall was needed. It requires me to jump into virtual console prompt (Thanks Ctrl + Alt + Fn) to install drivers again. But it worked after that like a charm. Few days ago on Reddit someone told me to never do that again (installing Nvidia drivers from official Nvidia site) :).

Unfortunately after latest kernel changes it started to be more problematic. It started with kernel updates on Fedora 34 so my first thought was to upgrade Fedora to 35 and then to 36. But after all installing latest Nvidia drivers - no matter from - gives me black screen. I mean not the totally  black because mouse pointer was fine. It's really hard to work with mouse pointer only. The serious problem was actually switching to virtual console prompt, as my system switches to power save mode. The solution was to revert system to use nouveau drivers. I'm really unsatisfies with nouveau but at least everything is displayed on the screen (not only mouse pointer).

But how to achieve this without terminal access? Sadly the only way I could done that was with Fedora 36 USB stick (of course I needed to created it somewhere else :)).

1. Boot Fedora from USB Stick
2. Choose "Try a Live Fedora"
3. Wait for Fedora fully loads
4. Go to "Files" & "Other Locations"
5. Choose partition, where your original Fedora is installed
6. Go to `/etc/X11/xorg.conf.d/` and check if any files related with Nvidia is present there - delete those files
7. Go to `/usr/share/X11/xorg.conf.d/` and check if any files related with Nvidia is present there - delete those files
8. Go to `/etc/modprobe.d/` and check if any files related with Nvidia or blacklisted Nouveau is present there - delete those files
9. Reboot withou USB stick

<small class="unsplash-reference">
    Photo by <a href="https://unsplash.com/@christianw?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Christian Wiediger</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>  
</small>
