import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def generate_custom_signal(t, A, K, t1, n, t2, f, phi):
    signal = A * K * ((t / t1) ** n / (1 + (t / t1) ** n)) * np.exp(-t / t2) * np.cos(2 * np.pi * f * t + phi)
    return signal

def plot_time_domain(time, signal, title):
    plt.plot(time, signal)
    plt.xlim(0, 0.5)
    plt.title(title + " w dziedzinie czasu")
    plt.xlabel("Czas [s]")
    plt.ylabel("Amplituda")
    plt.grid(True)
    plt.show()

def plot_frequency_domain(signal, sampling_rate, title):
    fft_signal = fft(signal)
    frequency_axis = np.linspace(-sampling_rate / 2, sampling_rate / 2, len(fft_signal))
    plt.plot(frequency_axis, np.abs(np.fft.fftshift(fft_signal)))
    plt.title(title + " - Charakterystyka częstotliwościowa")
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Amplituda")
    plt.grid(True)
    plt.xlim(left=-5000000, right=5000000)  # Ograniczenie zakresu osi X
    plt.show()

# Parametryzacja sygnału
A = 1.0
K = 0.8
t1_values = [0.2, 0.5, 1.0]  # Różne wartości czasu t1
t2_vlaues = [0.1, 0.6, 2]
n_values = [2, 4, 6]  # Różne wartości nachylenia charakterystyki gaśnięcia sinusoidy n
f = 259004
phi_values = [0, np.pi/4, np.pi/2]  # Różne wartości fazy φ
duration = 1.0
sampling_rate = 60000000

# Generowanie sygnałów i wykresów
for t1 in t1_values:
    for t2 in t2_vlaues:
        for n in n_values:
            for phi in phi_values:
                time = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
                signal = generate_custom_signal(time, A, K, t1, n, t2, f, phi)
                title = f"Sygnał: t1={t1}, , t2={t2}, n={n}, φ={phi}"
                plot_time_domain(time, signal, title)
                plot_frequency_domain(signal, sampling_rate, title)
