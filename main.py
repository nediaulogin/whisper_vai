import whisper

model = whisper.load_model("base")
result = model.transcribe("video_sound.mp3")


with open("transcription.json", "w") as f:
    f.write(result["text"])

with open("transcription.json", "r") as f:
    content = f.read()
    print(content)