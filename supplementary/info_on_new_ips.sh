#! /usr/bin/env bash
cd ~/work/github/hosts.deny
git diff hosts.deny | grep "^+" | grep -v '^++' | cut -f 2 -d ' ' | while read r
do
  echo $r
  geoiplookup $r
  whois $r | grep -Ei "abuse|range"
  echo
done
