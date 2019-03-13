#!/usr/bin/python
import sys,os,pwd,syslog
syslog.syslog(syslog.LOG_INFO, ' '.join('{!r}'.format(w) for w in sys.argv))
os.environ['SHELL'] = '/bin/bash'
sudo = '/usr/bin/sudo'
common = [ 'sudo', '-E', '-u', pwd.getpwuid(os.getuid())[0], os.environ['SHELL'] ]
if len(sys.argv) < 2:
    # SSH(1): ssh connects and logs into the specified hostname
    args = common + [ '-l' ]
else:
    # SSH(1): If command is specified, it is executed on the remote host instead of a login shell
    args = common + sys.argv[1:] # ssh invoked us as $0 -c
os.execve(sudo, args, os.environ)
