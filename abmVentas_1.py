from tadAgencia import *
from tadVenta import *
from datetime import date, time

# ─────────────────────────────────────────────
#  BÚSQUEDAS
# ─────────────────────────────────────────────

def buscarPorNombre(agencia, nombre):
    i = 0
    while i < tamanio(agencia):
        venta = recuperarVenta(agencia, i)
        if verNombre(venta) == nombre:
            return i
        i += 1
    return -1

def buscarPorCodigo(agencia, codigo):
    i = 0
    while i < tamanio(agencia):
        venta = recuperarVenta(agencia, i)
        if verCodigo(venta) == codigo:
            return i
        i += 1
    return -1


# ─────────────────────────────────────────────
#  MOSTRAR UNA VENTA
# ─────────────────────────────────────────────

def mostrarVenta(venta):
    print("Código        :", verCodigo(venta))
    print("Servicio      :", verNombre(venta))
    print("Tipo actividad:", verTipo(venta))
    print("Operador      :", verOperador(venta))
    print("Plan de pago  :", verPlan(venta))
    print("Importe       :", verImporte(venta))
    print("Fecha         :", verFecha(venta))
    print("Hora          :", verHora(venta))


# ─────────────────────────────────────────────
#  OPERACIÓN 1: REGISTRAR NUEVA VENTA
# ─────────────────────────────────────────────

def registrarVenta(agencia):
    print("\n-- REGISTRAR VENTA --")
    codigo   = int(input("Código de excursión: "))
    nombre   = input("Nombre del servicio: ")
    tipo     = input("Tipo de actividad (Aventura / Cultural / Relax): ")
    operador = input("Operador turístico: ")
    plan     = input("Plan de pago: ")
    importe  = float(input("Importe: "))
    fecha_str = input("Fecha (YYYY-MM-DD): ")
    hora_str  = input("Hora (HH:MM): ")
    anio, mes, dia     = fecha_str.split("-")
    horas, minutos     = hora_str.split(":")
    fecha = date(int(anio), int(mes), int(dia))
    hora  = time(int(horas), int(minutos))

    venta = crearVenta()
    cargarVenta(venta, codigo, nombre, tipo, operador, plan, importe, fecha, hora)
    agregarVenta(agencia, venta)

    print("Venta registrada exitosamente.")


# ─────────────────────────────────────────────
#  OPERACIÓN 2a: MODIFICAR VENTA (por nombre)
# ─────────────────────────────────────────────

def modificarVenta(agencia):
    print("\n-- MODIFICAR VENTA --")
    nombre = input("Nombre del servicio a modificar: ")
    indice = buscarPorNombre(agencia, nombre)

    if indice == -1:
        print("No se encontró ninguna venta con ese nombre.")
        return

    venta = recuperarVenta(agencia, indice)

    print("¿Qué campo querés modificar?")
    print("  1. Código")
    print("  2. Nombre")
    print("  3. Tipo de actividad")
    print("  4. Operador")
    print("  5. Plan de pago")
    print("  6. Importe")
    print("  7. Fecha")
    print("  8. Hora")
    opcion = input("Opción: ")

    if opcion == "1":
        modCodigo(venta, int(input("Nuevo código: ")))
    elif opcion == "2":
        modNombre(venta, input("Nuevo nombre: "))
    elif opcion == "3":
        modTipo(venta, input("Nuevo tipo de actividad: "))
    elif opcion == "4":
        modOperador(venta, input("Nuevo operador: "))
    elif opcion == "5":
        modPlan(venta, input("Nuevo plan de pago: "))
    elif opcion == "6":
        modImporte(venta, float(input("Nuevo importe: ")))
    elif opcion == "7":
        modFecha(venta, input("Nueva fecha (YYYY-MM-DD): "))
    elif opcion == "8":
        modHora(venta, input("Nueva hora (HH:MM): "))
    else:
        print("Opción inválida.")
        return

    print("Venta modificada exitosamente.")


# ─────────────────────────────────────────────
#  OPERACIÓN 2b: CANCELAR VENTA (por código)
# ─────────────────────────────────────────────

def cancelarVenta(agencia):
    print("\n-- CANCELAR VENTA --")
    codigo = int(input("Código de excursión a cancelar: "))
    indice = buscarPorCodigo(agencia, codigo)

    if indice == -1:
        print("No se encontró ninguna venta con ese código.")
        return

    else: venta = recuperarVenta(agencia, indice)
    eliminarVenta(agencia, venta)
    print("Venta cancelada exitosamente.")


# ─────────────────────────────────────────────
#  LISTAR TODAS LAS VENTAS
# ─────────────────────────────────────────────

def listarVentas(agencia):
    print("\n-- VENTAS REGISTRADAS --")
    if tamanio(agencia) == 0:
        print("No hay ventas registradas.")
        return
    i = 0
    while i < tamanio(agencia):
        print(f"\nVenta #{i + 1}")
        mostrarVenta(recuperarVenta(agencia, i))
        i += 1


# ─────────────────────────────────────────────
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────────

def mostrarMenu():
    print("\n=== AGENCIA DE TURISMO ===")
    print("1. Registrar nueva venta")
    print("2. Modificar venta (por nombre)")
    print("3. Cancelar venta  (por código)")
    print("4. Listar ventas")
    print("0. Salir")

def main():
    agencia = crearAgencia()

    opcion = ""
    while opcion != "0":
        mostrarMenu()
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            registrarVenta(agencia)
        elif opcion == "2":
            modificarVenta(agencia)
        elif opcion == "3":
            cancelarVenta(agencia)
        elif opcion == "4":
            listarVentas(agencia)
        elif opcion != "0":
            print("Opción inválida.")

    print("¡Hasta luego!")

main()
