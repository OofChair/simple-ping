#! /usr/bin/env python3
'''
Ping package

Usage (from shell):
    $ python -m ping

API:
    from ping import Ping

    ping_once = Ping('localhost')
    print(ping_once.avg)
    print(ping_once.avg)

    ping_more = Ping()
    ping_more.ping('localhost')
    print(ping_more.avg)
    ping_more.ping('google.com')
    print(ping_more.avg)
'''

from subprocess import run
import re


class Ping:
    '''The class Ping'''
    def __init__(self, host=None, count=3) -> None:
        '''Initiate the class Ping'''
        self.returncode = None
        self.stderr = None
        self.min = None
        self.avg = None
        self.max = None
        self.jitter = None

        if host: self.ping(host, count)
    def ping(self, host, count=3) -> None:
        '''
        Run ping

        Arguments:
            host (str): Hostname or IP address to be pinged
            count (int, optional): Number of pings to run (default: 3)

        Attributes:
            returncode (int): OS error return code
            stderr (str): OS error message
            min (float): Lowest ping response, in ms
            avg (float): Average ping response, in ms
            max (float): Highest ping response, in ms
            jitter (float): Average of deviation
        '''
        assert isinstance(count, int), f'count arg is {type(count)}, not int'
        assert len(host) > 0, f'host arg must be a valid hostname or IP'

        cmd = [ 'ping', '-q', '-n', '-c', str(count), host ]
        res = run(cmd, capture_output=True)
        self.returncode = res.returncode

        if res.returncode > 0:
            self.stderr = res.stderr.decode().rstrip('\n')
            return None

        for line in res.stdout.decode().split('\n'):
            if 'avg' in line:
                s = re.search('.* = ([0-9\.]+)/([0-9\.]+)/([0-9\.]+)/([0-9\.])+ ms.*', line)

                self.min = s.group(0)
                self.avg = s.group(1)
                self.max = s.group(2)
                self.jitter = s.group(3)

