import turtle
t = turtle.Turtle()
t.shape("turtle")

list1 = []

data = int(input("x1 :"))
list1.append(data)

data = int(input("y1 :"))
list1.append(data)

data = int(input("x2 :"))
list1.append(data)

data = int(input("y2 :"))
list1.append(data)

data = int(input("x3 :"))
list1.append(data)

data = int(input("y1 :"))
list1.append(data)

t.goto(list1[0], list1[1])
t.goto(list1[2], list1[3])
t.goto(list1[4], list1[5])
