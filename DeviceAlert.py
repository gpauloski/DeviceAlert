# Scans network for device with certain MAC address
# Triggers IFTTT webhook if device found
# Designed for use in home automation applications

#import the class
import nmap
import datetime
import time
import requests

# Variables for IFTTT webhook
iftttTrigger = 'xxx'
iftttKey = 'xxx'

# Mac address to search network for
mac = '00:00:00:00:00:00'

while True:
	# Run scan on network using nmap
	# Set IP to IP of router
	print('\nScanning network for', mac)
	nm = nmap.PortScanner()
	nm.scan(hosts='192.168.1.1/24', arguments='-sP')

	# Checks to see if mac address found in list of devices returned my nmap
	for host in nm.all_hosts():
		if mac in str(nm[host]['addresses']):
			print('Device found at', host, nm[host].hostname(), 'at', str(datetime.datetime.now()))
			
			# Create report to send with IFTTT notification
			# Values can be used within IFTTT applet for additional functions
			report = { 'value1' : host, 'value2' : nm[host].hostname() }
			
			# Trigger webhook and send report
			requests.post("https://maker.ifttt.com/trigger/" + iftttTrigger + "/with/key/" + iftttKey, data=report)
			print("IFTTT notification sent")
			
			# If device found, pause script for 1 hour
			# Prevents IFTTT notifications being spammed
			time.sleep(60*60)
	
	# Pause before scanning network again
	time.sleep(60)
			