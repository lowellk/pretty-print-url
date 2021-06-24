#!/usr/bin/env python3

# requires python 3.8.5

# make installer
# http://docs.python.org/distutils/introduction.html

import sys
from urllib.parse import urlparse, parse_qs

def pretty_print_url(url_string):
    """pretty print an url to stdout"""
    parsed = urlparse(url_string)
    query = parse_qs(parsed.query)
    print('scheme:   %s' % parsed.scheme) 
    print('hostname: %s' % (parsed.hostname or ''))
    print('port:     %s' % (parsed.port or ''))
    print('path:     %s' % parsed.path)
    print('params:   %s' % parsed.params)
    print('fragment: %s' % parsed.fragment)
    print('query:')

    keys = query.keys()
    if keys:
        sorted(keys)
        max_key_len = max([len(key) for key in keys])
        for key in keys:
            value = query[key]
            if len(value) == 1:
                value = value[0]
            print('  %s: %s' % (key.ljust(max_key_len), value))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print >> sys.stderr, 'Usage: %s <url>' % sys.argv[0]
        sys.exit(1)

    pretty_print_url(sys.argv[1])
