# ANNOUNCEMENT

This project is *DEAD*


# Wigle Extract

# What is it?

Wigle Extract is a program that can interact with the generated CSV files from Wigle <br>
It extracts insecure and vulnerable Wi-Fi Access Points based on my personal Wi-Fi hacking experience

(Please Note: There is no 100% accuracy guarantee!)


# Releases:

You should find all releases on GitHub's release page. If there is no file, then you find it on [Google Drive](https://drive.google.com/drive/folders/1z2rp4DSN2o7kJwugVZBhZjjIWPXkvV85?usp=sharing)
<br> The files mostly exceed the maximum allowed size of 25 Megabytes. So I need to put them on Google Drive


# Platforms:

- Windows
- Linux
- MacOS
- Any System with a Graphical Environment, Display Server and Python / Qt Support

# Installation / Building
<br>You don't need to build it by yourself, you can just use the pre-compiled releases if you want.
<br> (The following instructions are for Ubuntu. If you are running on another System, you need to change some commands)

- Install a version of Python 3.X and git
- Install Pyside6 and Pyinstaller : pip install PySide6 pyinstaller
- Clone the project: git clone https://github.com/EchterAlsFake/wigle-extract
- Go into Project Folder: cd wigle-extract
- Build with: pyinstaller -F Wigle_Extract.py
- Output will be in a directory called "dist"
<br> Info I built everything with Arch Linux with Python 3.11.3

# Changelog:

Note: Beta releases are not mentioned here. Search in the commits from the past 8 months to get additional information.

## 1.0 

- Changed Application Development to PySide6
- Removed CLI
- Removed German Language Support
- Changed License to LGPLv3
- Application is resizeable now
- Changed the overall UI look
- Improved Performance 
- Refactored code

# License:

LGPLv3

You should see a LICENSE file in the repository and in every release on Google Drive.

Just in case there is no LICENSE file, you can see it [here](https://www.gnu.org/licenses/lgpl-3.0.en.html)

# Support

You can contact me at EchterAlsFake@proton.me or on Discord: echteralsfake (Old Tag System: EchterAlsFake#7164)
In case you encounter any issues, you can create an Issue tab on GitHub.  PRs are welcome :) 
