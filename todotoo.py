#!/usr/bin/env python

# todotoo - command line interface to manage todo.txt
# Copyright (C) 2015 Robert van Bregt
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import argparse
import ConfigParser

__version__   = "0.0.1"
__date__      = "2015-05-22"
__author__    = "Robert van Bregt (robert@robertvanbregt.nl)"
__copyright__ = "Copyright 2015, Robert van Bregt"
__license__   = "GPL"

def todo_arguments():
    parser = argparse.ArgumentParser(description='Manage your TODO.TXT')
    parser.add_argument('-c', dest='config_file', default='./todotoo.conf',
                        help='path to config file')
    parser.add_argument('action',
                        help='the action to execute')
    return parser.parse_args()

def todo_config(config_file):
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    return config

def read_todos(todo_filepath):
    todo_file = open(todo_filepath, 'r')
    raw_todos = todo_file.readlines()
    todo_file.close()
    todos = []
    for item in raw_todos:
        item = item.strip("\n")
        todos.append(item)
    return todos

def list_todos(results, numbers = 1):
    if len(results) == 0:
        #empty list
        print("No results.")
    else:
        i = 1
        for item in results:
            if numbers == 1:
                print("{0}. {1}".format(i, item))
            else:
                print(item)
            i += 1

if __name__ == "__main__":
    args = todo_arguments()

    config = todo_config(args.config_file)

    todo_path = config.get('files', 'todo_dir')
    # TODO: only add slash if required
    todo_filepath = todo_path + "/" + config.get('files', 'todo_file')

    # at this time, just list file contents
    todos = read_todos(todo_filepath)
    list_todos(todos)

    sys.exit()
