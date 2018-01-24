sudo cp hosts.allow /etc/hosts.allow
sudo cp hosts.deny /etc/hosts.deny
sudo mkdir -p /usr/local/bin/sshfilter
sudo cp sshfilter.py config.ini config.py /usr/local/bin/sshfilter
