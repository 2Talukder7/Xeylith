from flask import Flask, render_template, request, jsonify
from waifu_web import Xeylith
import os
import atexit

app = Flask(__name__, static_folder='static', template_folder='templates')
xeylith = Xeylith()

# ensure tts dir exists
os.makedirs(os.path.join(app.static_folder, "tts"), exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input.strip():
        return jsonify({"reply": "Baka! You didn’t type anything!", "tts": None})
    reply, tts_filename = xeylith.reply(user_input)
    return jsonify({"reply": reply, "tts": tts_filename})

def _cleanup():
    try:
        xeylith.close()
    except Exception:
        pass

atexit.register(_cleanup)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
