The idea here is to block ssh connections from unauthorized machines by using multiple layers of defense mechanisms.

The first layer of defense is to explicitly list the IP addresses in hosts.allow and hosts.deny files. An IP address in hosts.allow is always allowed to connect and an IP address in hosts.deny is always blocked. Sample entries in either file will be:

<pre>
ALL: <ip address 1>
ALL: <ip address 2>
</pre>

For example

<pre>
ALL: 34.195.172.30
</pre>

We can also allow/block an IP address range instead of a single IP address. This range can be obtained from the abuse contact information listed in the whois record.

For example, I noticed that there were many brute-force ssh login attempts from 120.205.199.218 into one of my machines on 2018-01-06. This IP address is owned by China Mobile. However, I do not expect anyone from China Mobile to connect to any of my machines. So I decided to block the entire IP range  120.192.0.0 - 120.255.255.255. This range was obtained from

<pre>
$ whois 120.205.199.218 | grep abuse
% Abuse contact for '120.192.0.0 - 120.255.255.255' is 'abuse@chinamobile.com'
...
</pre>

The syntax to block a range of hosts is starting_ip/subnet_mask . The subnet mask can be obtained by 255.255.255.255 - (ending_ip - starting_ip) with the subtraction done on individual fields.

So the subnet mask of the IP range 120.192.0.0 - 120.255.255.255 is 255.255.255.255 - (120.255.255.255 - 120.192.0.0) = 255.255.255.255 - (0.(255-192).255.255) = 255.(255-(255-192)).0.0 = 255.192.0.0

The corresponding entry in the hosts.deny file would be 

<pre>
ALL: 120.192.0.0/255.192.0.0
</pre>

The second layer of defense is based on the country of the IP address. We can either allow or deny ssh connections from IP address belonging to a prespecified set of countries.

To allow/block certain countries add them to the ALLOW/DENY variables in the COUNTRIES section of the config.ini file. Then call sshfilter.py in hosts.allow/hosts.deny files. For example

<pre>
$ cat config.ini
...
[COUNTRIES]
DENY = CN RU
ALLOW = IN US
...

$ cat hosts.allow
...
sshd: ALL: aclexec /usr/local/bin/sshfilter/sshfilter.py allow %a
...

$ cat hosts.deny
...
sshd: ALL: aclexec /usr/local/bin/sshfilter/sshfilter.py deny %a
...
</pre>

will allow connections from IP addresses in India and USA, block connections from Russia and China.


The third and final layer of defense is to check if the IP address is blacklisted. The list of bad IPs are read from the black_list_file variable in the DEFAULT section of config.ini . The default is set to a local copy of the level 2 file provided by the ipsum project <fill the exact location later>. I have a cron job that updates this file on a regular basis. This ensures that I am always comparing against the latest set of bad boys.


