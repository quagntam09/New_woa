import numpy as np

# Hàm Sphere (đơn giản, liên tục, lồi) 
# Global minimum: 0 tại x = [0,0,...,0]
# [−5, 5]
def sphere_func(x):
    return sum(xi ** 2 for xi in x)

# Hàm Rastrigin [-5, 5]
def rastrigin_func(x):
    return 10 * len(x) + sum((xi**2 - 10 * np.cos(2 * np.pi * xi)) for xi in x)

# Hàm Rosenbrock (phức tạp hơn, liên tục, không lồi) 
# Global minimum: 0 tại x = [1,1,...,1]
# [−2, 2]
def rosenbrock_func(x):
    return sum(100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2 for i in range(len(x) - 1))

# Hàm Ackley (khó khăn, không lồi) 
# Global minimum: 0 tại x = [0,0,...,0]
# [−5,5]
def ackley_func(x):
    a = 20
    b = 0.2
    c = 2 * np.pi
    n = len(x)
    sum1 = sum(xi ** 2 for xi in x) 
    sum2 = sum(np.cos(c * xi) for xi in x)
    return -a * np.exp(-b * np.sqrt(sum1 / n)) - np.exp(sum2 / n) + a + np.e

# Hàm Griewank (không lồi, có nhiều cực trị cục bộ) 
# Global minimum: 0 tại x = [0,0,...,0]
# [−600,600]
def griewank_func(x):
    part1 = sum(xi ** 2 for xi in x) / 4000
    part2 = np.prod([np.cos(xi / np.sqrt(i+1)) for i, xi in enumerate(x)])
    return part1 - part2 + 1

# Hàm Schwefel (khó khăn, không lồi) 
# Global minimum: 0 tại x: [420.9687,420.9687,...,420.9687] 
# [−500,500]
def schwefel_func(x):
    d = len(x)
    return 418.9829 * d - np.sum(x * np.sin(np.sqrt(np.abs(x))))

# Hàm Zakharov (liên tục, không lồi)
# Global minimum: 0 tại x=[0,0,...,0]
# Dải giá trị: [−5,10]
def zakharov_func(x):
    sum1 = sum(xi ** 2 for xi in x)
    sum2 = sum(0.5 * (i + 1) * xi for i, xi in enumerate(x))
    return sum1 + sum2 ** 2 + sum2 ** 4

# Hàm Michalewicz (khó khăn, không lồi, nhiều cực trị)
# Global minimum: Giá trị phụ thuộc vào số chiều, ví dụ cho 2 chiều là -1.8013.
# Dải giá trị: [0,π]
def michalewicz_func(x, m=10):
    x = np.array(x)  # Đảm bảo đầu vào là numpy array
    i = np.arange(1, len(x) + 1)  # Tạo chỉ số i
    term = np.sin(x) * (np.sin(i * x**2 / np.pi)) ** (2 * m)
    return -np.sum(term)

# Hàm Levy (phức tạp, không lồi)
# Global minimum: 0 tại x=[1,1,...,1]
# Dải giá trị: [−10,10]
def levy_func(x):
    w = [(1 + (xi - 1) / 4) for xi in x]
    term1 = np.sin(np.pi * w[0]) ** 2
    term2 = sum((wi - 1) ** 2 * (1 + 10 * np.sin(np.pi * wi + 1) ** 2) for wi in w[:-1])
    term3 = (w[-1] - 1) ** 2 * (1 + np.sin(2 * np.pi * w[-1]) ** 2)
    return term1 + term2 + term3


def switch_case(f_name):
    ranges_and_functions = {
        "F1": (-5,5, sphere_func),
        "F2": (-5.12,5.12, rastrigin_func),
        "F3": (-2,2, rosenbrock_func),
        "F4": (-5,5, ackley_func),
        "F5": (-600,600, griewank_func),
        "F6": (-500,500, schwefel_func),
        "F7": (-5,10, zakharov_func),
        "F8": (0,np.pi, michalewicz_func),
        "F9": (-10,10, levy_func),
    }

    if f_name in ranges_and_functions:
        return ranges_and_functions[f_name]
    else:
        return "Hàm không tồn tại trong danh sách."
