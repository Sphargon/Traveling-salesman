if __name__ == '__main__':
    from fen_set_up import *
    from optimal_path import random_path_finding


    width:int = 1440
    height:int = 720
    fenetre , canvas = set_up()
    
    points = draw_cloud( canvas , height, width , 10 )
    print(points)
    draw_path( canvas, points )


    Random_path = Button(text = "Calcul : random", command = lambda : random_path_finding(points))
    Random_path.place(x=0, y=0)

    fenetre.mainloop()
