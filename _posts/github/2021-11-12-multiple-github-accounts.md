---
title: Developing with multiple GitHub accounts on one MacBook
layout: post
post-image: "https://raw.githubusercontent.com/thedevslot/WhatATheme/master/assets/images/What%20is%20Jekyll%20and%20How%20to%20use%20it.png?token=AHMQUELVG36IDSA4SZEZ5P26Z64IW"
description: I have two github accounts now. https://github.com/tom6174 and https://github.com/thomas6174. Both are very active accounts. This post outlines how I setup my MacBook for easy git usage.
tags: [github]
permalink: "/blog/:title"
---

Jekyll is a simple, blog-aware, static site generator perfect for personal, project, or organization sites. Think of it like a file-based CMS, without all the complexity. Jekyll takes your content, renders Markdown and Liquid templates, and spits out a complete, static website ready to be served by Apache, Nginx or another web server. Jekyll is the engine behind GitHub Pages, which you can use to host sites right from your GitHub repositories and if you don't know what GitHub Pages are you can visit on click [here](https://help.github.com/en/github/working-with-github-pages/about-github-pages){:target="blank"} or [here](https://pages.github.com/){:target="blank"}
###### Source : [`Ibrahim's Blog`](https://medium.com/@ibrahimlawal/developing-with-multiple-github-accounts-on-one-macbook-94ff6d4ab9ca)

> I am using a third, nonexistent account in the samples to show that this can be extended to more than 2 accounts.
	
# Create SSH keys for all accounts
First make sure your current directory is your ***.ssh*** folder.

`$ cd ~/.ssh`<br>
`$ ssh-keygen -t rsa -C "my@pers.on.al" -f "github-ibrahimlawal"`<br>
`$ ssh-keygen -t rsa -C "my@wo.rk" -f "github-ibrahimlawal-paystack"`<br>
`$ ssh-keygen -t rsa -C "moi@pl.ay" -f "github-ibraheemweynodey"`<br>

* The -C option is a comment to help identify the key.
* The -f option specifies the file name for the key pair.


You can choose how to name the key pair. I followed the recommendation here and used ***github-{GitHub username}***.
You’ll now have a public and private key in your ~/.ssh/ folder.

# Add the SSH keys to your SSH-agent
Your keys are now created but won’t be used until they are added to the agent. Let’s add them.

>`$ ssh-add -K ~/.ssh/github-ibrahimlawal`<br>
>`$ ssh-add -K ~/.ssh/github-ibrahimlawal-paystack`<br>
>`$ ssh-add -K ~/.ssh/github-ibraheemweynodey`

You only need the -K option on a mac. More details on adding keys to the SSH agent here.

### After Installing the Requirements you can follow these guides:
**For detailed install instructions have a look at the guide for your operating system.**
* [macOS](https://jekyllrb.com/docs/installation/macos/){:target="_blank"}
* [Ubuntu](https://jekyllrb.com/docs/installation/ubuntu/){:target="_blank"}
* [Other Linux Distros](https://jekyllrb.com/docs/installation/other-linux/){:target="_blank"}
* [Windows](https://jekyllrb.com/docs/installation/windows/){:target="_blank"}

### Creating a new Jekyll site
**We can create a new Jekyll site just by a simple command:**<br>
> # `jekyll new my-site`

Jekyll will create a new directory named as `my-site` which is customizable (i.e., you can change the name from `my-site` to anything you want for example `jekyll new brutus`).

### Changing into the Directory
**We have to go inside the directory:**<br>
> # `cd my-site`

Again, `my-site` is just a random name which is customizable.

### Building the site and making it available on a local server
> # `bundle exec jekyll serve`

### Browsing your Jekyll site
> # Browse to [`http://localhost:4000/`](http://localhost:4000/){:target="_blank"}

###### On encountering any problem while building and serving your Jekyll site you can consider visiting to the [troubleshooting](https://jekyllrb.com/docs/troubleshooting/#configuration-problems){:target="_blank"} page