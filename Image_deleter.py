import os

path = '.\downloads'

for address in open('text.txt'):
    address = address[:-1]
    os.remove(path + address)
    print('Removing {}'.format(address))
