def suma(a):
  s = a[0] + a[1]
  for i in range(1, len(a)):
    if (a[i-1] + a[i]) > s:
      s = a[i] + a[i+1]
  return s

if __name__=='__main__':
  a = input("Digite los numeros separados por comas: ").split(',')
  a = [int(n) for n in a]
  s = suma(a)
  print(s)