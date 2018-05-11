#! /usr/bin/env bash

# set -x

src_dir=${1:-~/work/github/hosts.deny}

echo checking in $src_dir
cd $src_dir
git diff hosts.deny | grep "^+" | grep -v '^++' | cut -f 2 -d ' ' | while read r
do
  echo $r
  geoiplookup $r
  whois $r | grep -Ei "abuse|range"
  echo
done
