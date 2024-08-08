---
date: 2024-02-19
title: macOS Caffeinate Shortcut
summary: How to use Shortcuts to prevent your Mac from sleeping
image:
  url: /posts/img/caffeinate-shortcut.avif
  width: 1470
  height: 980
---

My work MacBook is a managed device, so various system preferences have been disabled or restricted for security reasons. One such setting is the screen saver timeout which can’t be set to longer than 15 minutes.

As someone whose job involves cross-device testing, I need my Mac to stay awake so I can hear notifications for emails and Slack messages. It’s annoying to realise that it’s gone to sleep because I forgot to wiggle my mouse while I was testing something.

I’m a security conscious person and would never leave my devices unlocked. Risk is never zero, but as a fully remote worker my home has fewer prying eyes than an office. I think it’s reasonable to work around this restriction.

## Caffeinate

Like some Linux distros, macOS has a `caffeinate` command which will keep the system awake while it’s running. It has a man page which will do a better job of explaining the command’s various options than me – you can run `man caffeinate` from a terminal to read it, but I’ve found that `caffeinate -dims` works for my needs.

I’ve been using this trick for several years now, but what’s really elevated it to the next level is macOS Shortcuts which gives me the ability to toggle it on and off from my menu bar.

## Creating a shortcut

To create a toggle, open the Shotcuts app (press <kbd>⌘</kbd> + <kbd>Space</kbd> and type “Shortcuts”) and click the plus button to create a new shortcut. Use the search box to find the ‘Run Shell Script’ action and paste the following into the Shell Script text box:

```sh
caffeinate -dims || true
```

_If you’re curious, the `... || true` stops the Shortcuts app from thinking the command failed when you toggle the shortcut off._

![A screenshot of the Shortcuts app showing a shortcut with the shell script above](/posts/img/caffeinate-shortcut-screenshot.avif)

Choose a name and an icon (I chose ‘Caffeinate’ and a brown coffee cup because I lack imagination) and then close the editor.

If you drag the shortcut from All Shortcuts to Menu Bar on the left, you’ll get a Shortcuts icon in the menu bar from which you can toggle your new shortcut. Simply click it to keep your Mac awake, and again to stop the shortcut allow your Mac sleep like normal.

And that’s it! Let me know if you find this helpful and if you have a useful shortcut I’d love to hear it.
