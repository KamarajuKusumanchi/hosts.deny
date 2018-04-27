#! /usr/bin/env bash
set -u
set -e
hosts_deny_file=${1:-~/work/github/hosts.deny/hosts.deny}
out_file=${2:-junk.txt}
echo reading from $hosts_deny_file
for i in `grep -v '^#' $hosts_deny_file  | grep -v "/" | cut -f2 -d ' '`
do
    echo $i
    whois $i | grep -Ei "abuse|range"
    sleep 1
    echo
done > junk.txt 2>&1
echo output stored in $out_file
