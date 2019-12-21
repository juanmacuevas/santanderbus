#!/usr/bin/env python
from xml.dom.minidom import parseString

def parseLineas(content,colores):
    xml_doc = parseString(content)
    lineas = []
    for l in xml_doc.getElementsByTagName('InfoLinea'):
        label = l.getElementsByTagName('label')[0].childNodes[0].data
        nombre = l.getElementsByTagName('nombre')[0].childNodes[0].data
        color = colores.get(label,"000000")
        linea = [nombre,label,color]    
        lineas.append(linea)
    return lineas

def parseLinea(content):
    xml_doc = parseString(content)
    rutas = []
    for ir in xml_doc.getElementsByTagName('InfoRuta'):
        paradas = []    
        nombreRuta =  ir.getElementsByTagName('nombre')[0].childNodes[0].data            
        for ins in ir.getElementsByTagName('InfoNodoSeccion'):
            nodo = ins.getElementsByTagName('nodo')[0].childNodes[0].data
            nombreParada = ins.getElementsByTagName('nombre')[0].childNodes[0].data
            paradas.append([nodo,nombreParada])             
        rutas.append([nombreRuta,paradas])
    return rutas

def parseEstimacion(content,colores):
    xml_doc = parseString(content)
    est = []
    for l in xml_doc.getElementsByTagName('linea'):
        for e in l.parentNode.getElementsByTagName('minutos'):
            minutos = int(e.childNodes[0].data)
            if minutos>=0:
                linea =l.childNodes[0].data
                color = colores.get(linea,"000000")
                estimation = [minutos,linea,color]
                est.append(estimation)
    return sorted(est)





