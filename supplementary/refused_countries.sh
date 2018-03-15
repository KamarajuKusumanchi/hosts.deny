outfile=bad_countries.txt_`date +'%Y%m%d_%H%M%S'`
cat /var/log/auth.log | grep -Eo 'sshd\[[0-9]{1,}\]:.refused connect from ([0-9]{,3}\.?)*' | sed "s/^.*refused connect from //g" | uniq | {
while read r
do
    geoiplookup $r
done
} | sort | uniq | cut -c 24-25 | sort | uniq | grep -vE "IN|US" > $outfile
echo output stored in $outfile
