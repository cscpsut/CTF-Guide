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
- [Setting up FirstBloods discord bot announcer (optional)](https://github.com/cscpsut/CTF-Guide#FirstBloodsDiscord)
- [Setting up FirstBloods notifications using CTFd API (optional)](https://github.com/cscpsut/CTF-Guide#FirstBloods)
- [Deploying Challenges with Docker](https://github.com/cscpsut/CTF-Guide#Dockers)
- [Setting up OpenVPN/WireGaurd for machines](https://github.com/cscpsut/CTF-Guide#VPN)
- [Password Policies and Management (We have to talk about this)](https://github.com/cscpsut/CTF-Guide#Passwords)
- [Password Policies and Management (We have to talk about this)](https://github.com/cscpsut/CTF-Guide#Cloud)

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
- Profit 💰💰💰
<p align="center">
<img src="random/Animation.gif?raw=true" width="800">
</p>

## Cloudflare

This is the cloudflare DNS management interface, you can leave it as is
<p align="center">
<img src="random/cloudflare.png?raw=true" width="800">
</p>

## CTFd

CTFd is an open-source Capture The Flag framework focusing on ease of use and customizability. It comes with everything you need to run a CTF and it's easy to customize with plugins and themes. Checkout their [Github Repository](https://github.com/CTFd/CTFd). For detailed guidance checkout their [docs](https://docs.ctfd.io)
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
This tells nginx to forward the real client's IP instead of CloudFlare's Servers (CTFd shows the team's real IP addresses)

<br/>

5- Run with docker-compose, then visit `http://<vps-ip>:8000` or `https://cscpsut.com` to check if its running
```console
root@server:~/CTFd# docker-compose up -d
```

## Countries
CTFd has a property called _**Country**_ for every user. To remove Israel from the list:

1- shutdown CTFd temporarily
```console
root@server:~/CTFd# docker-compose down
```
<br/>

2- Edit `CTFd/utils/countries/__init__.py` file

```console
root@server:~/CTFd# rsub CTFd/utils/countries/__init__.py
```

<br/>

3- Replace `("IL", "Israel")` with `("GSA", "Galaxy سلط")`

<br/>

4- Power up CTFd again using `--build` option to rebuild and add the new changes
```console
root@server:~/CTFd# docker-compose up --build -d
```
<br/>
5- Profit 💰💰💰 
<br/><br/>
<p align="center">
<img src="random/image.png?raw=true" width="800">
</p>
<br/>

## FirstBloodsDiscord

It is nice to have an announcer for first bloods on discord. Check out this awesome project which uses docker-compose https://github.com/jordanbertasso/CTFd-First-Blood-Discord. Can be added to the same compose file as CTFd so both services can be run together. Before you can use it you have to do the following:

- Create a CTFd API token:

Make sure to store it safely as this token have the same permissions as your account .i.e Admin , Refer to [Passwords](https://github.com/cscpsut/CTF-Guide#Passwords).

<br/>
<p align="center">
<img src="random/Untitled.png?raw=true" width="800">
</p>
<br/>

- Create Discord Webhook:

Go to  `Server Settings --> Intergrations --> Webhooks`. Click on `New Webhook`, specify the channel that will have the first blood announcements on and copy the URL.

<br/>
<p align="center">
<img src="random/discord.png?raw=true" width="800">
</p>
<br/>


The announcements should look like this...
<br/>
<p align="center">
<img src="random/channel.png?raw=true" width="800">
</p>
<br/>

To spice it up you can edit the code and add an embed to have something like this...
<p align="center">
<img src="random/embed.png?raw=true" width="800">
</p>

How? Check out discord.py [docs](https://discordpy.readthedocs.io/en/stable/api.html). This is [file](https://github.com/jordanbertasso/CTFd-First-Blood-Discord/blob/main/ctfd-first-blood-discord/solve_handler.py) responsible for sending the announcments, customize it as you see fit 

## FirstBloods
To be done later

## Dockers

## VPN
I recommend using https://github.com/angristan/openvpn-install. Run the installation script for the first time then use [batch.py](https://github.com/cscpsut/CTF-Guide/blob/main/random/batch.py) to create config files for all competitors given a CSV file.

## Passwords

This section not only includes login password, but also sensitive secrets like CTFd API tokens. Anyone who has your token has admin privileges on your CTFd which allows extracting flags, add challenges, remove challenges ....etc. You get my point. Also Discord Webhook Links, you don't want people to hijack your first blood anouncment channel. 

Things I have to say. Please be really serious about this:
- Do not use weak passwords. ALWAYS generate random strong passwords
- Avoid copying or sending passwords over chat (Discord, whatsapp...etc)

I recommend using a shared/synced Password Manager for all those who are involved in CTF deployment/writing. My favourite is [buttercup](https://github.com/buttercup/buttercup-desktop). It is an open-source password manager and can be self-hosted (Check out https://github.com/cscpsut/CTF-Guide#Cloud), it can also be installed on both IOS/Android and boimetrics unlocking can be enabled. 


 ## Cloud

CTFd cannot handle large file attachments (for example Memory Captures and Disk Images), so you have to upload them to Google Drive. But sometimes the upload/download speed can be disappointing and sometimes Google Drive blocks you from uploading after spamming many times. Why not just host your own cloud/Drive! Check out https://github.com/nextcloud/server! You can also use it to safely store the shared passwords Vault (Make sure to enabl WebDAV which Nextcloud supports) 


