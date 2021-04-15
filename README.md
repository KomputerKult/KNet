# KomputerNet [![Build Status](https://travis-ci.org/HelloKomputerNet/KomputerNet.svg?branch=py3)](https://travis-ci.org/HelloKomputerNet/KomputerNet) [![Documentation](https://img.shields.io/badge/docs-faq-brightgreen.svg)](https://komputernet.io/docs/faq/) [![Help](https://img.shields.io/badge/keep_this_project_alive-donate-yellow.svg)](https://komputernet.io/docs/help_komputernet/donate/) ![tests](https://github.com/HelloKomputerNet/KomputerNet/workflows/tests/badge.svg) [![Docker Pulls](https://img.shields.io/docker/pulls/nofish/komputernet)](https://hub.docker.com/r/nofish/komputernet)

Decentralized websites using Bitcoin crypto and the BitTorrent network - https://komputernet.io / [onion](http://komputernet34m3r5ngdu54uj57dcafpgdjhxsgq5kla5con4qvcmfzpvhad.onion)


## Why?

* We believe in open, free, and uncensored network and communication.
* No single point of failure: Site remains online so long as at least 1 peer is
  serving it.
* No hosting costs: Sites are served by visitors.
* Impossible to shut down: It's nowhere because it's everywhere.
* Fast and works offline: You can access the site even if Internet is
  unavailable.


## Features
 * Real-time updated sites
 * Namecoin .bit domains support
 * Easy to setup: unpack & run
 * Clone websites in one click
 * Password-less [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki)
   based authorization: Your account is protected by the same cryptography as your Bitcoin wallet
 * Built-in SQL server with P2P data synchronization: Allows easier site development and faster page load times
 * Anonymity: Full Tor network support with .onion hidden services instead of IPv4 addresses
 * TLS encrypted connections
 * Automatic uPnP port opening
 * Plugin for multiuser (openproxy) support
 * Works with any browser/OS


## How does it work?

* After starting `komputernet.py` you will be able to visit komputernet sites using
  `http://127.0.0.1:43110/{komputernet_address}` (eg.
  `http://127.0.0.1:43110/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D`).
* When you visit a new komputernet site, it tries to find peers using the BitTorrent
  network so it can download the site files (html, css, js...) from them.
* Each visited site is also served by you.
* Every site contains a `content.json` file which holds all other files in a sha512 hash
  and a signature generated using the site's private key.
* If the site owner (who has the private key for the site address) modifies the
  site, then he/she signs the new `content.json` and publishes it to the peers.
  Afterwards, the peers verify the `content.json` integrity (using the
  signature), they download the modified files and publish the new content to
  other peers.

####  [Slideshow about KomputerNet cryptography, site updates, multi-user sites »](https://docs.google.com/presentation/d/1_2qK1IuOKJ51pgBvllZ9Yu7Au2l551t3XBgyTSvilew/pub?start=false&loop=false&delayms=3000)
####  [Frequently asked questions »](https://komputernet.io/docs/faq/)

####  [KomputerNet Developer Documentation »](https://komputernet.io/docs/site_development/getting_started/)


## Screenshots

![Screenshot](https://i.imgur.com/H60OAHY.png)
![ZeroTalk](https://komputernet.io/docs/img/zerotalk.png)

#### [More screenshots in KomputerNet docs »](https://komputernet.io/docs/using_komputernet/sample_sites/)


## How to join

### Windows

 - Download [KomputerNet-py3-win64.zip](https://github.com/HelloKomputerNet/KomputerNet-win/archive/dist-win64/KomputerNet-py3-win64.zip) (18MB)
 - Unpack anywhere
 - Run `KomputerNet.exe`
 
### macOS

 - Download [KomputerNet-dist-mac.zip](https://github.com/HelloKomputerNet/KomputerNet-dist/archive/mac/KomputerNet-dist-mac.zip) (13.2MB)
 - Unpack anywhere
 - Run `KomputerNet.app`
 
### Linux (x86-64bit)
 - `wget https://github.com/HelloKomputerNet/KomputerNet-linux/archive/dist-linux64/KomputerNet-py3-linux64.tar.gz`
 - `tar xvpfz KomputerNet-py3-linux64.tar.gz`
 - `cd KomputerNet-linux-dist-linux64/`
 - Start with: `./KomputerNet.sh`
 - Open the ZeroHello landing page in your browser by navigating to: http://127.0.0.1:43110/
 
 __Tip:__ Start with `./KomputerNet.sh --ui_ip '*' --ui_restrict your.ip.address` to allow remote connections on the web interface.
 
 ### Android (arm, arm64, x86)
 - minimum Android version supported 16 (JellyBean)
 - [<img src="https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png" 
      alt="Download from Google Play" 
      height="80">](https://play.google.com/store/apps/details?id=in.canews.komputernetmobile)
 - APK download: https://github.com/canewsin/komputernet_mobile/releases
 - XDA Labs: https://labs.xda-developers.com/store/app/in.canews.komputernet
 
#### Docker
There is an official image, built from source at: https://hub.docker.com/r/nofish/komputernet/

### Install from source

 - `wget https://github.com/HelloKomputerNet/KomputerNet/archive/py3/KomputerNet-py3.tar.gz`
 - `tar xvpfz KomputerNet-py3.tar.gz`
 - `cd KomputerNet-py3`
 - `sudo apt-get update`
 - `sudo apt-get install python3-pip`
 - `sudo python3 -m pip install -r requirements.txt`
 - Start with: `python3 komputernet.py`
 - Open the ZeroHello landing page in your browser by navigating to: http://127.0.0.1:43110/

## Current limitations

* ~~No torrent-like file splitting for big file support~~ (big file support added)
* ~~No more anonymous than Bittorrent~~ (built-in full Tor support added)
* File transactions are not compressed ~~or encrypted yet~~ (TLS encryption added)
* No private sites


## How can I create a KomputerNet site?

 * Click on **⋮** > **"Create new, empty site"** menu item on the site [ZeroHello](http://127.0.0.1:43110/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D).
 * You will be **redirected** to a completely new site that is only modifiable by you!
 * You can find and modify your site's content in **data/[yoursiteaddress]** directory
 * After the modifications open your site, drag the topright "0" button to left, then press **sign** and **publish** buttons on the bottom

Next steps: [KomputerNet Developer Documentation](https://komputernet.io/docs/site_development/getting_started/)

## Help keep this project alive

- Bitcoin: 1QDhxQ6PraUZa21ET5fYUCPgdrwBomnFgX
- Paypal: https://komputernet.io/docs/help_komputernet/donate/

### Sponsors

* Better macOS/Safari compatibility made possible by [BrowserStack.com](https://www.browserstack.com)

#### Thank you!

* More info, help, changelog, komputernet sites: https://www.reddit.com/r/komputernet/
* Come, chat with us: [#komputernet @ FreeNode](https://kiwiirc.com/client/irc.freenode.net/komputernet) or on [gitter](https://gitter.im/HelloKomputerNet/KomputerNet)
* Email: hello@komputernet.io (PGP: [960F FF2D 6C14 5AA6 13E8 491B 5B63 BAE6 CB96 13AE](https://komputernet.io/files/tamas@komputernet.io_pub.asc))
