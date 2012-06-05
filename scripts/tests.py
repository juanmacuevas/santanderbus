from suds.client import Client
# import cPickle

url = 'http://www.ayto-santander.es:9001/services/dinamica.asmx?WSDL'
client = Client(url)
print client

estimaciones =  client.service.GetTiposNodosMap()
