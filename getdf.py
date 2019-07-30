#!/usr/bin/env python
 
import sys
import json
import ansible.runner
 
hostlist = [ '10.17.0.189', '10.17.0.188']
 
def gigs(kibs):
    return float(kibs) / 1024.0 / 1024.0
 
runner = ansible.runner.Runner(
    module_name='df',
    module_args='',
    remote_user='root',
    pattern=':'.join(hostlist),
)
 
response = runner.run()
 
 
 
if 'dark' in response:
    if len(response['dark']) > 0:
        print "Contact failures:"
        for host, reason in response['dark'].iteritems():
            print "  %s (%s)" % (host, reason['msg'])
 
total = 0.0
for host, res in response['contacted'].iteritems():
    print host
    for fs in res['space']:
        gb = gigs(fs['available'])
        total += gb
        print "  %-30s %10.2fG" % (fs['mountpoint'], gb)
 
print "Total space over %d hosts: %.2f GB" % (len(response['contacted']), total)
