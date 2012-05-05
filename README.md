pretty-print-url
================

Command line tool to pretty print urls.

Example
=======

When you type:

    $ pretty-print-url.py "http://maps.google.com/maps?saddr=Jack+London+Square,+Oakland,+CA&daddr=downtown,+sf&hl=en&sll=37.797034,-122.346153&sspn=0.281598,0.288391&geocode=FZOyQAIdHzW2-CFarnWbBB33kQ%3BFVJmQAIdKAe0-CkhAGkAbZqFgDH_rXbwZxNQSg&oq=jack+lon&mra=ls&t=m&z=12"

You will be shown:

	scheme:   http
	hostname: maps.google.com
	port:     
	path:     /maps
	params:   
	fragment: 
	query:
	  sspn   : 0.281598,0.288391
	  sll    : 37.797034,-122.346153
	  daddr  : downtown, sf
	  geocode: FZOyQAIdHzW2-CFarnWbBB33kQ;FVJmQAIdKAe0-CkhAGkAbZqFgDH_rXbwZxNQSg
	  t      : m
	  hl     : en
	  saddr  : Jack London Square, Oakland, CA
	  z      : 12
	  mra    : ls
	  oq     : jack lon
