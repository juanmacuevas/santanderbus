#!/usr/bin/python
import urllib2
import sys  
#import urllib
from xml.dom.minidom import parse, parseString
# import cPickle



linea = 1
if len(sys.argv)>1:
    linea=sys.argv[1]


url = 'http://www.ayto-santander.es:9001/services/estructura.asmx'

data = """<?xml version="1.0" encoding="utf-8"?>
<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><GetRutasSublinea xmlns="http://tempuri.org/"><label>%s</label><sublinea>1</sublinea></GetRutasSublinea></SOAP-ENV:Body></SOAP-ENV:Envelope>"""%(linea)
#data2 = urllib.urlencode(data)

headers = { 
'Host': 'www.ayto-santander.es:9001',
'Content-Type': 'text/xml; charset=utf-8',
'Content-Length': len(data),
'SOAPAction': 'http://tempuri.org/GetRutasSublinea',
'Accept': '*/*','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding': 'gzip,deflate,sdch',
'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
'Cache-Control': 'no-cache',
'Connection': 'keep-alive',
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
rutas = []
for ir in dom1.getElementsByTagName('InfoRuta'):
	paradas = []	
	nombreRuta =  ir.getElementsByTagName('nombre')[0].childNodes[0].data
	#print nombreRuta
	for ins in ir.getElementsByTagName('InfoNodoSeccion'):
		nodo = ins.getElementsByTagName('nodo')[0].childNodes[0].data
		nombreParada = ins.getElementsByTagName('nombre')[0].childNodes[0].data
		paradas.append([nodo,nombreParada])		
	rutas.append([nombreRuta,paradas])
print rutas



# est = sorted(est)
# print "linea "+str(linea)
# print est



