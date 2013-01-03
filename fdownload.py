#!/usr/bin/env python

import glob
from base64 import b64decode
from urllib2 import urlopen
from sys import exit

def download(url, fname):
    fname = fname if fname.endswith('torrent') else '{0}.torrent'.format(fname)
    try:
        data = urlopen(url, timeout=10)
    except:
        return False

    with open(fname, 'w') as f:
        f.write(data.read())
    return True


def parse_url(url):
    url = url.lstrip('flashget://')
    end_cuts = url.find('&')
    if end_cuts > 0:
        url = url[:end_cuts]

    try:
        url = b64decode(url)
    except:
        return None
    return url[10: -10]

def process():
    files = glob.glob('*.torrent')
    files = [f.rstrip('.torrent') for f in files]

    while True:
        url = raw_input('url = ')
        if url == 'exit':
            exit(0)

        url = parse_url(url)
        if not url:
            print 'illegal url'
            continue

        while True:
            fname = raw_input('name = ')
            if fname == 'exit':
                exit(0)
            if not fname:
                continue
            if fname in files:
                print 'this name already exists, choose another one'
                continue
            break

        status = download(url, fname)
        if status:
            files.append(fname)
            print 'Done'
        else:
            print 'Download Error'


if __name__ == '__main__':
    process()
