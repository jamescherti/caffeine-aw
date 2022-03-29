# Caffeine

https://launchpad.net/caffeine/

Caffeine is a small daemon that prevents the desktop from becoming idle (and
hence the screen saver and/or blanker from activating) when the active
window is full-screen.

Also provided are an indicator, caffeine-indicator, that gives a manual
toggle, and caffeinate, which allows desktop idleness to be inhibited for
the duration of any command. See their man pages for more information.

Caffeine is distributed under the GNU General Public License, either version
3, or (at your option) any later version. See COPYING.

The Caffeine SVG icons are Copyright (C) 2009 Tommy Brunn
(http://www.blastfromthepast.se/blabbermouth), and distributed under the
terms of the GNU Lesser General Public License, either version 3, or (at
your option) any later version. See COPYING.LESSER.

Caffeine uses pyewmh from https://sf.net/projects/pyewmh


## If you think you’ve found a bug

Try running, in a terminal:

```
window_id=`xwininfo | grep "Window id" | cut -d " " -f 4`
```

Now click on the terminal window, and then run:

```
xdg-screensaver suspend $window_id
xdg-screensaver resume $window_id
```

This performs the same steps at a lower level as turning Caffeine on then
off again manually. If this gives the same problem as using Caffeine, then
the bug is definitely not in Caffeine.


## Testing translations

If you want to test out a translation without changing the language for the
whole session, run caffeine as e.g.: LANGUAGE=ru ./caffeine

To compile the translations: ./update_translations.py (this is done
automatically when building the package, so no need to do it normally).

You will need a language pack for the given language. Be aware that some
stock items will not be translated unless you log in with a given language.
