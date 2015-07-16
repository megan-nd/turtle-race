import turtle
import random
import time

turtle.setup(1050,300)
t = turtle.Pen()
u = turtle.Pen()
r = turtle.Pen()
l = turtle.Pen()
e = turtle.Pen()

t.up()
t.goto(-500,100)
t.down()

u.up()
u.goto(-500,50)
u.down()

r.up()
r.goto(-500,0)
r.down()

l.up()
l.goto(-500,-50)
l.down()

e.up()
e.goto(-500,-100)
e.down()

t.shape('turtle')
t.color('red')
t.speed(1)
u.shape('turtle')
u.color('green')
u.speed(1)
r.shape('turtle')
r.color('blue')
r.speed(1)
l.shape('turtle')
l.color('orange')
l.speed(1)
e.shape('turtle')
e.color('purple')
e.speed(1)

def move():
    print('Take your pick!')
    time.sleep(2)
    print('Ready..')
    time.sleep(1)
    print('Set..')
    time.sleep(1)
    print('Go!')
    print(' ')
    for x in range(0,20):
        fwd = random.randint(0,100)
        t.forward(fwd)
        if t.xcor() >= int(500):
            print('Red wins!')
            break
        fwd = random.randint(0,100)
        u.forward(fwd)
        if u.xcor() >= int(500):
            print('Green wins!')
            break
        fwd = random.randint(0,100)
        r.forward(fwd)
        if r.xcor() >= int(500):
            print('Blue wins!')
            break
        fwd = random.randint(0,100)
        l.forward(fwd)
        if l.xcor() >= int(500):
            print('Orange wins!')
            break
        fwd = random.randint(0,100)
        e.forward(fwd)
        if e.xcor() >= int(500):
            print('Purple wins!')
            break

def victory_spin():
    print('Take a victory spin!')
    if t.xcor() >= int(500):
        t.backward(500)
        t.speed(3)
        t.circle(-40,320)
        t.circle(-60,350)
        t.circle(-55,330)
        t.circle(-35,325)
        t.circle(-50,385)
    if u.xcor() >= int(500):
        u.backward(500)
        u.speed(3)
        u.circle(-40,320)
        u.circle(-60,350)
        u.circle(-55,330)
        u.circle(-35,325)
        u.circle(-50,385)
    if r.xcor() >= int(500):
        r.backward(500)
        r.speed(3)
        r.circle(40,320)
        r.circle(60,350)
        r.circle(55,330)
        r.circle(35,325)
        r.circle(50,385)
    if l.xcor() >= int(500):
        l.backward(500)
        l.speed(3)
        l.circle(40,320)
        l.circle(60,350)
        l.circle(55,330)
        l.circle(35,325)
        l.circle(50,385)
    if e.xcor() >= int(500):
        e.backward(500)
        e.speed(3)
        e.circle(40,320)
        e.circle(60,350)
        e.circle(55,330)
        e.circle(35,325)
        e.circle(50,385)

move()
print(' ')
print('Red is at %s' % t.xcor())
print('Green is at %s' % u.xcor())
print('Blue is at %s' % r.xcor())
print('Orange is at %s' % l.xcor())
print('Purple is at %s' % e.xcor())
print(' ')
time.sleep(2)
victory_spin()
