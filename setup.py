#!/usr/bin/env python3

from distutils.core import setup
import os
from os.path import join, abspath, dirname, exists
import shutil
import subprocess

ROOT_DIR = dirname(abspath(__file__))
PO_DIR = 'translations'
VERSION = open(join(ROOT_DIR, "VERSION")).read().strip()

# Update the translations
if not exists(PO_DIR):
    os.makedirs(PO_DIR)
subprocess.check_call(["xgettext", "-o", join(PO_DIR, "caffeine-indicator.pot"), "--language=python", "--from-code=UTF-8", "caffeine-indicator"])
subprocess.check_call(["./compile_translations.py", "caffeine-indicator", PO_DIR])

# don't trash the system icons!
blacklist = ['index.theme']

data_files = []
for path, _, files in os.walk("share"):
    if len(files) > 0:
        data_files.append(tuple((path,
            [join(path, file) for file in files if file not in blacklist])))

desktop_name = "caffeine.desktop"
desktop_file = join("share", "applications", desktop_name)
autostart_dir = join("etc", "xdg", "autostart")
if not exists(autostart_dir):
    os.makedirs(autostart_dir)
shutil.copy(desktop_file, autostart_dir)
data_files.append(tuple(("/" + autostart_dir, [join(autostart_dir, desktop_name)])))
data_files.append(tuple(("", ["VERSION", "compile_translations.py"])))

setup(name="caffeine",
    version=VERSION,
    description="Stop the desktop from becoming idle in full-screen mode.",
    license="GPLv3",
    author="The Caffeine Developers",
    author_email="rrt@sc3d.org",
    url="https://launchpad.net/caffeine",
    data_files=data_files,
    scripts=["caffeine", "caffeinate", "caffeine-indicator"]
    )
