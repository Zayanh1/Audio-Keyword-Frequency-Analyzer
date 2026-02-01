import os
from pydub import AudioSegment

def create_silent_audio(duration=2000):  # Duration in milliseconds
    silent_segment = AudioSegment.silent(duration=duration)
    silent_segment.export("silent_test.wav", format="wav")

if __name__ == "__main__":
    create_silent_audio()
