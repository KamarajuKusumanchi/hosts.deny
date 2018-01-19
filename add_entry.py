#! /usr/bin/env python3

import sys

import shlex
import subprocess
import re


def process_input():
    if len(sys.argv) == 3:
        # possible choices are
        # <script_name> ip1 ip2
        begin_ip_str = sys.argv[1]
        end_ip_str = sys.argv[2]
        # print(begin_ip_str)
        # print(end_ip_str)
        mask = subnet_mask(begin_ip_str, end_ip_str)
        result = "ALL: " + begin_ip_str + '/' + mask
    elif len(sys.argv) == 2:
        # possible choices are
        # <script_name> "ip1 - ip2"
        # <script_name> "ip1"
        ip = [i.strip() for i in sys.argv[1].split('-')]
        if len(ip) == 2:
            begin_ip_str = ip[0]
            end_ip_str = ip[1]
            mask = subnet_mask(begin_ip_str, end_ip_str)
            result = "ALL: " + begin_ip_str + '/' + mask
        elif len(ip) == 1:
            result = "ALL: " + ip[0]
    print(result)


def subnet_mask(begin_ip_str, end_ip_str):
    nf = 4    # number of fields
    begin_ip = [int(i) for i in begin_ip_str.split('.')[:nf]]
    end_ip = [int(i) for i in end_ip_str.split('.')[:nf]]

    ip_diff = [255 - (end_ip[i] - begin_ip[i]) for i in range(4)]
    mask = '.'.join([str(i) for i in ip_diff])
    return mask


def check_output(command):
    return subprocess.check_output(shlex.split(command),
                                   universal_newlines=True).splitlines()


def grep(pattern, lines):
    return [line for line in lines if re.search(pattern, line)]


def grepi(pattern, lines):
    return [line for line in lines if re.search(pattern, line, re.IGNORECASE)]


if __name__ == "__main__":
    process_input()
