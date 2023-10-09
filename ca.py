#utf-8
 #<< Harry >> CODE BY Haris akhtar     
''' Orginal Coding Haris akhtar '''

import requests,os
from requests import api
os.system('clear')
xxx = open(api.__file__,'r').read()
if ('print(method,url,kwargs)') in xxx:
    print('[•] Capture Mode is ON\n')
else:
    print('only basics tool M capture')
    print('[•] Capture Mode is OF\n')
print('[1] Capture Mode ON')
print('[2] Capture Mode OF')
select = input(' opt: ')
if select == ('1'):
    x = open(api.__file__,'r').read()
    if ('print(method,url,kwargs)') in x:
        print('[•] Capture Mode is ON\n')
        exit()
    xx = x.replace('def request(method, url, **kwargs):','''def request(method, url, **kwargs):
    print(method,url,kwargs)''')
    open(api.__file__,'w').write(str(xx))
    os.system('python capture.py')
elif select == ('2'):
    x = open(api.__file__,'r').read()
    xx = x.replace('''def request(method, url, **kwargs):
    print(method,url,kwargs)''','def request(method, url, **kwargs):',)
    open(api.__file__,'w').write(xx)
    os.system('python capture.py')
else:
    os.system('python capture.py')