def GetURL():
    print "What URL do you want to read?"
    url = raw_input("")
    try:
        req = urllib2.Request(link, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
        response = urllib2.urlopen(req).read()
    except IOError:
        print "File could not be found."
        GetURL()
    print response;
    GetURL()
def returnURL(url):
    try:
        req = urllib2.Request(link, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
        response = urllib2.urlopen(req).read()
        return response;
    except IOError:
        return null;
print "Initiate System?"
response = raw_input("")
if "YES" in response.upper():
    GetURL()
