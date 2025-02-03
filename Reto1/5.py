def anagramas(l):
  g = {}
  for p in l:
    if p is not str:
      raise TypeError("Solo se aceptan cadenas de caracteres")
    c = tuple(sorted(p.lower()))
    if c in g:
      g[c].append(p)
    else:
      g[c] = [p]
  r = []
  for go in g.values():
    if len(go) > 1:
      r.extend(go)
  return r

if __name__=='__main__':
  e = input("Digite las cadenas de caracteres separadas por comas: ")
  l = [p.strip() for p in e.split(',')]
  print (l)
  r = anagramas(l)
  print(r)