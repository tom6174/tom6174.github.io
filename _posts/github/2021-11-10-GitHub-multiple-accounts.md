---
title: Developing with multiple GitHub accounts on a MacBook
layout: post
post-image: ../assets/images/github_multiple_users.png
date: 2021-11-10 00:40:00
description: I have two github accounts now. https://github.com/tom6174 and https://github.com/uc1973. Both are very active accounts. This post outlines how I setup my MacBook for easy git usage.
category: github
tags: github multiple_accounts
permalink: "/blog/:title"
---

###### Source : [`Ibrahim's Blog`](https://medium.com/@ibrahimlawal/developing-with-multiple-github-accounts-on-one-macbook-94ff6d4ab9ca)


> I am using a second, nonexistent account in the samples to show that this can be extended to more than 1 account.
	
## Create SSH keys for all accounts
First make sure your current directory is your ***.ssh*** folder.

```
$ cd ~/.ssh 
$ ssh-keygen -t rsa -b 4096 -C "thomas78.song@gmail.com" -f ~/.ssh/id_rsa_tom
$ ssh-keygen -t rsa -b 4096 -C "uc.thomas78@gmail.com" -f ~/.ssh/id_rsa_uc
```

* The **-C** option is a comment to help identify the key.
* The **-f** option specifies the file name for the key pair.


You’ll now have a public and private key in your ~/.ssh/ folder.

## Add a passphrase
Next, you will be prompted to add an (optional) passphrase. We recommend you do so because it adds an extra layer of security: if someone gains access to your computer, your keys will be compromised unless they are attached to a passphrase.

To update the passphrase for your SSH keys:
```
$ ssh-keygen -p -f ~/.ssh/id_rsa_tom
$ ssh-keygen -p -f ~/.ssh/id_rsa_uc
```

You can check your newly created key with:
```
$ ls -la ~/.ssh
```

## Add the SSH keys to your SSH-agent
Your keys are now created but won’t be used until they are added to the agent. Let’s add them.

```
$ eval "$(ssh-agent -s)" && \
$ ssh-add -K ~/.ssh/id_rsa_tom
$ ssh-add -K ~/.ssh/id_rsa_uc
```

You only need the **-K** option on a mac. More details on adding keys to the SSH agent here.


## Edit your SSH config

If you don’t have one, create an SSH config file `touch ~/.ssh/config` and add the following contents to it:
```
#tom6174에 대한 SSH 설정
Host github.com-tom6174
    HostName github.com
    User tom6174
    IdentityFile ~/.ssh/id_rsa_tom

#uc1973에 대한 SSH 설정
Host github.com-UC1973
    HostName github.com
    User UC1973
    IdentityFile ~/.ssh/id_rsa_uc
```

## Import all the public keys on the corresponding GitHub accounts

You can quickly copy each key to the clipboard with the commands below. After each copy,
* Visit [here](https://github.com/settings/keys){:target="_blank"} while logged in to the corresponding GitHub account; 
* Click the ‘New SSH key’ button and paste the public key from clipboard.

```
$ pbcopy < ~/.ssh/id_rsa_tom.pub
$ pbcopy < ~/.ssh/id_rsa_uc.pub
```
or
```
tr -d '\n' < ~/.ssh/id_rsa_tom.pub | pbcopy
tr -d '\n' < ~/.ssh/id_rsa_uc.pub | pbcopy
```

Paste the public key on Github.
* Sign in to Github Account
* Goto Settings > SSH and GPG keys > New SSH Key
* Paste your copied public key and give it a Title of your choice.


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
[e.g. $] git clone git@github.com-tom6174:tom6174/tom6174.github.io.git
```

## Updating remote for repositories already cloned
You can now choose to, clone your repo, add or change your remote with:

```
$ git remote add origin git@github.com-tom6174:tom6174/tom6174.github.io.git

$ git remote set-url origin git@github.com-uc1973:UC1973/uc1973.github.io.git
```

## Finally
From now on, to ensure that your commits and pushes from each repository on the system uses the correct GitHub user — especially in case it is not to be the default — you will have to do the following in every repository. Freshly cloned or existing before the need to have multiple accounts on a system. Just pick the correct pair. Running all will only mean all repositories will be committed with the play account!

```
$ git config user.email "thomas78.song@gmail.com"
$ git config user.name "tom6174"

$ git config user.email "uc.thomas78@gmail.com"
$ git config user.name "UC1973"
```
