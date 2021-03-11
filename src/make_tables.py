#!/usr/bin/python3

import subprocess
import sys

if __name__ == '__main__':
    subprocess.run(sys.argv[1:], check=True)
    open('fake-table-header.h', 'w')
