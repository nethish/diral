#! /usr/bin/python3
import os
import sqlite3
import sys
import argparse

## Constants
HOME = os.path.expanduser('~')
DIR = HOME + '/.local/share/diral'
ALIAS_DB = DIR + '/alias.db'

CREATE = '''
    CREATE TABLE IF NOT EXISTS alias(dir varchar(128), alias_name varchar(8), alias string varchar(256));
'''

SELECT = '''
    SELECT * FROM alias WHERE dir = ?
'''

INSERT = '''
    INSERT INTO alias VALUES (?, ?, ?)
'''

DELETE = '''
    DELETE FROM alias WHERE alias_name = ?
'''

EXISTS = '''
    SELECT * FROM alias WHERE alias_name = ?
'''

## ----------------------

parser = argparse.ArgumentParser()

parser.add_argument('alias', help="Alias name", nargs='?')
parser.add_argument('command', help="Command", nargs='*')
parser.add_argument('-d', '--delete', help="Delete Alias")

args = parser.parse_args()
# print(args)
# print('Coward', os.getcwd())

def create_if_not_exists():
    os.makedirs(DIR, exist_ok = True)
    get_cursor().execute(CREATE)

def get_cursor():
    return sqlite3.connect(ALIAS_DB).cursor()

def load():
    cur_dir = os.getcwd()
    cur = get_cursor()

    rows = cur.execute(SELECT, (cur_dir,)).fetchall()

    for row in rows:
        command = 'alias ' + row[1] + '=' + '\'' + row[2] + '\''
        print(command)
        os.system(command)

def save():
    if len(sys.argv) < 3:
        return

    alias, command = args.alias, ' '.join(args.command)

    exists = len(get_cursor().execute(EXISTS, (alias, )).fetchall()) > 0
    if exists:
        print('the command already exists. delete and recreate; diral -d <alias>')
        return

    cur_dir = os.getcwd()

    conn = sqlite3.connect(ALIAS_DB)
    cursor = conn.cursor()
    cursor.execute(INSERT, (cur_dir, alias, command))
    conn.commit()

def delete(alias):
    conn = sqlite3.connect(ALIAS_DB)
    cursor = conn.cursor()
    cursor.execute(DELETE, (alias,))
    conn.commit()

create_if_not_exists()
if args.delete:
    delete(args.delete)
if args.alias and args.command:
    save()
else:
    load()

