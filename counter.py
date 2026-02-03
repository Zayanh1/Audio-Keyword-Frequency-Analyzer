import whisper
import torch
import datetime

# 1. Use CPU if MPS is hanging (sometimes more stable for long files)
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"🚀 Device: {device.upper()}")

# 2. Load 'base' - it's the best balance for a MacBook Air
model = whisper.load_model("base").to(device)

def analyze_audio(file_path):
    target_words = ["guys", "guise", "skies"]
    print(f"🎙️ Processing... (Press Ctrl+C to stop)")
    
    # verbose=True will show you the text as it's processed
    # initial_prompt helps the AI focus on your keywords
    result = model.transcribe(
        file_path, 
        fp16=False, 
        verbose=True, 
        initial_prompt="guys, guise, skies"
    )
    
    matches = []
    for segment in result['segments']:
        text = segment['text'].lower()
        words_in_segment = text.replace('.', '').replace(',', '').split()
        
        for target in target_words:
            if target in words_in_segment:
                timestamp = str(datetime.timedelta(seconds=int(segment['start'])))
                matches.append((timestamp, target, segment['text'].strip()))

    print("\n" + "="*30)
    print(f"📊 FINAL REPORT")
    print("="*30)
    for time, word, context in matches:
        print(f"[{time}] Found '{word}': \"{context}\"")
    
    print(f"\n✅ Total occurrences: {len(matches)}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python counter.py your_audio_file.mp3")
    else:
        analyze_audio(sys.argv[1])
