import sys
import wave
import contextlib
from openai_whisper import transcribe
from tqdm import tqdm

def count_words(transcription, words):
    count = 0
    for word in transcription['segments']:
        if word['text'].lower() in words:
            count += 1
    return count

def main(audio_file_path):
    with contextlib.closing(wave.open(audio_file_path, 'r')) as f:
        duration = f.getnframes() / float(f.getframerate())
    
    transcription = transcribe(audio_file_path)
    words_to_count = ['guys', 'guise', 'skies']
    word_count = count_words(transcription, words_to_count)
    
    print(f"Total matches of 'guys', 'guise', and 'skies': {word_count}")
    for segment in transcription['segments']:
        if segment['text'].lower() in words_to_count:
            start_time = segment['start']
            end_time = segment['end']
            print(f"Match found at {start_time:.2f} to {end_time:.2f} seconds")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <audio_file_path>")
    else:
        main(sys.argv[1])
