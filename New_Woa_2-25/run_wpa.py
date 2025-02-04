import numpy as np
import matplotlib.pyplot as plt
from wpa import WPA
from Get_funcion import switch_case

def creat_populations(lb,ub,dim,number_of_sols):
    return np.random.uniform(lb, ub, (number_of_sols, dim))



if __name__ == "__main__":
    dim = 30
    number_of_sols = 30
    max_iter = 1000
    lb, ub, fitness_func = switch_case("F1")
    n = 10
    avr = 0
    for i in range (n):
        populations = creat_populations(lb, ub, dim, number_of_sols)
        wpa = WPA(dim,(lb,ub),number_of_sols, max_iter, fitness_func, populations)
        wpa.optimize()
        avr += wpa.best_fitness

    print("AVR: ",avr / n)


    # populations = creat_populations(lb, ub, dim, number_of_sols)
    # wpa = WPA(dim,(lb,ub),number_of_sols, max_iter, fitness_func, populations)
    # wpa.optimize()
    # print("Best_fitness: ",wpa.best_fitness)
    # plot_single_algorithm(wpa.fitness_history)

