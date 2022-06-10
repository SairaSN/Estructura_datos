### Alejandro Álvarez Patiño
### Hernán Rios Igelsias
### Saira Salazar Nuñez
### Tatiana Guzman Cruz

import random
from ColasPython import Queue

class Cajas:
    
    def __init__(self, ppr): 
        self.tasaProductos = ppr      #Promedio de prodcutos registrados en 1 minuto 
        self.tareaActual = None
        self.tiempoRestante = 0
        self.contadorDeProductos=0    #Contador de productos adquiridos por cada persona
        self.cantidad=0                 

    def tiempo(self):
        if self.tareaActual != None:
            self.tiempoRestante = self.tiempoRestante - 1 
            if self.tiempoRestante == 0:
                self.tareaActual = None

    def ocupada(self):
        if self.tareaActual != None:
            return True
        else:
            return False
    
    def iniciarNueva(self,nuevaTarea):
        self.tareaActual = nuevaTarea
        cantidad=nuevaTarea.obtenerProductos()
        self.cantidadProductos(cantidad)
        self.tiempoRestante = cantidad * (60/self.tasaProductos) + 120 #Cantidad de productos adquiridos * promedio de tiempo en registrar productos + 120 segundos del tiempo de pago y devolución de dinero o pago con medios electrónicos

    def cantidadProductos(self,productos):
        self.contadorDeProductos+=productos   #Suma de los productos totales
        

class Tarea:
    def __init__(self,tiempo):
        self.marcaTiempo = tiempo
        self.productos = random.randrange(1,61) #Número aleatorio de productos que adquieren las personas

    def obtenerMarca(self):
        return self.marcaTiempo

    def obtenerProductos(self):
        return self.productos

    def tiempoEspera(self, tiempoActual):
        return tiempoActual - self.marcaTiempo

# Simulación con una sola fila para las tres cajas registradoras.
def simulacion1Fila(numeroSegundos, productosPorMinuto):   #Número de segundos para simulación y promedio de productos registrados por minuto en las cajas.
    filaPago = Queue()                                     
    tiemposEspera = []
    caja1 = Cajas(productosPorMinuto)  
    caja2 = Cajas(productosPorMinuto)
    caja3 = Cajas(productosPorMinuto)
    numeroClientes=0   #Número de personas que llegan a la fila                                 
    clientesCaja1=0    #Número de personas atendidas en cada caja
    clientesCaja2=0    #
    clientesCaja3=0    #     

    for segundoActual in range(numeroSegundos):            

        if nuevaTareaRegistro():
            tarea = Tarea(segundoActual)
            filaPago.enqueue(tarea)
            numeroClientes+=1
        if (not filaPago.is_empty()):                  

            if (not caja1.ocupada()):
                tareaSiguiente = filaPago.dequeue()
                tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
                caja1.iniciarNueva(tareaSiguiente)
                clientesCaja1+=1

            elif (not caja2.ocupada()):
                tareaSiguiente = filaPago.dequeue()
                tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
                caja2.iniciarNueva(tareaSiguiente)
                clientesCaja2+=1

            elif (not caja3.ocupada()):
                tareaSiguiente = filaPago.dequeue()
                tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
                caja3.iniciarNueva(tareaSiguiente)
                clientesCaja3+=1

        caja1.tiempo()
        caja2.tiempo()
        caja3.tiempo()

    print("SIMULACIÓN 1 FILA")
    print("Total Clientes: ",numeroClientes)
    print("Clientes atendidos: caja 1:",clientesCaja1," caja 2: ",clientesCaja2 ," caja 3: ",clientesCaja3 )
    esperaPromedio = sum(tiemposEspera) / float(len(tiemposEspera))
    print("Total productos vendidos: ",(caja1.contadorDeProductos+caja2.contadorDeProductos+caja2.contadorDeProductos))
    print("Tiempo de espera promedio %6.2f segundos %3d Clientes restantes en fila" % (esperaPromedio, filaPago.size()))

# Simulación con filas independientes cada una de las tres cajas registradoras.
def simulacion3Filas(numeroSegundos, productosPorMinuto):   #Número de segundos para simulación y promedio de productos registrados por minuto en las cajas.
    tiemposEspera = []
    filaPagoCaja1 = Queue()   
    filaPagoCaja2 = Queue()
    filaPagoCaja3 = Queue()
    caja1 = Cajas(productosPorMinuto)
    caja2 = Cajas(productosPorMinuto)
    caja3 = Cajas(productosPorMinuto)
    numeroClientes=0   #Número de personas que llegan a la fila
    clientesCaja1=0    #Número de personas atendidas en cada caja
    clientesCaja2=0    # 
    clientesCaja3=0    #

    for segundoActual in range(numeroSegundos):        
        if nuevaTareaRegistro():
            numeroClientes+=1
            tarea = Tarea(segundoActual) 
            #Asignar tarea a la fila con menor tamaño
            if filaPagoCaja1.size() <= filaPagoCaja2.size() and filaPagoCaja1.size() <= filaPagoCaja3.size():
                filaPagoCaja1.enqueue(tarea)
            elif filaPagoCaja2.size() <= filaPagoCaja1.size() and filaPagoCaja2.size() <= filaPagoCaja3.size():
                filaPagoCaja2.enqueue(tarea)
            else:
                filaPagoCaja3.enqueue(tarea)
        
        if (not filaPagoCaja1.is_empty()) and (not caja1.ocupada()):
            clientesCaja1+=1 
            tareaSiguiente = filaPagoCaja1.dequeue()
            tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
            caja1.iniciarNueva(tareaSiguiente)

        elif (not filaPagoCaja2.is_empty()) and (not caja2.ocupada()):
            clientesCaja2+=1
            tareaSiguiente = filaPagoCaja2.dequeue()
            tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
            caja2.iniciarNueva(tareaSiguiente)

        elif (not filaPagoCaja3.is_empty()) and (not caja3.ocupada()):
            clientesCaja3+=1
            tareaSiguiente = filaPagoCaja3.dequeue()
            tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
            caja3.iniciarNueva(tareaSiguiente)

        caja1.tiempo()
        caja2.tiempo()
        caja3.tiempo()

    print("SIMULACIÓN 3 FILAS")
    print("Total Clientes: ",numeroClientes)
    print("Clientes atendidos: caja 1:",clientesCaja1," caja 2: ",clientesCaja2 ," caja 3: ",clientesCaja3 )
    esperaPromedio = sum(tiemposEspera) / float(len(tiemposEspera))
    print("Total productos vendidos: ",(caja1.contadorDeProductos+caja2.contadorDeProductos+caja2.contadorDeProductos))
    print("Tiempo de espera promedio",round(esperaPromedio,2),"segundos  Clientes restantes caja 1:",filaPagoCaja1.size()," Clientes restantes caja 2: ",filaPagoCaja2.size()," Clientes restantes caja 3: ",filaPagoCaja1.size())

def nuevaTareaRegistro():
    numero = random.randrange(1,612)  #Rango de tiempo estimado que le toma a una persona en llegar a la fila. 
    if numero == 1:
        return True
    else:
        return False

for i in range(10):
    simulacion3Filas(3600,8)  
    print("")
    simulacion1Fila(3600,8)
    print("-------------------------------------------------------------")

