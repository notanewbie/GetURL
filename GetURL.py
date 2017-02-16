def GetURL():
    print "What URL do you want to read?"
    url = raw_input("")
    try:
        File = file_object  = open(url, "r")
    except IOError:
        print "File could not be found."
        GetURL()
    print File;
    GetURL()
print "Initiate System?"
print
response = raw_input("")
if "YES" in response.upper():
    GetURL()
