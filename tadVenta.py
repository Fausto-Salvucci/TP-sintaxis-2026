#venta = [0,"",0,"","",0,0,0]
    #codigo, nombre, tipo actividad, operador, plan pago, importe, fecha venta, hora venta

def crearVenta():
    venta = [0,"",0,"","",0,0,0]
    return venta

def cargarVenta(codigo, nombre, tipoActividad, operador, planPago, importe, fechaVenta, horaVenta):
    venta[0]=codigo
    venta[1]=nombre
    venta[2]=tipoActividad
    venta[3]=operador
    venta[4]=planPago
    venta[5]=importe
    venta[6]=fechaVenta
    venta[7]=horaVenta

def asignarVenta(venta1,venta2):
    venta2[0]=venta1[0]
    venta2[1]=venta1[1]
    venta2[2]=venta1[2]
    venta2[3]=venta1[3]
    venta2[4]=venta1[4]
    venta2[5]=venta1[5]
    venta2[6]=venta1[6]
    venta2[7]=venta1[7]
    
    
def verCodigo(venta):
    return venta[0]

def verNombre(venta):
    return venta[1]

def verTipo(venta):
    return venta[2]

def verOperador(venta):
    return venta[3]

def verPlan(venta):
    return venta[4]

def verImporte(venta):
    return venta[5]

def verFecha(venta):
    return venta[6]

def verHora(venta):
    return venta[7]


def modCodigo(venta, nuevoCod):
    venta[0] = nuevoCod

def modNombre(venta, nuevoNom):
    venta[1] = nuevoNom


def modTipo(venta, nuevoTipo):
    venta[2] = nuevoTipo

def modOperador(venta, nuevoOpe):
    venta[3] = nuevoOpe

def modPlan(venta, nuevoPlan):
    venta[4] = nuevoPlan

def moImporte(venta, nuevoImporte):
    venta[5] = nuevoImporte

def modFecha(venta, nuevaFecha):
    venta[6] = nuevaFecha

def modHora(venta, nuevaHora):
    venta[7]= nuevaHora