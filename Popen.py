#!/usr/bin/python

from  subprocess import *
p = Popen(["ping", "192.168.1.1"], bufsize=32,stdin=PIPE,stdout=PIPE, close_fds=True)
(fin, fout) =  (p.stdin, p.stdout)                                                 
for i in xrange(1000000):            
    # fin.write('\n')
    # fin.flush()
    print fout.readline(),