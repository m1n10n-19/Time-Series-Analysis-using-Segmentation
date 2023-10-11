import numpy as np
import matplotlib.pyplot as plt
import csv

def generate_curve(amplitudes, frequencies, num_samples=1000):
    t = np.linspace(0, 2*np.pi, num_samples)
    curve = np.zeros_like(t)

    for amp, freq in zip(amplitudes, frequencies):
        curve += amp * np.cos(freq * t) + amp * np.sin(freq * t)
    
    return t, curve

def main():
    amplitudes = [1.0, 0.5]  # List of amplitudes for cosine and sine components
    frequencies = [2.0, 4.0]  # List of frequencies for cosine and sine components
    num_samples = 1000

    t, curve = generate_curve(amplitudes, frequencies, num_samples)

    # Display the curve
    plt.figure()
    plt.plot(t, curve)
    plt.title('Generated Curve')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()

    # Save sampled points to CSV file
    with open('ts_data\sampled_wave_data_1.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Time', 'Amplitude'])
        for i in range(num_samples):
            csvwriter.writerow([t[i], curve[i]])

if __name__ == "__main__":
    main()
