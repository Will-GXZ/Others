Do you bother with the inconvenience of the location of direction keys of your 
Macbook? I do, so I figured out some way to modify the key sets, now I can use 
"Caps Lock + W/S/A/D" as "up/down/left/right", and make "Caps Lock + Tab" act as
 "Caps Lock", also I use "Caps Lock + F" as delete forward key set, and I'm willing 
 to share this approach with you guys.


Here are the approach.
********************************************************************************

First we are gonna need 2 softwares, they are SEIL and KARABINER, they are both
open source program and easily accessible on the Internet, let's appreciate the 
authors first.

Then we can use SEIL to change the key match of CapsLock key, here we'll change 
the key code of CapsLock from 51 to 63 which is the key code of "FN".

Then we use KARABINER to implement our key sets matching modification. 
1.   Open Karabiner, select "Misc & Uninstall" on the higher right most conner, 
     then clik "Open private.xml" on the middle of the window.

2.   Open private.xml in your text editor. 
    
3.   Download my will_private.xml I uploaded, open it, copy the content of my 
     file, paste them in your private.xml, save.

4.   Back to Karabiner, click "Change Key" on the higher left most conner, then 
     hit "Reload XML". Then you will see a new line appeared on the top of the 
     list below, select this item.

5.   Restart your Macbook, then you are all set.

********************************************************************************

If you have any questions, feel free to contact me, you can just fork this repo 
and pull request with your comments. 

Thanks to the authors of Seil and Karabiner, we can change the key sets of Mac 
now, really appreciated, again.
 