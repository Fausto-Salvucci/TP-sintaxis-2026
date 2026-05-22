
#================================= SE CAMBIAAAA ===============================

# =============================================================================
# TAD COLA (Necesario para el Inciso 6)
# =============================================================================
# Se requiere para generar la "Cola de Operador" solicitada 
def crearCola():
    return []

def encolar(cola, elemento):
    cola.append(elemento)

def desencolar(cola):
    return cola.pop(0)

def es_vacia(cola):
    return len(cola) == 0

# =============================================================================
# LÓGICA DE NEGOCIO (Incisos 5 y 6)
# =============================================================================

def inciso_5_depuracion(agencia):
    """Elimina ventas del último mes de un tipo de actividad específico [cite: 17]"""
    tipo_a_borrar = input("Ingrese Tipo de Actividad para depurar: ")
    hoy = datetime.datetime.now()
    
    for i in range(tamanio(agencia)):
        v = recuperarAgencia(agencia, i)
        f_venta = datetime.datetime.strptime(verFecha(v), "%Y-%m-%d")
        diferencia_dias = (hoy - f_venta).days
        
        # Si NO cumple ambas condiciones (mismo tipo Y < 30 días), se mantiene
        if not (verTipo(v) == tipo_a_borrar and diferencia_dias <= 30):
            agregarVentas(nueva_agencia, v)
    
    print("Depuración completada.")
    return nueva_agencia





# ============================SE QUEDAAAA======================================= 
def inciso_6_operador_y_caja(agencia):
    """Genera cola por operador y realiza corte de caja diario [cite: 19, 20]"""
    # 6.1 Cola de Operador
    op_buscado = input("Ingrese nombre del Operador para generar la Cola: ")
    cola_op = crearCola()
    
    for i in range(tamanio(agencia)):
        v = recuperarAgencia(agencia, i)
        if verOperador(v) == op_buscado:
            # Encolar Nombre, Tipo y Fecha 
            encolar(cola_op, [verNombre(v), verTipo(v), verFecha(v)])
    
    print(f"\n--- Cola del Operador: {op_buscado} ---")
    while not es_vacia(cola_op):
        datos = desencolar(cola_op)
        print(f"Servicio: {datos[0]} | Actividad: {datos[1]} | Fecha: {datos[2]}")

    # 6.2 Corte de Caja Parcial
    hora_corte = input("\nIngrese hora para corte de caja (HH:MM): ")
    fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d")
    monto_total = 0
    cantidad = 0
    
    for i in range(tamanio(agencia)):
        v = recuperarAgencia(agencia, i)
        # Filtramos por fecha actual y hora límite [cite: 20]
        if verFecha(v) == fecha_hoy and verHora(v) <= hora_corte:
            monto_total += verImporte(v)
            cantidad += 1
            
    print(f"--- Corte de Caja ({fecha_hoy}) ---")
    print(f"Cantidad vendida: {cantidad}")
    print(f"Total recaudado: ${monto_total}")
