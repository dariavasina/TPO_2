import csv
from functions.system_function import system_function
EPSILON = 1e-10

def generate_csv(start, end, step, filename, eps=EPSILON):
    """
    Генерация csv-файла с двумя столбцами: x и system_function(x).
    Параметры:
      start – начальное значение x,
      end – конечное значение x,
      step – шаг изменения x,
      filename – имя файла для сохранения.
    """
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        x = start
        while x <= end:
            try:
                result = system_function(x, eps)
            except Exception as e:
                result = str(e)
            writer.writerow([x, result])
            x += step