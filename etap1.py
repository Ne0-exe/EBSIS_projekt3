import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def generate_sinusoidal_signal(amplitude, frequency, duration, sampling_rate):
    time = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * time)
    return time, signal

def generate_composite_signal(amplitude1, frequency, amplitude2, duration, sampling_rate, time_shift):
    time = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    signal1 = amplitude1 * np.sin(2 * np.pi * frequency * time)
    signal2 = amplitude1 * np.sin(2 * np.pi * 0.5 * frequency * time + np.pi/4)  # Generowanie sygnału sinusoidalnego
    # Tworzenie gasnącego sygnału
    # fade_out = np.exp(-1000000 * time)  # Zastosowanie eksponencjalnego zaniku (można dostosować wartość zaniku)
    # signal2 *= fade_out  # Mnożenie sygnału przez wartości zaniku
    composite_signal = signal1 + signal2
    return time, composite_signal

def plot_time_domain(time, signal, title):
    plt.plot(time, signal)
    plt.xlim(0, 0.00001)
    plt.title(title + " w dziedzinie czasu")
    plt.xlabel("Czas [s]")
    plt.ylabel("Amplituda")
    plt.grid(True)
    plt.ylim(bottom=min(signal) - 0.5, top=max(signal) + 0.5)  # Przeskalowanie wykresu
    plt.show()

def plot_frequency_domain(signal, sampling_rate, title):
    fft_signal = fft(signal)
    frequency_axis = np.linspace(-sampling_rate / 2, sampling_rate / 2, len(fft_signal))
    plt.plot(frequency_axis, np.abs(np.fft.fftshift(fft_signal)))
    plt.title(title + " - Charakterystyka częstotliwościowa")
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Amplituda")
    plt.grid(True)
    plt.xlim(left=-300000, right=300000)  # Ograniczenie zakresu osi X
    plt.show()

# Parametryzacja sygnałów
amplitude1 = 1.0
frequency = 259004
amplitude2 = 2
duration = 0.2
sampling_rate = 60000000
time_shift = 0.1
K = 0.8


# Generowanie sygnałów
time_sinusoidal, sinusoidal_signal = generate_sinusoidal_signal(amplitude1, frequency, duration, sampling_rate)
time_composite, composite_signal = generate_composite_signal(amplitude1, frequency, amplitude2,
                                                             duration, sampling_rate, time_shift)

# Wykresy w dziedzinie czasu
plot_time_domain(time_sinusoidal, sinusoidal_signal, "Sygnał sinusoidalny")
plot_time_domain(time_composite, composite_signal, "Złożony sygnał")

# Wykresy w dziedzinie częstotliwości
plot_frequency_domain(sinusoidal_signal, sampling_rate, "Sygnał sinusoidalny")
plot_frequency_domain(composite_signal, sampling_rate, "Złożony sygnał")
