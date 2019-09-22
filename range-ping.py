"""
Author:      Harris Chan
Description: For testing all host can response in a range of network.
"""
import subprocess

targetNetwork = input('Target Network (Format: XXX.XXX.XXX): ')
rangeFrom = input('The host from: ')
rangeTo = input('The host to: ')

for ping in range (int(rangeFrom), int(rangeTo)):
    address = targetNetwork + '.' + str(ping)

    print('==============================================')
    responses = subprocess.call(['ping', '-c', '1', address])

    if responses == 0:
        print('Ping to ', address, ': OK')
        print('==============================================\n')
    else:
        print('Ping to ', address, ': Failed')
        print('==============================================\n')
    
