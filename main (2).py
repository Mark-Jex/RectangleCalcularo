Length = int(input("Length?:"))

Width = int(input("Width?:"))

guess = int(input("what do you think is the area?:"))

area = Length * Width

if guess != area:
  print ("wrong")

if guess == area:
  print ("CORRRRRRRRRRRRRRRRRRRRRRRRRRRREEEEEEEEEEEEEEEEEEEEEEEEECCCCT!")