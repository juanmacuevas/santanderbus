from suds.client import Client
# import cPickle

url = 'http://www.ayto-santander.es:9001/services/dinamica.asmx?WSDL'
client = Client(url)
print client

estimaciones =  client.service.GetPasoParadaREG("*", 28, 3,0 )

for l in estimaciones[0][0]:
    for e in l:
    # print l['linea']
        print e[1][0]

{
   GetPasoParadaREGResult = 
      (ArrayOfPasoParada){
         PasoParada[] = 
            (PasoParada){
               cabecera = False
               e1 = 
                  (e1){
                     minutos = 5
                     metros = 1592
                     tipo = "Normal"
                  }
               e2 = 
                  (e2){
                     minutos = 23
                     metros = 5369
                     tipo = "Normal"
                  }
               linea = "1"
               parada = "28"
               ruta = "ADARZO"
               sublinea = "3"
            },
            (PasoParada){
               cabecera = False
               e1 = 
                  (e1){
                     minutos = 11
                     metros = 2701
                     tipo = "Normal"
                  }
               e2 = 



Methods (15):
            GetAcciones(xs:int macro, xs:int linea, xs:int coche, xs:int vehiculo, )
            GetCoches(xs:string linea, )
            GetEvents(xs:string linea, xs:int sec, xs:int parada, )
            GetInfoActividades(xs:string svcbus, xs:string svccond, xs:int cond, )
            GetInfoVehiculo(xs:string linea, xs:int coche, xs:int vehiculo, )
            GetLastError()
            GetPasoParada(xs:string linea, xs:string parada, xs:int status, )
            GetPasoParadaREG(xs:string linea, xs:string parada, xs:int medio, xs:int status, )
            GetStatusLinea(xs:string linea, )
            GetStatusLineas(ArrayOfString lineas, )
            GetVehiculos(xs:string linea, )
            XGetCoches(xs:string pass, xs:string linea, )
            XGetPasoParada(xs:string pass, xs:string linea, xs:string parada, xs:int status, )
            XGetPasoParadaREG(xs:string pass, xs:string linea, xs:string parada, xs:int medio, xs:int status, )
            XGetVehiculos(xs:string pass, xs:string linea, )
         Types (19):
            ActividadesInfo
            ArrayOfActividadesInfo
            ArrayOfInfoAccion
            ArrayOfInfoCoche
            ArrayOfInfoHeaderEvent
            ArrayOfInfoVehiculo
            ArrayOfLineStatusInfo
            ArrayOfPasoParada
            ArrayOfString
            Estimacion
            InfoCoche
            InfoHeaderEvent
            InfoPosicion
            InfoSeparacion
            InfoVehiculo
            LineStatusInfo
            PasoParada
            infoAccion
            infoVehiculoExt
      (DinamicaSoap12)
         Methods (15):
            GetAcciones(xs:int macro, xs:int linea, xs:int coche, xs:int vehiculo, )
            GetCoches(xs:string linea, )
            GetEvents(xs:string linea, xs:int sec, xs:int parada, )
            GetInfoActividades(xs:string svcbus, xs:string svccond, xs:int cond, )
            GetInfoVehiculo(xs:string linea, xs:int coche, xs:int vehiculo, )
            GetLastError()
            GetPasoParada(xs:string linea, xs:string parada, xs:int status, )
            GetPasoParadaREG(xs:string linea, xs:string parada, xs:int medio, xs:int status, )
            GetStatusLinea(xs:string linea, )
            GetStatusLineas(ArrayOfString lineas, )
            GetVehiculos(xs:string linea, )
            XGetCoches(xs:string pass, xs:string linea, )
            XGetPasoParada(xs:string pass, xs:string linea, xs:string parada, xs:int status, )
            XGetPasoParadaREG(xs:string pass, xs:string linea, xs:string parada, xs:int medio, xs:int status, )
            XGetVehiculos(xs:string pass, xs:string linea, )
         Types (19):
            ActividadesInfo
            ArrayOfActividadesInfo
            ArrayOfInfoAccion
            ArrayOfInfoCoche
            ArrayOfInfoHeaderEvent
            ArrayOfInfoVehiculo
            ArrayOfLineStatusInfo
            ArrayOfPasoParada
            ArrayOfString
            Estimacion
            InfoCoche
            InfoHeaderEvent
            InfoPosicion
            InfoSeparacion
            InfoVehiculo
            LineStatusInfo
            PasoParada
            infoAccion
            infoVehiculoExt
