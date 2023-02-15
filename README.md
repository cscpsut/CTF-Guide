# CTF Guide

**CTF deployment guide for future generations** :space_invader:

<img align="right" src="https://user-images.githubusercontent.com/35840617/171266140-a7f88018-c359-4ad1-955d-f96d54bfbdc1.png" width="300"><br/>


## Overview

The cyber security club PSUT has 2 virtual private servers (Ubuntu Server LTS) from [Contabo](https://contabo.com). 
- `CTF platform` VPS hosts the CTFd platform on [cscpsut.com](https://cscpsut.com).
- `Challenges` VPS is for hosting **remote** CTF challenges (web, pwn and crypto).

The club currently adopts the use of [CTFd](https://github.com/CTFd/CTFd) which is an open-source CTF platform that's easy to setup and use. The domain [cscpsut.com](https://cscpsut.com) is being managed using [Cloudflare](https://www.cloudflare.com/) due to the useful features cloudflare offers (mostly HTTPS implementation and DDoS protection). As for remote challenges we currently **_still_** depend on single Docker Containers which run on the `Challenges VPS` and use a couple of handy bash scripts to automate the deployment and destruction of containers (challenges). 

>Note: I am currently researching the prospect of deploying on-demand private challenge instances using Kubernetes/Docker Swarm but as of the current date/time (03/11/2022) we still rely on single Docker containers for each challenge.

This repository aims to offer a step-by-step guide on how to deploy a successful CTF. Bear in mind that this guide was written according to the past experiences of previous Infrastructure Adminstration Officers in the club, you're free to follow them as is or add your own spice to the mix as you see fit!

### Quick Links
- [Infrastructure and diagrams](https://github.com/cscpsut/CTF-Guide#Architecture)
- [SSH + Sublime/VSCode plugins](https://github.com/cscpsut/CTF-Guide#SSH)
- [Cloudflare DNS/DDoS protection](https://github.com/cscpsut/CTF-Guide#Cloudflare)
- [Setting up CTFd](https://github.com/cscpsut/CTF-Guide#CTFd)
- [Replace Israel from the countries list with "مجرة السلط الأبية"](https://github.com/cscpsut/CTF-Guide#Countries)
- [Setting up FirstBloods notifications using CTFd API (optional)](https://github.com/cscpsut/CTF-Guide#FirstBloods)
- [Setting up FirstBloods discord bot announcer (optional)](https://github.com/cscpsut/CTF-Guide#FirstBloodsDiscord)
- [Deploying Challenges with Docker](https://github.com/cscpsut/CTF-Guide#Dockers)
- [Setting up OpenVPN/WireGaurd for machines](https://github.com/cscpsut/CTF-Guide#VPN)
- [Password Policies and Management (We have to talk about this)](https://github.com/cscpsut/CTF-Guide#Passwords)


## Architecture

- `CTFd VPS` sits behind cloudflare's proxy servers that handles HTTPS and offers DDoS/DoS protection
- `CTFd VPS` has 4 docker containers that function to serve [CTFd](https://github.com/CTFd/CTFd) and are managed using `docker-compose` (more details in [CTFd Setup](https://github.com/CTFd/CTFd))
-  `Challenges VPS` is directly connectable and has the challenges' containers listening on their respective ports
<p align="center">
<img src="random/diagram.png?raw=true" width="800">
</p>


## SSH
### - Setup
- Install windows terminal from [Microsoft Store](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=ar-jo&gl=jo&rtc=1) or [Github](https://github.com/microsoft/terminal) 
- Install SSH client on windows terminal `Settings --> Apps & Features --> Optional Features --> Add a feature --> OpenSSH Client` (PuTTY is just so bad)
- open terminal and simply type `ssh root@<vps-ip>` to have a shell!

### - Sublime/VSCode over SSH
&nbsp;&nbsp;&nbsp;You'll be editing files all the time, you don't want to stick with nano or vim.... _**trust me**_
- To install **RemoteSubl** plugin for Sublime-Text, follow this [guide](https://stackoverflow.com/questions/37458814/how-to-open-remote-files-in-sublime-text-3)
- To install **Remote-SSH** extension for VSCode, follow this [guide](https://code.visualstudio.com/docs/remote/ssh)
- profit 💰💰💰
<p align="center">
<img src="random/Animation.gif?raw=true" width="800">
</p>

## Cloudflare


## CTFd

CTFd is an open-source Capture The Flag framework focusing on ease of use and customizability. It comes with everything you need to run a CTF and it's easy to customize with plugins and themes. Checkout their [Github Repository](https://github.com/CTFd/CTFd), for detailed guidance checkout their [docs](https://docs.ctfd.io)
### TDLR
1- Install docker and docker-compose 
```console
root@server:~# apt install docker.io docker-compose
```
<br/>

2- Clone CTFd github repository
```console
root@server:~# git clone https://github.com/CTFd/CTFd.git
root@server:~# cd CTFd/
```
<br/>

3- Generate SECRET_KEY for the CTFd service
```console
root@server:~/CTFd# head -c 64 /dev/urandom > .ctfd_secret_key
```
<br/>

4- Edit `.conf/nginx/http.conf` file, replace the following lines:
```nginx
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
```
with 
```nginx
proxy_set_header X-Real-IP $http_cf_connecting_ip;
proxy_set_header X-Forwarded-For $http_cf_connecting_ip;
```
This tells nginx to forward the real client's IP instead of CloudFlare's Servers (CTFd shows the team's IP addresses)

<br/>

5- Run with docker-compose, visit `http://<vps-ip>:8000` or `https://cscpsut.com` to check if its running
```console
root@server:~/CTFd# docker-compose up -d
```

## Countries

## FirstBloods

## FirstBloodsDiscord

## Dockers

## VPN

## Passwords
