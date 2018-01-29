#! /usr/bin/env python3

import argparse
import sys

import shlex
import subprocess
import re

from config import Config


def check_output(command):
    return subprocess.check_output(shlex.split(command),
                                   universal_newlines=True).splitlines()


def get_country(ip):
    output = check_output('geoiplookup ' + ip)[0]
    regex = re.compile("GeoIP Country Edition: (\w+), ")
    country = regex.findall(output)[0]
    return country


def deny(ip):
    country = get_country(ip)
    return country in Config['COUNTRIES']['DENY']


def allow(ip):
    country = get_country(ip)
    return country in Config['COUNTRIES']['ALLOW']


def parse_arguments(args):
    parser = argparse.ArgumentParser(
        description='ssh access filter')
    parser.add_argument("access", action='store',
                        choices=['allow', 'deny'], help='type of access')
    parser.add_argument("ip", action='store', help='ip address')

    res = parser.parse_args(args)
    return res


def process_arguments(args):
    # print(args)
    # print(Config['COUNTRIES']['DENY'].split(' '))
    # print(Config['COUNTRIES']['ALLOW'].split(' '))
    #
    # for ip in ['218.87.109.152', '223.206.125.118', '8.8.8.8']:
    #     print(get_country(ip))
    #     print(deny(ip))
    #     print(allow(ip))
    access = args.access
    ip = args.ip
    if access == 'allow':
        if allow(ip):
            sys.exit(0)
        else:
            sys.exit(1)
    if access == 'deny':
        if deny(ip):
            sys.exit(0)
        else:
            sys.exit(1)


if __name__ == "__main__":
    args = parse_arguments(sys.argv[1:])
    process_arguments(args)
