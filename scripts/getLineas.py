#!/usr/bin/python
import urllib2
import sys  
#import urllib
from xml.dom.minidom import parse, parseString
# import cPickle




url = 'http://www.ayto-santander.es:9001/services/estructura.asmx'

data = """<?xml version="1.0" encoding="utf-8"?>
<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><GetLineasFilter xmlns="http://tempuri.org/"><mask>0</mask></GetLineasFilter></SOAP-ENV:Body></SOAP-ENV:Envelope>"""
#data2 = urllib.urlencode(data)

headers = { 
'Host': 'www.ayto-santander.es:9001',
'Content-Type': 'text/xml; charset=utf-8',
'Content-Length': len(data),
'SOAPAction': 'http://tempuri.org/GetLineasFilter',
'Accept': '*/*','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding': 'gzip,deflate,sdch',
'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
'Cache-Control': 'no-cache',
#'Connection': 'keep-alive',
'DNT': 1,
'Origin': 'http://www.ayto-santander.es:9001',
'Pragma': 'no-cache',
'Referer': 'http://www.ayto-santander.es:9001/lineaestimaciones.swf',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5'
}
req = urllib2.Request(url, data, headers)

response = urllib2.urlopen(req)
the_page = response.read()


dom1 = parseString(the_page)
#print dom1.toprettyxml()
lineas = []
for l in dom1.getElementsByTagName('InfoLinea'):
    lineas.append([l.getElementsByTagName('nombre')[0].childNodes[0].data,
        l.getElementsByTagName('label')[0].childNodes[0].data])

print lineas







# 'Content-Type': 'application/soap+xml; charset=utf-8', 
# 'Accept': '*/*','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
# 'Accept-Encoding': 'gzip,deflate,sdch',
# 'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
# 'Cache-Control': 'no-cache',
# 'Connection': 'keep-alive',
# 'DNT': 1,

# 'Origin': 'http://www.ayto-santander.es:9001',
# 'Pragma': 'no-cache',
# 'Referer': 'http://www.ayto-santander.es:9001/lineaestimaciones.swf',
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
# 'Content-Type': 'text/xml; charset=utf-8',





req = urllib2.Request(url, data, headers)

response = urllib2.urlopen(req)
the_page = response.read()