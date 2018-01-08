The hosts.deny file contains a list of IP addresses that are not allowed to access any of my machines.

An IP address is added to this list when I detect any unsolicited activity such as brute-force ssh login attempts.

In some cases, I add an IP address range instead of a single IP address. This range is obtained from the abuse contact information listed in the whois record.

For example, on 2018-01-06, I noticed that there were many brute-force ssh login attempts from 120.205.199.218 into one of my machines. This IP address is owned by China Mobile. However, I do not expect anyone from China Mobile to connect to any of my machines. So I decided to block the entire IP range  120.192.0.0 - 120.255.255.255. This range is obtained from

<pre>
$ whois 120.205.199.218 | grep abuse
% Abuse contact for '120.192.0.0 - 120.255.255.255' is 'abuse@chinamobile.com'
...
</pre>

The syntax to block a range of hosts is starting_ip/subnet_mask . The subnet mask can be obtained by 255.255.255.255 - (ending_ip - starting_ip) with the subtraction done on individual fields.

So the subnet for all hosts in 120.192.0.0 - 120.255.255.255 is 255.255.255.255 - (120.255.255.255 - 120.192.0.0) = 255.255.255.255 - (0.(255-192).255.255) = 255.(255-(255-192)).0.0 = 255.192.0.0

So the corresponding entry in the hosts.deny file would be 120.192.0.0/255.192.0.0
