# Caffeine-aw - Keep your computer awake, even when the full-screen window is not focused!

Caffeine-aw URL: https://github.com/jamescherti/caffeine-aw

(Caffeine-aw is a fork of caffeine 2.9.12)

## What is the difference between caffeine-aw and caffeine?

* **Caffeine-aw** (this fork) prevents the desktop from becoming idle **when one of the windows is in full-screen mode**, even if the fullscreen window is not focused.
* **Caffeine** only prevents the desktop from becoming idle if the focused window is in full-screen mode.

## What is caffeine-aw?

Caffeine-aw is a small daemon that prevents the desktop from becoming idle (and
hence the screen saver and/or blanker from activating) when one of the windows
is in full-screen mode.

Also provided are an indicator, caffeine-indicator, that gives a manual
toggle, and caffeinate, which allows desktop idleness to be inhibited for
the duration of any command. See their man pages for more information.

## Installation

```sh
sudo pip install git+https://github.com/jamescherti/caffeine-aw
```

## License

Caffeine is distributed under the GNU General Public License, either
version 3, or (at your option) any later version. See COPYING.

The Caffeine SVG icons are Copyright (C) 2009 Tommy Brunn, and distributed
under the terms of the GNU Lesser General Public License, either version 3, or
(at your option) any later version. See COPYING.LESSER.
