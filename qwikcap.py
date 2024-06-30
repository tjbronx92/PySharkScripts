#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyshark

# Quickly capture 50 packets by default

# Define which interface to capture from and output filname
cap = pyshark.LiveCapture(interface="Wi-Fi", output_file="CLI_Capture00")

# Sniff for traffic
cap.sniff(packet_count=50)

# Print capture status
# To print individual packets use packet index and slicing (ex: cap[24])
print(cap)

"""
Created on Sun Jun 30 14:27:30 2024

@author: tj
"""

