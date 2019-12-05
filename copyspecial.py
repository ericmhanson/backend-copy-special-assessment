#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = 'Eric Hanson'


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    """returns a list of the absolute paths of the
    special files in the given directory"""
    file_list = []
    for dir_path, _, filenames in os.walk(dir):
        for f in filenames:
            if re.search(r'__\w+__', f):
                file_list.append(os.path.abspath(os.path.join(dir_path, f)))
                print(os.path.abspath(os.path.join(dir_path, f)) + '\n')
        break
    return file_list


def copy_to(paths, dir):
    """given a list of paths, copies those files into the given directory"""
    if not os.path.exists(dir):
        os.makedirs(dir)
    for p in paths:
        shutil.copy(p, dir)


def zip_to(paths, zippath):
    """given a list of paths, zip those files up into the given zipfile"""
    command = ['zip', '-j']
    zippath = [zippath]
    command_list = command + zippath + paths
    # print(command_list)
    print('Command I am going to do:')
    print(' '.join(command_list))
    try:
        subprocess.check_output(command_list)
    except subprocess.CalledProcessError as e:
        print('{}'.format(e.output))
        exit(e.returncode)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument('dir', help='source directory to read special file')
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.
    # If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions

    source_dir, to_dir, to_zip = args.dir, args.todir, args.tozip
    if source_dir:
        file_list = get_special_paths(source_dir)

    if source_dir and to_dir:
        copy_to(file_list, to_dir)

    if source_dir and to_zip:
        zip_to(file_list, to_zip)


if __name__ == "__main__":
    main()
