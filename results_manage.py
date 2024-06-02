from linecache import getline

def save_results(
        path_to_save:list[ list[ int,int ] ],
        path_length:float,
        # method_used:str,
        Id:int = -1 ) -> None:
    
    with open("Resultats.txt", "r+") as my_file:

        if Id == -1:

            my_file.seek(0, 0)
            index = int(my_file.readline())
            place = 9*(index) + 3

            text_to_write = f'''{place}\
            \n----------------------------------\
            \nThe path taken is :\
            \n{path_to_save}
            \nIts length is :\
            \n{path_length}\
            \n----------------------------------
            \n'''

            my_file.seek(0)
            my_file.write(f"{index+1}")

            my_file.seek(0, 2)
            my_file.write(text_to_write)

            

        else:
            return
        
        my_file.close()

def isset_id(Id:str) -> bool:
    try:
        line_index:int = int(Id[0])
        line:list = eval(getline("index.txt", line_index))

    except:
        print("The given Id doesn't follow the rules of id setting")
        return False

    Id = int(Id)
    for i in line:
        if i == Id:
            return True
    return False
