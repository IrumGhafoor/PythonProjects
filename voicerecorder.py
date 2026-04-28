import sounddevice as sd
from scipy.io.wavfile import write
import time

freq = 44100

input("Press ENTER to start recording")

duration = int(input("Enter recording duration in seconds: "))

print("Recording started...")

recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

for i in range(duration):
    print(f"Recording... {i+1} sec")
    time.sleep(1)

sd.wait()

write("recording.wav", freq, recording)

print("Recording finished and saved as recording.wav")