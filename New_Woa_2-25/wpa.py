import numpy as np

class WPA:
    def __init__(self, dim, range_, number_of_sols, max_iter, fitness_func,populations):

        self.dim = dim
        self.range = range_
        self.fitness_func = fitness_func
        self.number_of_sols = number_of_sols
        self.max_iter = max_iter
        self.population = populations
        self.c1 = 1
        self.c2 = 0.1

        self.pbest_sol = np.copy(self.population)
        self.pbest_fitness = self.calculate_fitness(populations)
        self.best_sol = self.pbest_sol[np.argmin(self.pbest_fitness)]
        self.best_fitness = np.min(self.pbest_fitness)
        self.velocity = np.random.uniform(-1,1, (number_of_sols, dim))

        self.fitness_history = []
        self.IC_history = []
        self.Deversity = []

    def calculate_fitness(self, pop):
        return np.array([self.fitness_func(whale) for whale in pop])

    def select_best_fitness(self, fitness_list):
        min_idx = np.argmin(fitness_list)
        curr_best_sol = self.population[min_idx]
        min_value = fitness_list[min_idx]

        if min_value < self.best_fitness:
            self.best_sol = curr_best_sol
            self.best_fitness = min_value

    def calculate_A(self, w):
        r = np.random.uniform(0, 1, self.dim)  
        return 2 * w * r - w

    def calculate_C(self):
        return 2 * np.random.uniform(0, 1, self.dim)  

    def calculate_D(self, X_rb, X):
        C = self.calculate_C()
        return np.abs(C * X_rb - X)  

    def encircling(self, X_best, X, A):
        D = self.calculate_D(X_best, X)
        return X_best - A * D  

    def searching(self, X_rand, X, A):
        D = self.calculate_D(X_rand, X)
        return X_rand - A * D  

    def attacking(self, vec,pbest):
        l = np.random.uniform(-1,1)
        return vec * np.exp(1 * l) * np.cos(2 * np.pi * l) + pbest

    def checking(self, populations, bounds):
        lb, ub = bounds
        populations[:] = np.clip(populations, lb, ub)


    def optimize(self):

        for t in range(self.max_iter):
            
            w = 2 - 2*t / self.max_iter

            self.c1 = self.c1 * (1 - t / self.max_iter)  # Giảm tuyến tính từ c1_init về 0
            self.c2 = self.c2 + (1 - self.c2) * (t / self.max_iter)  # Tăng tuyến tính

            for i in range(self.number_of_sols):

                cognitive_component = self.c1  * (self.pbest_sol[i] - self.population[i])  #khoảng cách đến tốt nhất cục bộ
                social_component = self.c2 * (self.best_sol - self.population[i]) #khoảng cách đến tốt nhất toàn cục
                self.velocity[i] = w * self.velocity[i] + cognitive_component + social_component #tính toán vector di chuyển
                v_max = 0.1 * (self.range[1] - (self.range[0]))
                self.velocity = np.clip(self.velocity, -v_max, v_max)
                p = np.random.uniform(0, 1)
                if p < 0.5:
                    A = self.calculate_A(w)
                    if np.linalg.norm(A) < 1:
                        self.population[i] = self.encircling(self.best_sol, self.population[i], A)
                    else:
                        self.population[i] = np.random.uniform(np.min(self.best_sol),np.max(self.best_sol),self.dim)
                else:
                    self.population[i] = self.attacking(self.velocity[i],self.pbest_sol[i])




                current_value = self.fitness_func(self.population[i])
                if current_value < self.pbest_fitness[i]:
                    self.pbest_sol[i] = self.population[i]
                    self.pbest_fitness[i] = current_value

            apbest_index = np.argmin(self.pbest_fitness)
            if self.pbest_fitness[apbest_index] < self.best_fitness:
                self.best_sol = self.pbest_sol[apbest_index]
                self.best_fitness = self.pbest_fitness[apbest_index]

            self.checking(self.population, self.range)
                
            self.fitness_history.append(self.best_fitness)

