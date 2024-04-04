---
date: 2015-09-15
title: OS X package management, without sudo
summary: An old take on setting up Homebrew and npm on macOS.
---

Recently, I had to use a shared company MacBook for a web dev project. Knowing this shared device would only be mine for a few weeks, I wanted to be able to delete everything when I was done.

I created a new OS X user and started looking into how I could install Homebrew and npm for that user. In doing this I found that both package managers could now be used without `sudo`. Here’s how.


## Homebrew

Homebrew doesn’t normally require sudo permissions, but installs to `/usr/local/bin` which won’t be deleted when the current user is deleted.

Installing Homebrew for the current user is as easy as cloning the repository and adding it’s `bin` to your `$PATH`. I chose to install it in `~/homebrew`, to do the same fire up a new shell in your home directory (or type `cd`) and enter:

```shell
git clone https://github.com/Homebrew/homebrew
```

Next you need to add `~/homebrew/bin` to your `$PATH` so you can use the `brew` command, as well as anything else you choose to install with `brew install`. The simplest way to do this is to add this line to the end of your `~/.bashrc` or `~/.zshrc` file:

```shell
export PATH="${HOME}/homebrew/bin"
```

You will need to start a new terminal session for the changes to take effect. After which you can test that it works by running `brew update` and, for example, `brew install tree`.


## npm

npm is installed with Node.js, so if you followed the instructions to install Homebrew the easiest way to install both is:

```shell
brew install node
```

This installs npm to `~/homebrew/bin/npm`, however npm will still try to install global packages to `/usr/local/bin`. You can change this behaviour by changing npm’s ‘prefix’ setting to a new folder in your home directory:

```shell
mkdir ~/npm-global
npm config set prefix "~/npm-global"
```

As with Homebrew, you need to add `~/npm-global/bin` to your `$PATH` so any programs you install with `npm install --global` can be found. The simplest way to do this is to add this line to the end of your `~/.bashrc` or `~/.zshrc` file:

```shell
export PATH="${HOME}/npm-global/bin"
```

Again, you will need to start a new terminal session for the changes to take effect. Test if npm works without sudo by running, for example, `npm install -g vtop`.


## Ruby

Installing Ruby gems is easier because it’s supported out of the box. To install for the current user only, use the `--user-install` flag:

```shell
gem install jekyll --user-install
```

The gem command will warn you that the install directory in `~/.gem/ruby` is not in your `$PATH`. The exact path you need to add depends on the Ruby version you have installed, but you will need add something like this to your `~/.bashrc` or `~/.zshrc` file:

```shell
export PATH="${HOME}/.gem/ruby/2.0.0/bin"
```

## Desktop Applications

Finally, you can also install OS X apps per-user if you wish. By default, if you’re installing from a `.dmg` the app will ask you to drag the program to `/Applications`. Each OS X user also has a `~/Applications` folder in their home directory, simply dragging new apps there will install them for the current user only.
