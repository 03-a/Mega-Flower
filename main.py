def MakeTheProject(): 
    import turtle
    import time
    
    FL = []
    CL = []
    n1 = int(input("Type circles: "))
    n2 = int(input("Type circle radius: "))
    n3 = int(input("Type dot radius: "))
    n4 = input("Type title: ")
    n5 = input("Type bgcolor: ")
    n6, n7 = map(int,input("X, y: ").split( ))
    n8 = int(input("Pen size: "))
    while True: 
        n9 = input("Type a specific fill color (Type End to end): ")
        if n9 == "End": 
            break
        else: 
            FL.append(n9)
    while True: 
        n10 = input("Type a specific outline color (Type End to end): ")
        if n10 == "End": 
            break
        else: 
            FL.append(n10)
    
    s = turtle.getscreen()
    t = turtle.Turtle()
    turtle.bgcolor(n5)
    turtle.title(n4)
    t.pensize(3)
    t.goto(n6, n7)
    t.speed(n8)
    
    for i in range(0, n1): 
        t.pencolor(CL[i % len(i)])
        t.fillcolor(FL[i % len(i)])
        t.begin_fill()
        t.circle(n2)
        t.rt(360 // n1)
        t.end_fill()
    t.dot(n3)
    
    time.sleep(10)

MakeTheProject()
