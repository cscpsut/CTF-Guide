# CTF Guide

**CTF deployment guide for future generations** :space_invader:<br/><br/>
 

<img align="right" src="https://user-images.githubusercontent.com/35840617/171266140-a7f88018-c359-4ad1-955d-f96d54bfbdc1.png" width="300"><br/>


## Overview

The cyber security club PSUT has two virtual private servers (Ubuntu Server LTS) from [Contabo](https://contabo.com). 
1. `CTFd VPS` is dedicated to hosting the CTFd platform on [cscpsut.com](https://cscpsut.com).
2. `Challenges VPS` is dedicated to hosting **remote** CTF challenges (mostly web, pwn and probably crypto too).

The club currently adopts the use of [CTFd](https://github.com/CTFd/CTFd) which is an open-source CTF platform that's easy to setup and use. The domain [cscpsut.com](https://cscpsut.com) is being managed using [Cloudflare](https://www.cloudflare.com/) due to the useful features cloudflare offers (mostly HTTPS implementation and DDoS protection). 

This repository aims to offer a step-by-step guide on how to deploy a successful CTF. Bear in mind that this guide was written according to the past experiences of previous Infrastructure Adminstration Officers in the club, you're free to follow them as is or add your own spice to the mix as you see fit!

- [SSH to the VPS (with sublime text)](https://github.com/cscpsut/CTF-Guide#SSH)
- [Cloudflare for Domain Management](https://github.com/cscpsut/CTF-Guide#Cloudflare)
- [How to setup CTFd](https://github.com/cscpsut/CTF-Guide#Cloudflare)
- 
- The full picture with detailed diagrams (Amer Jarrar's Architecture :D)

