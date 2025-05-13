#! /usr/bin/env python3

# Find files which are very close to MB boundaries for testing
import subprocess
import json
THRESHOLD = 512

vids = [ "VR1863", "VR1871", "VR5775", "VR7029", "VR3028"]

for vid in vids:
    tfLS_output = subprocess.check_output([f"cta-admin --json tf ls --vid {vid}"], shell=True)
    tfLS_dict = json.loads(tfLS_output)
    for tf in tfLS_dict:
        size = int(tf['af']['size'])
        disk_id = tf['df']['diskId']
        f_seq = tf['tf']['fSeq']

        mb = round(size / 1024 / 1024)
        delta = size - mb * 1024 * 1024
        if abs(delta) < THRESHOLD:
            print(f"{vid} {f_seq} {delta} {disk_id}")
