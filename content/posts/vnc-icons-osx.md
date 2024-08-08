---
date: 2014-02-05
title: Pimp your VNC shortcuts with macOS system icons
summary: Or, how to use icons for Screen Share (VNC) shortcuts in your Dock.
---

I use VNC (aka Screen Share) a lot, so I keep a folder of frequently accessed machines on my Dock.

The default VNC location file icon for OS X is a bit dull. Fortunately, OS X has a folder of system icons we can use instead. Even better, this folder contains icons for all recent Macbook, iMac and Mac Pro models.

The folder can be located here; hit ⌘⇧G in Finder and paste to jump right to it:

```plaintext
/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources
```

## Creating a VNC shortcut file

In order to access VNC locations from the Dock, we can create a `.vncloc` file. Use a text editor to paste the following into a file and save it with a name ending in `.vncloc`, e.g. `user-hostname.vncloc`:

```xml
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>URL</key>
    <string>vnc://user@hostname.lan</string>
  </dict>
</plist>
```

_Note: you’ll need to change the `vnc://user@hostname.lan` to the remote host’s details._

You can save this file wherever you like. I, for instance, keep all my VNC location shortcuts in a VNC Locations folder in Documents.


## Changing the icon

First choose an icon from the folder above. These are `.icns` files, a wrapper format that contains the same icon in multiple image sizes. They should open in Preview by default; on the largest size hit ⌘A to select the image and ⌘C to copy it.

Next, with the `.vncloc` file we created above, right click and choose “Get info”. There is a small icon preview top-left; click to select it and hit ⌘V and it should paste the new icon. You can drag the location file to the right of your Dock for quick access.
