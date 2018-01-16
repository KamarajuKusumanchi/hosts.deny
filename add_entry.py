#! /usr/bin/env python3

import sys

import shlex
import subprocess
import re

def subnet_mask(begin_ip_str, end_ip_str):
    nf = 4    # number of fields
    begin_ip = [int(i) for i in begin_ip_str.split('.')[:nf]]
    end_ip = [int(i) for i in end_ip_str.split('.')[:nf]]

    ip_diff = [255 - (end_ip[i] - begin_ip[i]) for i in range(4)]
    mask = '.'.join([str(i) for i in ip_diff])
    return mask

def check_output(command):
    return subprocess.check_output(shlex.split(command), universal_newlines=True).splitlines()

def grep(pattern, lines):
    return [line for line in lines if re.search(pattern, line)]

def grepi(pattern, lines):
    return [line for line in lines if re.search(pattern, line, re.IGNORECASE)]



if __name__ == "__main__":
    begin_ip_str = sys.argv[1]
    end_ip_str = sys.argv[2]
    # print(begin_ip_str)
    # print(end_ip_str)
    mask = subnet_mask(begin_ip_str, end_ip_str)
    print("ALL: " + begin_ip_str + '/' + mask)
