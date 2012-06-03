from suds.client import Client
import cPickle

url = 'http://www.ayto-santander.es:9001/services/estructura.asmx?WSDL'
client = Client(url)
print client

sublineas = []
nodos = {}

#get the list of lines
lineassoap = client.service.GetLineasFilter(0)
for l in lineassoap[0]:   
    for sl in l['sublineas'][0]:
        #print l['label']+','+l['nombre']+','+str(sl['sublinea'])+','+sl['nombre']+'\n'
        sublineas.append({'linea':l['label'],'nl':l['nombre'],'sublinea':sl['sublinea'],'nsl':sl['nombre']})

cPickle.dump(sublineas, open('sublineas.p', 'wb')) 


for i in sublineas:
    #get the list of nodes from a line
    rutassoap = client.service.GetRutasSublinea(i['linea'],i['sublinea'])
    for r in rutassoap[0]:
        #r['nombre']
        for s in r['secciones'][0]:
            for n in s['nodos'][0]:
                nodos[n['nodo']]={'tipo':n['tipo'],'nombre':n['nombre']}
    cPickle.dump(nodos, open('nodos.p', 'wb'))
    print 'added '+i['linea']+','+str(i['sublinea'])



