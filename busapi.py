#!/usr/bin/env python
import urllib2

def requestLineas():
    url = 'http://www.ayto-santander.es:9001/services/estructura.asmx'
    data = '<?xml version="1.0" encoding="utf-8"?><SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><GetLineasFilter xmlns="http://tempuri.org/"><mask>0</mask></GetLineasFilter></SOAP-ENV:Body></SOAP-ENV:Envelope>'
    headers = {'Host': 'www.ayto-santander.es:9001', 'Content-Type': 'text/xml; charset=utf-8', 'Content-Length': len(data), 'SOAPAction': 'http://tempuri.org/GetLineasFilter', 'Accept': '*/*','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'gzip,deflate,sdch', 'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6', 'Cache-Control': 'no-cache', 'DNT': 1, 'Origin': 'http://www.ayto-santander.es:9001', 'Pragma': 'no-cache', 'Referer': 'http://www.ayto-santander.es:9001/lineaestimaciones.swf', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5'}
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    return response.read()