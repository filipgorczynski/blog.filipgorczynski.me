Title: VirtualBox i Bridged Network w Kali Linux
Date: 2015-05-07 22:16
Author: filipgorczynski
Category: Programowanie
Slug: virtualbox-i-bridged-network-w-kali-linux
Status: draft

[![kali\_logo](https://filipgorczynski.files.wordpress.com/2015/05/kali_logo.png){.alignleft .wp-image-1048 .size-full width="128" height="128"}](https://filipgorczynski.files.wordpress.com/2015/05/kali_logo.png)

Kali LInux Bridged Network problem  
The solution was this

vi /etc/NetworkManager/NetworkManager.conf  
Change false to true

And then

service network-manager restart
