from deep_translator import GoogleTranslator
from gtts import gTTS
import sys

def translate_text(text, direction):
    if direction == 'ja-to-en':
        translated_text = GoogleTranslator(source='ja', target='en').translate(text)
    elif direction == 'en-to-ja':
        translated_text = GoogleTranslator(source='en', target='ja').translate(text)
    else:
        raise ValueError("Unsupported translation direction. Use 'ja-to-en' or 'en-to-ja'.")
    return translated_text

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang)
    filename = "output.mp3"
    tts.save(filename)
    print(f"Audio saved as {filename}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python translate_tts_main.py <direction> '<text>'")
        sys.exit(1)

    direction = sys.argv[1]
    text = sys.argv[2]
    target_lang = 'en' if direction == 'ja-to-en' else 'ja'

    try:
        translated_text = translate_text(text, direction)
        print(f"Translated Text: {translated_text}")
        text_to_speech(translated_text, target_lang)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
