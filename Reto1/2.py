def palindromo(a):
  for i in range(len(a)):
    if a[i] != a[-i-1]:
      return False
  return True

if __name__=="__main__":
  a = input("Digite una cadena de caracteres: ")
  p = palindromo(a)
  print(f"{a} es palindrome?: {p}")