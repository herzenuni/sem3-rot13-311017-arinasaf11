def rot13(str):
  """Функция шифрует введенную строку с помощью алгоритма rot13"""
  res = ""
  for s in str:
    if (ord("A")<=ord(s)<=ord("M")) or (ord("a")<=ord(s)<=ord("m")):
      s=chr(ord(s)+13)
      res+=s
    elif ord("N")<=ord(s)<=ord("Z") or (ord("n")<=ord(s)<=ord("z")):
      s=chr(ord(s)-13)
      res+=s
  return res
