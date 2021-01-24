import tkinter
from random import randint
import time
print(1)
count=0
def prepare_and_start():
    global player, target, goal, colour
    randx = randint(10, 500)
    randy = randint(10, 500)
    canvas.delete("all")
    goalr = randi1
        

    target = canvas.create_oval(
            265, 265, 335, 335, outline="#990000",
            fill="#990000", width=2
        )

    colour = randint(1, 999999)
    
    player = canvas.create_oval(
            randx, randy, randx+70, randy+70, outline=f"#{colour}",
            fill=f"#{colour}", width=2
        )
        
    
    label.config(text=f"Klick'n Kick         Ваш Счет: {count}")
    master.bind("<KeyPress>", key_pressed)


def move_wrap(ob
    if canvas.coords(obj)[0] <= 0:
        canvas.move(obj, tpnum, 0)
        
    if canvas.coords(obj)[1] <= 0:
        canvas.move(obj, 0, tpnum)
        
    if canvas.coords(obj)[0] >= 600:
        canvas.move(obj, -tpnum, 0)
        
    if canvas.coords(obj)[1] >= 600:
        canvas.move(obj, 0, -tpnum)
        
    
    master.bind("<KeyPress>", key_pressed)


def key_pressed(event):
    global count
    
    if event.keysym == 'Up':
        canvas.move(player, 0, -20)
      
    elif event.keysym == 'Down':
        canvas.move(player, 0, 20)
       
    elif event.keysym == 'Right':
        canvas.move(player, 20, 0)
        
    elif event.keysym == 'Left':
        canvas.move(player, -20, 0)
        
    if canvas.coords(player)[0] <= 0 or canvas.coords(player)[1] <= 0:
        move_wrap(player)
    if canvas.coords(player)[0] >= 600 or canvas.coords(player)[1] >= 600:
        move_wrap(player)
    if canvas.coords(target)[0] <= 0 or canvas.coords(target)[1] <= 0:
        move_wrap(target)
    if canvas.coords(target)[0] >= 600 or canvas.coords(target)[1] >= 600:
        move_wrap(target)

    
        
    if (canvas.coords(target)[0]-150 < canvas.coords(player)[0]+35 < canvas.coords(target)[0] and canvas.coords(target)[1] < canvas.coords(player)[1]+35 < canvas.coords(target)[1]+70):
        canvas.move(target, 20, 0)

    if (canvas.coords(target)[0] < canvas.coords(player)[0]+35 < canvas.coords(target)[0]+150 and canvas.coords(target)[1] < canvas.coords(player)[1]+35 < canvas.coords(target)[1]+70):
        canvas.move(target, -20, 0)

    if (canvas.coords(target)[0] < canvas.coords(player)[0]+35 < canvas.coords(target)[0]+70 and canvas.coords(target)[1]-150 < canvas.coords(player)[1]+35 < canvas.coords(target)[1]):
        canvas.move(target, 0, 20)

    if (canvas.coords(target)[0] < canvas.coords(player)[0]+35 < canvas.coords(target)[0]+70 and canvas.coords(target)[1] < canvas.coords(player)[1]+35 < canvas.coords(target)[1]+150):
        canvas.move(target, 0, -20)


    if canvas.coords(target)[0] < canvas.coords(goal)[0]+10 < canvas.coords(target)[0]+70 and canvas.coords(target)[1] < canvas.coords(goal)[1]+10 < canvas.coords(target)[1]+70:
        count +=1
        
        canvas.create_rectangle(
            0, 0, 600, 600,
            outline=f"#{colour}", fill=f"#{colour}",
        )
        canvas.create_text(
            300, 300, font="ComicSans",
            text="Победа!"
        )
        
        


master = tkinter.Tk()




canvas = tkinter.Canvas(master, bg='#FCAB08',
                        width=600, height=600)



label = tkinter.Label(master, text="Не попадись!")
restart = tkinter.Button(master, text="Начать заново",
                         command=prepare_and_start)

restart.pack()
label.pack()
canvas.pack()
prepare_and_start()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
