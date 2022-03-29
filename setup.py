#!/usr/bin/env python3

from setuptools import setup
import os
from os.path import join, abspath, dirname, exists
from pathlib import Path
import sys
import shutil
import subprocess

# Read README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Update the translations
PO_DIR = 'translations'
if not exists(PO_DIR):
    os.makedirs(PO_DIR)
subprocess.check_call(["xgettext", "-o", join(PO_DIR, "caffeine-indicator.pot"), "--language=python", "--from-code=UTF-8", "caffeine-indicator"])

def compile_catalog(po_dir, prg_name):
    po_files = []
    for dirpath, dirnames, filenames in os.walk(po_dir):
        for file in filenames:
            if file.split('.')[-1] == "po":
                po_files.append(os.path.join(dirpath, file))

    for po in po_files:
        lang = po.split('/')[-1]
        print("Compiling for Locale: "+"".join(lang.split(".")[:-1]))
        lang = lang.split('-')[-1]
        lang = lang.split('.')[0]
        lang = lang.strip()
        if not lang:
            continue

        lang_lc_dir = os.path.join('share', 'locale', lang, 'LC_MESSAGES')
        if not os.path.isdir(lang_lc_dir):
            os.makedirs(lang_lc_dir)

        subprocess.check_call(["msgfmt", po, "-o", os.path.join(lang_lc_dir,prg_name+".mo")])

compile_catalog(PO_DIR, "caffeine-indicator")

# Add extra data files
data_files = []
for path, _, files in os.walk("share"):
    if len(files) > 0:
        data_files.append(tuple((path,
            [join(path, file) for file in files])))
desktop_name = "caffeine.desktop"
desktop_file = join("share", "applications", desktop_name)
autostart_dir = join("etc", "xdg", "autostart")
if not exists(autostart_dir):
    os.makedirs(autostart_dir)
shutil.copy(desktop_file, autostart_dir)
data_files.append(tuple(("/" + autostart_dir, [join(autostart_dir, desktop_name)])))

setup(name="cups-of-caffeine",
    version="2.9.10",
    description="Keep your computer awake.",
    license="GPLv3",
    author="Reuben Thomas",
    author_email="rrt@sc3d.org",
    url="https://launchpad.net/caffeine",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    data_files=data_files,

    scripts=["caffeine", "caffeinate", "caffeine-indicator"],
    )
