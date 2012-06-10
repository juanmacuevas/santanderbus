#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import paradas
import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError
import sys  
from xml.dom.minidom import parse, parseString
from time import time
from google.appengine.api import memcache



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.out.write('SantanderBus')
        t1 = time()
        lineas_render = memcache.get("lineas")
        if lineas_render is not None:
                t2 = time()
                tt="<!--"+str(t2-t1)+" -->"
                self.response.out.write(lineas_render+tt)
                return       
        lineas = self.getLineas()
        template_values = {
            'lineas' :   lineas,
        }
        template = jinja_environment.get_template('lineas.html')
        lineas_render = template.render(template_values)
        if not memcache.set("lineas", lineas_render):
                logging.error("Memcache set failed.") 
        t2 =time()
        tt="<!--"+str(t2-t1)+" -->"              
        self.response.out.write(lineas_render+tt)

    def getLineas(self):
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

        return lineas

class StopHandler(webapp2.RequestHandler):
    def get(self,id):
    	# n = self.request.get('n')
        #self.response.out.write("La parada solicitada es "+paradas.nodos[28]['nombre'])
        if not id:
            self.error(404)
            self.response.out.write('<html><head><title>404 Not Found</title> </head> <body>  <h1>404 Not Found</h1>  The resource could not be found.<br /><br /> </body></html>')
            return
        if  not int(id) in paradas.nodos:
            self.error(404)
            self.response.out.write('<html><head><title>404 Not Found</title> </head> <body>  <h1>404 Not Found</h1>  The resource could not be found.<br /><br /> </body></html>')
            return

        t1 = time()
        estimaciones = self.getEstimation(id)
        t2 = time()
        name_stop = paradas.nodos[int(id)]['nombre']
        

        template_values = {
            'id_stop': id ,
            'name_stop': name_stop,
            'estimaciones' :   estimaciones,
            'time': str(t2-t1)[:5]     
        }

        template = jinja_environment.get_template('parada.html')

        self.response.out.write(template.render(template_values))


    def getEstimation(self,parada):

        url = 'http://www.ayto-santander.es:9001/services/dinamica.asmx'

        data = """<?xml version="1.0" encoding="utf-8"?>
        <SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><GetPasoParadaREG xmlns="http://tempuri.org/"><linea>*</linea><parada>%s</parada><medio>3</medio><status>0</status></GetPasoParadaREG></SOAP-ENV:Body></SOAP-ENV:Envelope>"""%(parada)
        #data2 = urllib.urlencode(data)

        headers = { 
        'Host': 'www.ayto-santander.es:9001',
        'Content-Type': 'text/xml; charset=utf-8',
        'Content-Length': len(data),
        'SOAPAction': 'http://tempuri.org/GetPasoParadaREG',
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
        #print dom1.toprettyxml()
        est = []
        for l in dom1.getElementsByTagName('linea'):
            for e in l.parentNode.getElementsByTagName('minutos'):
                minutos = int(e.childNodes[0].data)
                if minutos>=0:
                    est.append([minutos,l.childNodes[0].data])

        est = sorted(est)
        #print "parada "+str(parada)
        return est



class LineHandler(webapp2.RequestHandler):
    def get(self,id):
        # n = self.request.get('n')
        #self.response.out.write("La parada solicitada es "+paradas.nodos[28]['nombre'])

        # if  not int(id) in paradas.nodos:
        #     self.error(404)
        #     self.response.out.write('<html><head><title>404 Not Found</title> </head> <body>  <h1>404 Not Found</h1>  The resource could not be found.<br /><br /> </body></html>')
        #     return
        t1 = time()
        linea_render = memcache.get("linea/"+id)
        if linea_render is not None:
                t2 = time()
                tt="<!--"+str(t2-t1)+" -->"
                self.response.out.write(linea_render+tt)
                return   
        
        rutas = self.getLine(id)
        if  not rutas:
            self.error(404)
            self.response.out.write('<html><head><title>404 Not Found</title> </head> <body>  <h1>404 Not Found</h1>  The resource could not be found.<br /><br /> </body></html>')
            return

        template_values = {
            'rutas':rutas  ,
            'linea' : id 
        }

        template = jinja_environment.get_template('linea.html')
        linea_render = template.render(template_values)
        if not memcache.set("linea/"+id, linea_render):
                logging.error("Memcache set failed.") 
        t2 =time()
        tt="<!--"+str(t2-t1)+" -->"              
        self.response.out.write(linea_render+tt)


    def getLine(self,linea):

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
        try:
                response = urllib2.urlopen(req)
        except HTTPError, e:
                self.error(404)
                self.response.out.write('<html><head><title>404 Not Found</title> </head> <body>  <h1>404 Not Found</h1>  The resource could not be found.<br /><br /> </body></html>')
                return
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
        return rutas



app = webapp2.WSGIApplication([('/parada/(\d*)',StopHandler),('/linea/(.*)', LineHandler),('/', MainHandler)],
                              debug=True)
