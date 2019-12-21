#!/usr/bin/env python
import webapp2
import jinja2
import os
import paradas
import busapi
import xmlparser
from google.appengine.api import memcache

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        lineas_render = memcache.get("lineas")
        if lineas_render is not None:
            self.response.out.write(lineas_render)
            return
        content = busapi.requestLineas()
        lineas = xmlparser.parseLineas(content,paradas.colores)
        template_values = {'lineas' :   lineas,}
        template = jinja_environment.get_template('lineas.html')
        lineas_render = template.render(template_values)
        if not memcache.set("lineas", lineas_render):
            logging.error("Memcache set failed.") 
        self.response.out.write(lineas_render)


class StopHandler(webapp2.RequestHandler):
    def get(self,id):
        if not id or not int(id) in paradas.nodos:
            showError(self)  
            return
        content = busapi.requestEstimacion(id)
        estimaciones = xmlparser.parseEstimacion(content,paradas.colores)
        name_stop = paradas.nodos[int(id)]['nombre']
        template_values = {
            'id_stop': id ,
            'name_stop': name_stop,
            'estimaciones' : estimaciones,
            'time': ''     
        }
        template = jinja_environment.get_template('parada.html')
        self.response.out.write(template.render(template_values))


class LineHandler(webapp2.RequestHandler):
    def get(self,id):
        linea_render = memcache.get("linea/"+id)
        if linea_render is not None:
                self.response.out.write(linea_render)
                return
        content = busapi.requestLinea(id)
        if not content:
            showError(self)
            return
        rutas = xmlparser.parseLinea(content)
        if  not rutas:
            showError(self)
            return
        template_values = {'rutas':rutas, 'linea' : id }
        template = jinja_environment.get_template('linea.html')
        linea_render = template.render(template_values)
        if not memcache.set("linea/"+id, linea_render):
                logging.error("Memcache set failed.") 
        self.response.out.write(linea_render)

def showError(handler):
    handler.error(404)
    handler.response.out.write('<html><head><title>404 Not Found</title> </head> <body>  <h1>404 Not Found</h1>  The resource could not be found.<br /><br /> </body></html>')

app = webapp2.WSGIApplication([('/parada/(\d*)',StopHandler),('/linea/(.*)', LineHandler),('/', MainHandler)],
                              debug=True)
