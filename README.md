# reMiSTer
Use your computers keyboard on your MiSTer via the network

This is a program that lets you remotly control your MiSTer device as if you had connected your computers keyboard to your MiSTer. At least thats the goal. Currently its not feature complete more on that below.

## Installation

* Download reMiSTer from the releaes page, [Direct Link](https://github.com/sigboe/reMiSTer/releases/latest/download/remister)  and put it into `/media/fat/linux/` which is the `linux` folder on your SD card.
* Download pocomane's MiSTer_Batch_Control from his repo [Direct Link](https://github.com/pocomane/MiSTero_Batch_Control/releases/latest/download/mbc) and put it into `/media/fat/linux/` which again is the `linux` folder on your SD card.
* If you are on Windows and are using Putty you might need to change a setting to allow F1 through F4 to work. In PuTTy Configuration, under Terminal > Keyboard select Xtrem R6.

## Usage
SSH into your mister and type `remister`. Ctrl+D to close the program (just like you can log out of SSH or a close a shell prompt with Ctrl+D)

When the window with SSH is in focus on your computer (as if you were typing into it), the keys should be forwarded to the MiSTer as if it was a keyboard connected to the MiSTer.

## Known issues

Currently most keys work. Letters, numbers, and even symbols should pass through, as well as a list of keys that have hardcoded support. If things not listed here are not working, then feel free to open an issue and tell me about it. I believe some of these known issues may be fixable without a complete rewrite. 

* Esc: You need to press the Esc key twice for it to be registred. 
* Key combinations don't work, but if the key combination results in a symbol or a letter in your computer then it is possible that it will work. The symbol will be sent and remister will try to issue the symbol to MiSTer
* Alt, AltGr, Win, Shift, Ctrl, don't work but see the previous line regarding some things that may work.

## Other projects

* MiSTress https://github.com/sigboe/MiSTress

I have a couple of other projects I have not published yet, including a MiSTer driver installer, and a backup system for Linux settings in MiSTer.

## Todo

* Fix some of the know issues, and fix any keys that users request if possible
* Complete rewrite to increase compatibility and remove dependency on mbc
* Possibly write a client program you can run on your computer, instead of ssh to get full access to the keyboard

## Compiling

Need to use PyInstall to compile it to a single binary and include the dependencies. But to make a usable binary you also need an older glibc, so therefor the easiest way to compile it is to make a chroot on a raspberry pi (which is ARM) with an older raspbian. Included is notes for making the chroot, inclduing a know good version. I don't know the legality of sharing my chroot, if anyone knows I might just upload my chroot. Thankfully its easier to install everything you need for reMiSTer inside the chroot than it was to install everything needed for MiSTress (my other program for MiSTer). Yes but included are files how to make the chroot and enter it. Then copy the source into the chroot, and install dependencies, should only need to install pyinstaller, subprocess for python and curses for python using pip3 (which has to be manually installed) 

When you have your chroot setup, and the source copied into the chroot it is as simple as running

```
pyinstaller --onefile --clean remister.py
```

The soruce file will be in a folder called dist and be named remister. 


## Credits

* Pocomane for his MiSTer_Batch_Control https://github.com/pocomane/MiSTer_Batch_Control Because when I tried to make virtual evdev keyboards my self it was not recognized by MiSTer
* Mellified (github) for telling me about MiSTer_Batch_Control
* Sega Colection (discord) for the name reMiSTer
