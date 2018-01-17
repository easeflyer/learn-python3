import os

try:
    from httplib import HTTPConnection # Python 2
except ImportError:
    from http.client import HTTPConnection # Python 3

BOUNDARY = "$Python-Essential-Reference$"
CRLF = '\r\n'

def upload(addr, url, formfields, filefields):
    # Create the sections for form fields
    formsections = []
    for name in formfields:
        section = [
            '--'+BOUNDARY,
            'Content-disposition: form-data; name="%s"' % name,
            '',
            formfields[name]
            ]
formsections.append(CRLF.join(section)+CRLF)
# Collect information about all of the files to be uploaded
fileinfo = [(os.path.getsize(filename), formname, filename)
for formname, filename in filefields.items()]
# Create the HTTP headers for each file
filebytes = 0
fileheaders = []
for filesize, formname,filename in fileinfo:
headers = [
'--'+BOUNDARY,
'Content-Disposition: form-data; name="%s"; filename="%s"' % \
(formname, filename),
'Content-length: %d' % filesize,
''
]
fileheaders.append(CRLF.join(headers)+CRLF)
filebytes += filesize
# Closing marker
closing = "--"+BOUNDARY+"--\r\n"
# Determine the entire length of the request
content_size = (sum(len(f) for f in formsections) +
sum(len(f) for f in fileheaders) +
filebytes+len(closing))
# Upload it
conn = HTTPConnection(*addr)
conn.putrequest("POST",url)
conn.putheader("Content-type", 'multipart/form-data; boundary=%s' % BOUNDARY)
conn.putheader("Content-length", str(content_size))
conn.endheaders()

# Send all form sections
for s in formsections:
conn.send(s.encode('latin-1'))
# Send all files
for head,filename in zip(fileheaders,filefields.values()):
conn.send(head.encode('latin-1'))
f = open(filename,"rb")
while True:
chunk = f.read(16384)
if not chunk: break
conn.send(chunk)
f.close()
conn.send(closing.encode('latin-1'))
r = conn.getresponse()
responsedata = r.read()
conn.close()
return responsedata
# Sample: Upload some files. The form fields 'name', 'email'
# 'file_1','file_2', and so forth are what the remote server
# is expecting (obviously this will vary).
server = ('localhost', 8080)
url = '/cgi-bin/upload.py'
formfields = {
'name' : 'Dave',
'email' : 'dave@dabeaz.com'
}
filefields = {
'file_1' : 'IMG_1008.JPG',
'file_2' : 'IMG_1757.JPG'
}
resp = upload(server, url,formfields,filefields)
print(resp)