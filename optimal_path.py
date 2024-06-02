from random import sample, seed, random
from ouais.results_manage import save_results
from math import sqrt


def path_length(path:list[ list[ int,int ] ]) -> int:
    final_length = 0
    for i in range(len(path)):
        try:
            final_length += sqrt( (path[i+1][0] - path[i][0]) ** 2 + (path[i+1][1] - path[i][1]) ** 2 )

        except IndexError:
            final_length += sqrt( (path[0][0] - path[i][0]) ** 2 + (path[0][1] - path[i][1]) ** 2 )

    return final_length


def random_path_finding(
        steps:list[ list[ int,int ] ],
        Id:int = None,
        max_recurrence:int = 100 ) -> list:
    
    # start:int = randint(0, len(steps)-1)
    best_path:list = []
    best_length = 1_000_000_000

    for i in range(max_recurrence):

        new_path = sample(steps, k=len(steps))
        new_length = path_length(new_path)

        if new_length < best_length:
            best_path = new_path
            best_length = new_length

    if not Id:
        save_results(best_path, best_length)
        
        # specific_seed = 0
        # for i in steps:
        #     specific_seed += i[0]+i[1]

        # seed(specific_seed)
        # save_results(best_path, best_length, round(random()*10**10))

    else:
        save_results(best_path, best_length, Id)






