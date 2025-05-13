#! /usr/bin/env python3

# Find files which are very close to MB boundaries for testing
import subprocess
import json
THRESHOLD = 300

vids = [ "VR1863", "VR1871", "VR5775", "VR7029" ]

for vid in vids:
    tfLS_output = subprocess.check_output([f"cta-admin --json tf ls --vid {vid}"], shell=True)
    tfLS_dict = json.loads(tfLS_output)
    for tf in tfLS_dict:
        size = int(tf['af']['size'])
        disk_id = tf['df']['diskId']
        f_seq = tf['tf']['fSeq']

        delta = abs(size % (1024*1024))
        if delta < THRESHOLD:
            print(f"{vid} {f_seq} {delta} {disk_id}")
            
