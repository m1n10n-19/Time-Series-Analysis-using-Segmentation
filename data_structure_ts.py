import matplotlib.pyplot as plt
import numpy as np
import csv

tol = 0.0000001

class TimeSeriesData:
    def __init__(self, data=None):
        self.data = [] if data is None else data

    def add_data(self, x, primitive, y):
        self.data.append((x, primitive, y))

    def delete_data(self, primitive):
        self.data = [entry for entry in self.data if entry[1] != primitive]

    def display(self):
        for entry in self.data:
            print(f"({entry[0]} {entry[1]} {entry[2]})")

    def plot(self):
        x = 0
        y = []
        for entry in self.data:
            y_segment = [entry[0] + i for i in range(0, entry[2] - entry[0], 0.01)]
            x += int(entry[1][1:])
            for point in y_segment:
                y.append(point)
        x = np.linspace(0.0, )

def read_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  
        for row in csvreader:
            time = float(row[0])
            amplitude = float(row[1])
            data.append((time, amplitude))
    return data

def identify_primitive(first_slope, second_slope):
    if first_slope < tol and second_slope < tol:
        return 'A'
    elif first_slope - second_slope <= tol:
        if first_slope < 0:
            return 'F'
        else:
            return 'C'
    elif first_slope*second_slope < 0:
        if first_slope < 0:
            return 'I'
        else:
            return 'H'
    elif first_slope > second_slope:
        if first_slope > 0:
            return 'D'
        else:
            return 'G'
    elif second_slope > first_slope:
        if first_slope > 0:
            return 'B'
        else:
            return 'E'
    else:
        return '?'

if __name__ == '__main__':
    '''data = [
        (4.9132, 'G2', 6.2),
        (6.2, 'G2', 4.7),
        (4.7, 'E2', 2.2),
        (2.2, 'B2', 6.1),
        (6.1, 'D2', 9.9),
        (9.9, 'G2', 5.15),
        (5.15, 'E2', -0.003),
    ]'''

    data = []
    ts = TimeSeriesData(data)

    filename = 'ts_data/sampled_wave_data_1.csv'  
    wave_data = read_csv(filename)
    
    '''for point in wave_data:
        time, amplitude = point
        print(f"Time: {time}, Amplitude: {amplitude}")'''
    
    data_str = ''
    for i in range(2, len(wave_data), 3):
        new_component = identify_primitive(wave_data[i-1][1] - wave_data[i-2][1], wave_data[i][1] - wave_data[i-1][1])
        if i == 2:
            starting_point = wave_data[i-2]
            data_str += new_component + '1'
        else:
            if data_str[0] == new_component:
                data_str = new_component + str(int(data_str[1:]) + 1)
            else:
                ts.add_data(starting_point, data_str, wave_data[i-3])
                data_str = new_component + '1'
                starting_point = wave_data[i-2]
    
    ts.display()