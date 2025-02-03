def primos(a):
  n = len(a)
  i = 0
  while i < n:
    n = len(a)
    j = 2
    while j <= int(a[i]**0.5):
      if a[i] % j == 0:
        a.pop(i)
        j = int(i**0.5)+1
        i -= 1
      j +=1
    i += 1
  return a

if __name__=='__main__':
  a = input("Digite los numeros separados por comas: ").split(',')
  try:
    a = [int(n) for n in a]
    p = primos(a)
    print(p)
  except ValueError as ve:
    print("Hay datos que generan conflictos. ")
  