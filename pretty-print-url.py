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

    query_keys = [len(key) for key in query.keys()]
    if query_keys:
        max_key_len = max(query_keys)
        for k, v in query.items():
            if len(v) is 1:
                v = v[0]
            print '  %s: %s' % (k.ljust(max_key_len), v)

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print >> sys.stderr, 'Usage: %s <url>' % sys.argv[0]
        sys.exit(1)

    pretty_print_url(sys.argv[1])
