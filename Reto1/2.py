def palindromo(a):
  if a is not str:
    raise TypeError("Solo se aceptan cadenas de caracteres")
  for i in range(len(a)):
    if a[i] != a[-i-1]:
      return False
  return True

if __name__=="__main__":
  a = input("Digite una cadena de caracteres: ")
  p = palindromo(a)
  print(f"{a} es palindrome?: {p}")