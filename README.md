# Caffeine-aw - Keep your computer awake, even when the full-screen window is not focused!

Caffeine-aw URL: https://github.com/jamescherti/caffeine-aw

## What is the difference between caffeine-aw and caffeine?

Here are some of the enhancements in **Caffeine-aw**:
* **Caffeine-aw** prevents the desktop from becoming idle **when one of the windows is in full-screen mode**, even if the full-screen window is not focused.
* The process name is set to 'caffeine', 'caffeine-indicator', and 'caffeinate'.
* **Caffeine-aw** no longer inhibits desktop idleness when it is terminated.
* Only one instance of **Caffeine-aw** can run at a time.
* XFCE Desktop: Toggle 'XFCE Presentation Mode' on and off.

## What is Caffeine-aw?

Caffeine-aw is a small daemon that prevents the desktop from becoming idle (and hence the screen saver and/or blanker from activating) when one of the windows is in full-screen mode.

Also provided are an indicator, caffeine-indicator, that gives a manual toggle, and caffeinate, which allows desktop idleness to be inhibited for the duration of any command. See their man pages for more information.

## Installation

```sh
sudo pip install git+https://github.com/jamescherti/caffeine-aw
```

## Maintainer

- [James Cherti](https://www.jamescherti.com/)
