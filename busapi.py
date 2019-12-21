#!/usr/bin/env python
import urllib2

def request(url,data,headers):
    req = urllib2.Request(url, data, headers)
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        return ''
    return response.read()

def requestLineas():
    url = 'http://www.ayto-santander.es:9001/services/estructura.asmx'
    data = '<?xml version="1.0" encoding="utf-8"?><SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><GetLineasFilter xmlns="http://tempuri.org/"><mask>0</mask></GetLineasFilter></SOAP-ENV:Body></SOAP-ENV:Envelope>'
    headers = {'Host': 'www.ayto-santander.es:9001', 'Content-Type': 'text/xml; charset=utf-8', 'Content-Length': len(data), 'SOAPAction': 'http://tempuri.org/GetLineasFilter', 'Accept': '*/*','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'gzip,deflate,sdch', 'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6', 'Cache-Control': 'no-cache', 'DNT': 1, 'Origin': 'http://www.ayto-santander.es:9001', 'Pragma': 'no-cache', 'Referer': 'http://www.ayto-santander.es:9001/lineaestimaciones.swf', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5'}
    return request(url,data,headers)

def requestLinea(linea):
    url = 'http://www.ayto-santander.es:9001/services/estructura.asmx'
    data = '<?xml version="1.0" encoding="utf-8"?><SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><GetRutasSublinea xmlns="http://tempuri.org/"><label>%s</label><sublinea>1</sublinea></GetRutasSublinea></SOAP-ENV:Body></SOAP-ENV:Envelope>'%(linea)
    headers = { 'Host': 'www.ayto-santander.es:9001', 'Content-Type': 'text/xml; charset=utf-8', 'Content-Length': len(data), 'SOAPAction': 'http://tempuri.org/GetRutasSublinea', 'Accept': '*/*','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'gzip,deflate,sdch', 'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'DNT': 1, 'Origin': 'http://www.ayto-santander.es:9001', 'Pragma': 'no-cache', 'Referer': 'http://www.ayto-santander.es:9001/lineaestimaciones.swf', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5' }
    return request(url,data,headers)

def requestEstimacion(parada):
    url = 'http://www.ayto-santander.es:9001/services/dinamica.asmx'
    data = '<?xml version="1.0" encoding="utf-8"?><SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><GetPasoParadaREG xmlns="http://tempuri.org/"><linea>*</linea><parada>%s</parada><medio>3</medio><status>0</status></GetPasoParadaREG></SOAP-ENV:Body></SOAP-ENV:Envelope>'%(parada)
    headers = { 'Host': 'www.ayto-santander.es:9001', 'Content-Type': 'text/xml; charset=utf-8', 'Content-Length': len(data), 'SOAPAction': 'http://tempuri.org/GetPasoParadaREG', 'Accept': '*/*','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'gzip,deflate,sdch', 'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'DNT': 1, 'Origin': 'http://www.ayto-santander.es:9001', 'Pragma': 'no-cache', 'Referer': 'http://www.ayto-santander.es:9001/lineaestimaciones.swf', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5' }
    return request(url,data,headers)