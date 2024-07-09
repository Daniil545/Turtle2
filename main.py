import turtle as t
t.shape("classic")#turtle,circle,square
t.speed(5)
t.color("purple")

a=int(input("введите сколько строн?"))
size=int(input("введите длину стороны"))
if a==3:
  t.forward(size)
  t.left(120)
  t.forward(size)
  t.left(120)
  t.forward(size)
  t.left(120)
elif a==4:
  t.forward(size)
  t.left(90)
  t.forward(size)
  t.left(90)
  t.forward(size)
  t.left(90)
  t.forward(size)
  t.left(90)
elif a==5:
  t.forward(size)
  t.left(72)
  t.forward(size)
  t.left(72)
  t.forward(size)
  t.left(72)
  t.forward(size)
  t.left(72)
  t.forward(size)
  t.left(72)
else:
 print("такую фигуру не завезли")
