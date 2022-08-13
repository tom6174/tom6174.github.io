---
title: Developing with multiple GitHub accounts on a MacBook
layout: post
post-image: ../assets/images/github_multiple_users.png
description: I have two github accounts now. https://github.com/tom6174 and https://github.com/thomas6174. Both are very active accounts. This post outlines how I setup my MacBook for easy git usage.
tags: github multiple_accounts
permalink: "/blog/:title"
---

###### Source : [`Ibrahim's Blog`](https://medium.com/@ibrahimlawal/developing-with-multiple-github-accounts-on-one-macbook-94ff6d4ab9ca)


> I am using a third, nonexistent account in the samples to show that this can be extended to more than 2 accounts.
	
## Create SSH keys for all accounts
First make sure your current directory is your ***.ssh*** folder.

```
$ cd ~/.ssh 
$ ssh-keygen -t rsa -C "my@tech-knowledge" -f "github-tom6174" 
$ ssh-keygen -t rsa -C "my@family-log" -f "github-thomas6174" 
$ ssh-keygen -t rsa -C "moi@uc-" -f "github-ucsky6174" 
```

* The **-C** option is a comment to help identify the key.
* The **-f** option specifies the file name for the key pair.


You can choose how to name the key pair. I followed the recommendation here and used ***github-{GitHub username}***.
You’ll now have a public and private key in your ~/.ssh/ folder.

## Add the SSH keys to your SSH-agent
Your keys are now created but won’t be used until they are added to the agent. Let’s add them.

```
$ ssh-add -K ~/.ssh/github-ibrahimlawal
$ ssh-add -K ~/.ssh/github-ibrahimlawal-paystack
$ ssh-add -K ~/.ssh/github-ibraheemweynodey
```

You only need the **-K** option on a mac. More details on adding keys to the SSH agent here.

## Import all the public keys on the corresponding GitHub accounts

You can quickly copy each key to the clipboard with the commands below. After each copy,
* Visit [here](https://github.com/settings/keys){:target="_blank"} while logged in to the corresponding GitHub account; 
* Click the ‘New SSH key’ button and paste the public key from clipboard.

```
$ pbcopy < ~/.ssh/github-ibrahimlawal.pub
$ pbcopy < ~/.ssh/github-ibrahimlawal-paystack.pub
$ pbcopy < ~/.ssh/github-ibrahimweynodey.pub
```


## Create GitHub host entries for all accounts
The ***~/.ssh/config*** file allows you specify a lot of config options for SSH. The commands below create the file if it doesn’t exist. And opens it in your default editing command… Likely TextEdit.

```
$ open -e ~/.ssh/config
```

Add these lines to the file, each block corresponding to each account you created earlier.
```
#ibrahimlawal account
Host github.com-ibrahimlawal
    HostName github.com
    User git
    IdentityFile ~/.ssh/github-ibrahimlawal
#ibrahimlawal-paystack account
Host github.com-ibrahimlawal-paystack
    HostName github.com
    User git
    IdentityFile ~/.ssh/github-ibrahimlawal-paystack
#ibraheemweynodey account
Host github.com-ibraheemweynodey
    HostName github.com
    User git
    IdentityFile ~/.ssh/github-ibraheemweynodey
```    

## What account should be default?
Make it the global:

```
$ git config --global user.name "ibrahimlawal"
$ git config --global user.email "my@pers.on.al"
```
This will be used by default.

## Cloning GitHub repositories using secondary accounts
For those that are not yet cloned,
* Go to the root folder of the repository.
* Use the format below to craft the clone command

```
$ git clone git@github.com-{your-username}:{the-repo-organisation-or-owner-user-name}/{the-repo-name}.git
[e.g. $] git clone git@github.com-ibrahimweynodey:n/n.git
```

## Updating remote for repositories already cloned
Changing the user for repositories already cloned should also take only 3 steps:

```
$ git remote set-url origin git@github.com-{your-username}:{the-repo-organisation-or-owner-user-name}/{the-repo-name}.git

[e.g. $] git remote set-url origin git@github.com-ibrahimweynodey:n/n.git
```

## Finally
From now on, to ensure that your commits and pushes from each repository on the system uses the correct GitHub user — especially in case it is not to be the default — you will have to do the following in every repository. Freshly cloned or existing before the need to have multiple accounts on a system. Just pick the correct pair. Running all will only mean all repositories will be committed with the play account!

```
$ git config user.email "my@pers.on.al"
$ git config user.name "Ibrahim Lawal"

$ git config user.email "my@wo.rk"
$ git config user.name "Ibrahim Lawal"

$ git config user.email "my@pl.ay"
$ git config user.name "Ibrahim wey no dey"
```
