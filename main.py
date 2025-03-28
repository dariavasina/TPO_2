from functions.csv_generator import generate_csv
from functions.trigonometry import sin_taylor, cos_taylor
from functions.system_function import system_function
from functions.logarithms import ln_taylor, log_base

if __name__ == "__main__":
    generate_csv(-10, 10, 0.01, "results.csv")
    generate_csv(-10, 10, 0.01, "sin.csv", function=sin_taylor)
    generate_csv(-10, 10, 0.01, "cos.csv", function=cos_taylor)
    generate_csv(-10, 10, 0.01, "ln.csv", function=ln_taylor)
