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
    sub = {'E31': 1, 'LC': 1, '20': 1, '21': 1, '23': 1, '1': 1, '3': 3, '2': 1, '4': 1, 'E4': 1, 'E7': 1, 'E1': 1, 'E3': 1, 'E2': 1, '7C1': 1, '7C2': 1, '99': 1, '6C1': 1, '6C2': 1, '17': 1, 'N1': 1, 'N2': 1, 'N3': 2, '14': 2, '11': 1, '13': 1, '12': 1, '15': 1, '5C2': 2, '5C1': 2, '16': 1, '19': 1, '18': 3}
    url = 'http://www.ayto-santander.es:9001/services/estructura.asmx'
    data = '<?xml version="1.0" encoding="utf-8"?><SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><GetRutasSublinea xmlns="http://tempuri.org/"><label>%s</label><sublinea>%s</sublinea></GetRutasSublinea></SOAP-ENV:Body></SOAP-ENV:Envelope>'%(linea,sub[linea])
    headers = { 'Host': 'www.ayto-santander.es:9001', 'Content-Type': 'text/xml; charset=utf-8', 'Content-Length': len(data), 'SOAPAction': 'http://tempuri.org/GetRutasSublinea', 'Accept': '*/*','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'gzip,deflate,sdch', 'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'DNT': 1, 'Origin': 'http://www.ayto-santander.es:9001', 'Pragma': 'no-cache', 'Referer': 'http://www.ayto-santander.es:9001/lineaestimaciones.swf', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5' }
    return request(url,data,headers)

def requestEstimacion(parada):
    url = 'http://www.ayto-santander.es:9001/services/dinamica.asmx'
    data = '<?xml version="1.0" encoding="utf-8"?><SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><GetPasoParadaREG xmlns="http://tempuri.org/"><linea>*</linea><parada>%s</parada><medio>3</medio><status>0</status></GetPasoParadaREG></SOAP-ENV:Body></SOAP-ENV:Envelope>'%(parada)
    headers = { 'Host': 'www.ayto-santander.es:9001', 'Content-Type': 'text/xml; charset=utf-8', 'Content-Length': len(data), 'SOAPAction': 'http://tempuri.org/GetPasoParadaREG', 'Accept': '*/*','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'gzip,deflate,sdch', 'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'DNT': 1, 'Origin': 'http://www.ayto-santander.es:9001', 'Pragma': 'no-cache', 'Referer': 'http://www.ayto-santander.es:9001/lineaestimaciones.swf', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5' }
    return request(url,data,headers)