cat hosts.deny | grep -v '^#' | grep -v "/" | cut -f 2 -d ' ' | grep -v '^$' | (
    while read r
    do
        echo $r
        geoiplookup -f ~/.local/share/GeoIP/GeoIP.dat $r
    done
) |& tee junk.txt
