def rot13(str):
  res = ""
  for s in str:
    if (ord("A")<=ord(s)<=ord("M")) or (ord("a")<=ord(s)<=ord("m")):
      s=chr(ord(s)+13)
      res+=s
    elif ord("N")<=ord(s)<=ord("Z") or (ord("n")<=ord(s)<=ord("z")):
      s=chr(ord(s)-13)
      res+=s
  return res
string=input('Введите текст') 
#исключение  
try: #не могу придумать нормальное исключение
  print('Закодированная/раскодированная строка:',rot13(string,5))
except TypeError:
  print('TypeError:Функция rot13 должна иметь только один позиционный аргумент, попробуем другой вызов фунции')
finally:
  print('Закодированная/раскодированная строка:',rot13(string))