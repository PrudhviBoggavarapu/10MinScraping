from pprint import pprint
import requests
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
file = open('./file.txt', 'a+')
for x in ["%02d" % i for i in range(50)]:
    print(x)
    soup = BeautifulSoup(requests.get(f'http://members.iinet.net.au/~el_buno/GQ/GQ{x}.html').text, features="lxml")
    for y in soup.findAll('li')[1:]:
        thing_to_write = str(y.text.replace('\x97', '-'))+'\n'
        file.write(thing_to_write)
file.close()
