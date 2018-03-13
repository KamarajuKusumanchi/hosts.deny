#! /usr/bin/env bash
set -u
set -e
for i in `grep -v '^#' hosts.deny  | grep -v "/" | cut -f2 -d ' '`
do
    echo $i
    whois $i | grep -i abuse
    sleep 1
    echo
done > junk.txt 2>&1
