#!/usr/bin/env python
from xml.dom.minidom import parse, parseString

def parseLineas(doc,colores):        
    xml_doc = parseString(doc)
    lineas = []
    for l in xml_doc.getElementsByTagName('InfoLinea'):
            lin = l.getElementsByTagName('label')[0].childNodes[0].data
            lineas.append([l.getElementsByTagName('nombre')[0].childNodes[0].data,
            lin,colores.get(lin,"000000")])
    return lineas