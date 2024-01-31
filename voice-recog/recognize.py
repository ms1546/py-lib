import speech_recognition as sr


audio_file = "./sample.wav"

recognizer = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)
    try:
        # Googleの音声認識API
        text = recognizer.recognize_google(audio_data, language="ja-JP")
        print(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
