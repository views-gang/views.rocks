import random
n=random.randint(0, 180)
b= f'''  -webkit-transform: rotate({n}deg);
  -moz-transform: rotate({n}deg);
  -ms-transform: rotate({n}deg);
  -o-transform: rotate({n}deg);
  transform: rotate({n}deg);'''
print(b)