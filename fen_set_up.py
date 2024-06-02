from tkinter import *
from random import randrange

def set_up(
        win_height:int = 720,
        win_width:int = 1440,
        win_bg_col:str = "grey" ) -> Tk:
    


    #Mise en place de "l'environnement" graphique
    fen = Tk()
    fen.title("Wanderer's path")
    fen.geometry(f"{win_width+5}x{win_height+5}")

    Zone = Canvas(fen, width = win_width, height = win_height, bg = win_bg_col)
    Zone.place(x = 0, y = 0)

    return fen , Zone


def draw_cloud( canvas:Canvas ,
                win_height:int,
                win_width:int,
                nb_of_points:int = 0 ) -> list:


    coords:list = []

    for i in range(nb_of_points):
        x:int = randrange(0, win_width, 10)
        y:int = randrange(0, win_height, 10)

        coords.append([x, y])

        canvas.create_oval(x-5, y-5, x+5, y+5, fill = "black")

    return coords


''' A function that takes a list of points and draws the path that passes through each one of them following the order of the list '''
def draw_path( canvas:Canvas,
                order:list[ list[ int,int ] ] = [] ) -> None:

    for i in range(len(order)):

        try:
            x1 = order[i][0]
            y1 = order[i][1]
            x2 = order[i+1][0]
            y2 = order[i+1][1]

        except IndexError:
            x1 = order[i][0]
            y1 = order[i][1]
            x2 = order[0][0]
            y2 = order[0][1]

        finally:
            canvas.create_line(x1, y1, x2, y2, fill="white")
