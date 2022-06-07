#!/usr/bin/python


import re
from six.moves import input
import sys


def main():
    rpm_re = re.compile('[^/]+\.rpm')
    distros = [
        'centos',
        'redhat',
        'fedora',
        'opensuse',
        'suse',
    ]

    while True:
        line = input('')
        parts = line.split(' ')
        url = parts[0]
        distro = next(
            (
                d for d in distros
                if d in url.lower()
            ),
            'unknown'
        )
        search_res = rpm_re.search(url)
        print(
            "OK store-id=%s" % (
                'distro:%s:%s' % (distro, search_res.group())
                if search_res else url
            )
        )
        sys.stdout.flush()


if __name__ == '__main__':
    main()

