---
published: 2021-06-12
summary: Learn how to use systemd to run a simple python service
title: How to make your own Raspberry Pi service
---

Many Raspberry Pi projects involve running a program continually in the background. In this guide we’re going to look at how we can use part of the system that powers the Raspberry Pi, systemd, to run a custom Python script in the background, starting when the device powers on.

Some notes before we start

1. This guide assumes some familiarity with the command line, at least to the level covered in the [Raspberry Pi](https://www.raspberrypi.org/documentation/usage/terminal/) documentation. We’ll be executing commands as the root user so make sure you understand what you’re asking the terminal to do before you execute a command!

2. While it’s possible to write a script that uses Python [http.server](https://docs.python.org/3/library/http.server.html), it’s not a good idea – especially if the web server is visible to the open internet. This module is useful for development but you should look into using a production web server like [gunicorn](https://gunicorn.org), [uvicorn](https://www.uvicorn.org) or [nginx](https://www.nginx.com).

In Unix-like operating systems such as Raspberry Pi OS, a program that is run in the background by the operating system is called a service. Services are managed by a service daemon – essentially a service responsible for starting and stopping other services. On Raspberry Pi OS and it’s parent Linux distribution, Debian, this service daemon is called [systemd](https://en.wikipedia.org/wiki/Systemd).

Lets say we want to implement a service called `timestamp` which, once a second, writes the current date and time to a file in our home directory called `~/timestamp.txt`. The code for this, in a file called `~/timestamp.py`, might look something like this:

```python
from datetime import datetime
from pathlib import Path
import time

log_file = Path('timestamp.txt')

while True:
    log_file.write_text(str(datetime.now()))
    time.sleep(1)
```

We can verify that this runs by running it like a normal Python script:

```sh
python3 timestamp.py
```

To make this into a fully fledged service managed by systemd we need to create a service file. systemd service files can be found in a couple of places but for correctness we should add it to `/etc/systemd/system/`. Note that this is a system folder so we need to use `sudo` with our editor to create the file, for example:

```sh
sudo nano /etc/systemd/system/timestamp.service
```

```
[Unit]
Description=My timestamp service
After=mult-user.target

[Service]
ExecStart=/usr/bin/env python3 /home/pi/timestamp.py

[Install]
WantedBy=multi-user.target
```

After writing and closing the file we need to tell systemd to reload its list of available services. We do this using `systemctl` a command provided by systemd:

```sh
sudo systemctl daemon-reload
```

Now we can use `systemctl` to tell systemd to enable our timestamp service:

```sh
sudo systemctl enable timestamp.service
```

This will run the service every time the system is booted. If we only wanted to run this service until we reboot the system we could use `start` here instead instead of `enable`. We can also `stop` the service if it’s currently running, or `disable` to prevent systemd from starting it again in the future (e.g. on next boot). To check whether the service is running we can use

```sh
sudo systemctl status timestamp.service
```

We can also verify that our service is working by watching the timestamp.txt file for changes – press `Ctrl+C` to stop watching:

```sh
watch -n 1 tail timestamp.txt
```
