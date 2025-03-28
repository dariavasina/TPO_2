import csv
from functions.system_function import system_function

EPSILON = 1e-10


def generate_csv(start, end, step, filename, delimiter=",", eps=EPSILON):
    if step <= 0:
        raise ValueError("Step should be positive")
    
    with open(filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        x = start 
        while x <= end:
            try:
                result = system_function(x, eps)
            except Exception as e:
                result = None
            writer.writerow([x, result])
            x += step
