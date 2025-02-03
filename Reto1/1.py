def opBasicas(op):
  signo = op[2]
  if signo == "+":
    suma = op[0] + op[1]
    return suma
  elif signo == "-":
    resta = op[0] - op[1]
    return resta
  elif signo == "*":
    multiplicacion = op[0] * op[1]
    return multiplicacion
  elif signo == "/":
    division = op[0] / op[1]
    return division
  else:
    print("Opcion invalida")

if __name__=='__main__':
  print("\n Operaciones con enteros.")
  print("'+' Suma")
  print("'-' Resta")
  print("'*' Multiplicacion")
  print("'/' Division")
  a = input("Digite los numeros y despues el signo separados con comas: ").split(',')
  op = [int(a[0]), int(a[1]), str(a[2])]
  print(opBasicas(op))
