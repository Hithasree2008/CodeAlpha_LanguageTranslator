from flask import Flask, render_template, request
from deep_translator import MyMemoryTranslator

app = Flask(__name__)

languages = {
    
    "English": "en-GB",
    "Telugu": "te-IN",
    "Hindi": "hi-IN",
    "Tamil": "ta-IN",
    "Kannada": "kn-IN",
    "Malayalam": "ml-IN",
    "French": "fr-FR",
    "Spanish": "es-ES",
    "German": "de-DE",
    "Japanese": "ja-JP"

}


@app.route("/", methods=["GET", "POST"])
def home():

    translated_text = ""
    original_text = ""
    source_language = "English"
    target_language = "Telugu"

    if request.method == "POST":

        original_text = request.form["text"]
        source_language = request.form["source_language"]
        target_language = request.form["target_language"]

        try:

            translated_text = MyMemoryTranslator(
    source=languages[source_language],
    target=languages[target_language]
).translate(original_text)

        except Exception as e:

            translated_text = f"Translation failed: {e}"

    return render_template(
        "index.html",
        languages=languages,
        translated_text=translated_text,
        original_text=original_text,
        source_language=source_language,
        target_language=target_language
    )


if __name__ == "__main__":
    app.run(debug=True)