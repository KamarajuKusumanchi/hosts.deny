#! /usr/bin/env bash

# set -x

src_dir=${1:-~/work/github/hosts.deny}

echo checking in $src_dir
cd $src_dir
git diff hosts.deny | grep "^+" | grep -v '^++' | cut -f 2 -d ' ' | while read r
do
  echo $r
  grep $r ~/x/ipsum.txt_RK_*
  echo
  geoiplookup -f ~/data/geoiplookup/GeoIP.dat $r
  whois $r | grep -Ei "abuse|range"
  echo
done
