import os
from pydub import AudioSegment
from tqdm import tqdm

def create_silent_audio(duration=2000):  # Duration in milliseconds
    silent_segment = AudioSegment.silent(duration=duration)
    silent_segment.export("silent_test.wav", format="wav")

if __name__ == "__main__":
    for i in tqdm(range(100)):  # Simulate progress bar
        pass
    create_silent_audio()
