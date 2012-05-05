#!/usr/bin/env python

# requires python 2.7

# make installer
# http://docs.python.org/distutils/introduction.html

import sys
from urlparse import urlparse, parse_qs

def pretty_print_url(url_string):
    """pretty print an url to stdout"""
    parsed = urlparse(url_string)
    query = parse_qs(parsed.query)
    print 'scheme:   %s' % parsed.scheme
    print 'hostname: %s' % (parsed.hostname or '')
    print 'port:     %s' % (parsed.port or '')
    print 'path:     %s' % parsed.path
    print 'params:   %s' % parsed.params
    print 'fragment: %s' % parsed.fragment
    print 'query:'

    keys = query.keys()
    if keys:
        keys.sort()
        max_key_len = max([len(key) for key in keys])
        for key in keys:
            value = query[key]
            if len(value) is 1:
                value = value[0]
            print '  %s: %s' % (key.ljust(max_key_len), value)

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print >> sys.stderr, 'Usage: %s <url>' % sys.argv[0]
        sys.exit(1)

    pretty_print_url(sys.argv[1])
