while True:
  try:
    a, b, c = map(int, input().split())
    if a == b == c:
      print("*")
    elif a != b and a != c:
      print('A')
    elif b != a and b != c:
      print('B')
    else: print('C')
  except EOFError:
    break