import whisper


model = whisper.load_model("base")
audio_file = "./sample.wav"
result = model.transcribe(audio_file)

print(result["text"])
