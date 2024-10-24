from googletrans import Translator


def translate_text_auto(text, dest_lang):
    translator = Translator()
    try:
        # Automatically detect the source language and translate
        translated = translator.translate(text, dest=dest_lang)
        return translated.text, translated.src  # Return both translated text and detected source language
    except Exception as e:
        return f"Error: {str(e)}", None


def main():
    print("Language Converter (Auto Detect)")
    print("Supported languages: English (en), French (fr), Spanish (es), German (de), Urdu (ur), etc.")

    dest_lang = input("Enter destination language code (e.g., 'fr' for French): ").strip()
    text = input("Enter the text to translate: ").strip()

    translated_text, detected_lang = translate_text_auto(text, dest_lang)

    if detected_lang:
        print(f"Detected Language: {detected_lang}")
        print(f"Translated Text: {translated_text}")
    else:
        print(translated_text)


if __name__ == "__main__":
    main()
