from tadVenta import *
def crearAgencia():
    agencia=[]
    return agencia

def agregarVenta(agencia, v):
    agencia.append(v)

def eliminarVenta(agencia, v):
    agencia.removeagencia(v)

def recuperarVenta(agencia, i):
    return agencia[i]

def tamanio(agencia):
    return len(agencia)

def existeVenta(agencia, v):
    return  v in agencia
