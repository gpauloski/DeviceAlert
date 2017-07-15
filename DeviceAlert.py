#import the class
import nmap
import datetime

mac1 = '78:D7:5F:1C:3D:D0'	# S Phone
mac2 = 'A4:5E:60:E9:4D:C9'	# Greg Macbook
mac = mac2

print('Scanning network...')
nm = nmap.PortScanner()
nm.scan(hosts='192.168.1.1/24', arguments='-sP')

print('Searching for', mac, 'on network')
for host in nm.all_hosts():
	if mac in str(nm[host]['addresses']):
		print('Device found at', host, nm[host].hostname(), 'at', str(datetime.datetime.now()))
	#print('----------------------------------------------------')
	#print('Host : %s (%s)' % (host, nm[host].hostname()))
	#print('State : %s' % nm[host].state())
	#print('MAC Address : %s' % nm[host]['addresses'])
