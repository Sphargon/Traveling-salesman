from ouais.fen_set_up import *
from ouais.optimal_path import random_path_finding

def main() -> None:
    width:int = 1440
    height:int = 720
    fenetre , canvas = set_up()
    
    points = draw_cloud( canvas , height, width , 10 )
    print(points)
    draw_path( canvas, points )
    # id = str(input("Rentrez une ID si vous voules utiliser un preset : "))
    # if id == "":
    #     points = draw_cloud( canvas , height, width , 10 )
    #     print(points)
    #     draw_path( canvas, points )

    # else:
    #     pass



    Random_path = Button(text = "Calcul : random", command = lambda : random_path_finding(points))
    Random_path.place(x=0, y=0)

    fenetre.mainloop()



if __name__ == '__main__':
    main()
