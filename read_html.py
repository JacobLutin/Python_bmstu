import httplib
httplib.HTTPConnection.debuglevel = 1

import urllib

url_path = 'http://vk.com'
feeddata = urllib.urlopen(url_path).read()
print data
