import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

def generate_custom_signal(t, A, K, t1, n, t2, f, phi):
    signal = A * K * ((t / t1) ** n / (1 + (t / t1) ** n)) * np.exp(-t / t2) * np.cos(2 * np.pi * f * t + phi)
    return signal

# Parametryzacja sygnału
A = 1.0
K = 0.8
t1 = 0.2
n = 2
t2 = 0.5
f = 259004
phi = 0.0
duration = 1.0
sampling_rate = 6000000

# Generowanie sygnału
time = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
signal = generate_custom_signal(time, A, K, t1, n, t2, f, phi)

# Wykresy w dziedzinie czasu
plt.stem(time, signal)
plt.title("Sygnał w dziedzinie czasu")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.grid(True)
plt.show()

# Wykresy w dziedzinie częstotliwości (Spektrogram)
frequencies, times, spectrogram_data = spectrogram(signal, fs=sampling_rate)
plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram_data))
plt.title("Spektrogram sygnału")
plt.xlabel("Czas [s]")
plt.ylabel("Częstotliwość [Hz]")
plt.colorbar(label="Amplituda [dB]")
plt.show()
