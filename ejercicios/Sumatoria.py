def facto(num):
  if num == 1:
    return 1
  return num * facto(num-1)

def Termino1(n, x,numero_veces):
    ecuacion= 1 + (n*x)/facto(1)
    for conta in range(2,numero_veces+1):
        ecuacion += (n*(n-1)**conta)/facto(conta)
    return ecuacion
    

def Termino2(x, numero_veces):
  base = 1
  for conta in range(1,numero_veces+1):
    base += x**conta/facto(conta)
  return base

def Termino3(n,x, numero_veces):
    acum=1
    base = n*x**acum
    for conta in range(1, numero_veces+1):
        acum += conta
        base += (n-conta)*x**(acum)
    return base



def Termino4(x, numero_veces):
    primos= [i for i in range(2,numero_veces) if i%2 != 0 and i!=2]
    primos.insert(0, 2)
    conta=0
    result=0
    for num in primos:
        result += x**conta/facto(num)
        conta += 1
    return result

def Termino5(x, n, numero_veces):
    result = 0
    for conta in range(0, numero_veces+1):
        result += facto((x+(conta+1)))/x**(n-conta)
    return result

print(Termino5(5,2,5))


class Empleado():
    def __init__(name,salario,Deducciones):
        self.name = name
        self.salario = salario
        self.Deducciones = Deducciones
    
    
def promedio_salario(salario_empleados):
    acumS=0
    conta=0
    for salario in lista_empleados:
        acumS += salario
        conta += 1
    return acumS/conta

def porcentaje_empleados(salario_empleados):
    salario_minimo= 900000
    acumS=0
    conta=0
    for salario in salario_empleados:
        conta += 1
        if salario > (salario_minimo*4):
            acumS += 1
    return  acumS*100 / conta



empleados = []

            
