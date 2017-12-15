import rot13 as r
def test_rot13(str):
  """Функция проверяет функцию Rot13 на кодировку и раскодировку"""
  assert(r.rot13(r.rot13(str)) == str) 
  return r.rot13(r.rot13(str)) == str
  