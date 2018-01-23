#! /usr/bin/env bash
set -u
set -e
for i in `grep -v '^#' hosts.deny  | grep -v "/" | cut -f2 -d ' '`
do
    output=`geoiplookup $i`
    country_code=`echo $output | cut -c 24-25`
    country=`echo $output | cut -f 5- -d ' '`
    echo $i $country_code $country
done
