#!/usr/bin/env python

import urllib
import os


LOCATION = '/home/wang/.myhidefiles/cast'

def _down(url):
    file_name = os.path.basename(url)
    file_path = os.path.join(LOCATION, file_name)
    res = urllib.urlopen(url)
    with open(file_path, 'w') as f:
        f.write(res.read())

    print 'done,', url

def down(prefix, id_range, subfix):
    for i in id_range:
        url = "{0}{1}{2}".format(prefix, i, subfix)
        _down(url)


def start():
    prefix = raw_input("prefix= ")
    subfix = raw_input("subfix= ")
    start_id = raw_input("start id= ")
    end_id = raw_input("end id= ")
    
    start_id = int(start_id)
    end_id = int(end_id)

    id_range = [str(i).zfill(2) for i in range(start_id, end_id+1)]
    print id_range
    down(prefix, id_range, subfix)


if __name__ == '__main__':
    start()
