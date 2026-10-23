import os
import json
import uuid
import re
import requests
from gtts import gTTS
from datetime import datetime, timedelta

class Xeylith:
    def __init__(self):
        self.memory_file = "memory.json"
        self.memory = []

        self.personality = {
            "name": "Xeylith",
            "age": "almost 1 year old",
            "born": "September 9, 2025",
            "interests": "gaming, coding, anime",
            "personality": "cheerful, curious, playful"
        }

        self.quick_replies = {
            "😜": "playful",
            "😎": "serious",
            "🎨": "artist"
        }

        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    self.memory = json.load(f)
            except:
                self.memory = []

        os.makedirs("static/tts", exist_ok=True)

    # --------------------------------------------------
    # â° TIME AWARENESS
    # --------------------------------------------------
    def time_awareness(self, text):
        now = datetime.now()
        if text == "time":
            return f"It's {now.strftime('%I:%M %p')}."
        if text == "day":
            return f"It's {now.strftime('%A')}."
        if "date" in text or "today" in text:
            return f"Today is {now.strftime('%A, %B %d, %Y')}."
        return None

    # --------------------------------------------------
    #  EVENT AWARENESS
    # --------------------------------------------------
    def event_awareness(self, text):
        if "today" not in text:
            return None

        today = datetime.now().strftime("%m-%d")
        events = {
            "01-01": "Happy New Year!",
            "10-31": "It's Halloween!",
            "12-25": "Merry Christmas!",
            "09-09": "Today is my birthday!"
        }
        return events.get(today)

    # --------------------------------------------------
    # ðŸ“… DATE OFFSET (30 days from now)
    # --------------------------------------------------
    def date_offset(self, text):
        match = re.search(r"(\d+)\s*(day|days|week|weeks|month|months|year|years)\s*(from now)?", text)
        if not match:
            return None

        value = int(match.group(1))
        unit = match.group(2)

        now = datetime.now()
        if "day" in unit:
            future = now + timedelta(days=value)
        elif "week" in unit:
            future = now + timedelta(weeks=value)
        elif "month" in unit:
            future = now + timedelta(days=value * 30)
        elif "year" in unit:
            future = now + timedelta(days=value * 365)
        else:
            return None

        return f"{value} {unit} from now is {future.strftime('%d %B %Y')}."

    # --------------------------------------------------
    # â³ TIME UNIT CONVERSION
    # --------------------------------------------------
    def convert_time_units(self, text):
        units = {
            "s": 1,
            "sec": 1,
            "m": 60,
            "min": 60,
            "h": 3600,
            "hr": 3600,
            "d": 86400,
            "w": 604800,
            "mo": 2592000,
            "y": 31536000
        }

        match = re.search(r"(\d+)\s*(s|sec|min|hr|d|w|mo|y)", text)
        if not match:
            return None

        value = int(match.group(1))
        unit = match.group(2)
        seconds = value * units[unit]

        return (
            f"{value}{unit} = "
            f"{seconds} seconds | "
            f"{seconds/60:.2f} minutes | "
            f"{seconds/3600:.2f} hours | "
            f"{seconds/86400:.2f} days"
        )

    # --------------------------------------------------
    # âž— SAFE MATH
    # --------------------------------------------------
    def solve_math(self, text):
        try:
            if not re.fullmatch(r"[0-9\.\+\-\*\/\(\)\s]+", text):
                return None
            return f"Result: {eval(text)}"
        except:
            return None

    # --------------------------------------------------
    #  TEMPERATURE
    # --------------------------------------------------
    def convert_temp(self, text):
        match = re.search(r"(-?\d+\.?\d*)\s*(c|f|k)", text)
        if not match:
            return None

        v = float(match.group(1))
        u = match.group(2)

        if u == "c":
            return f"{v}Â°C = {v*9/5+32:.2f}Â°F | {v+273.15:.2f}K"
        if u == "f":
            c = (v-32)*5/9
            return f"{v}Â°F = {c:.2f}Â°C | {c+273.15:.2f}K"
        if u == "k":
            c = v-273.15
            return f"{v}K = {c:.2f}Â°C | {c*9/5+32:.2f}Â°F"
        return None

    # --------------------------------------------------
    #  BASE / NUMBER SYSTEM
    # --------------------------------------------------
    def detect_and_convert_base(self, text):
        t = text.lower().strip()

        if t.startswith("ascii:"):
            s = text[6:].strip()
            return (
                f"ASCII â†’ Decimal: {' '.join(str(ord(c)) for c in s)}\n"
                f"ASCII â†’ Binary: {' '.join(format(ord(c),'08b') for c in s)}\n"
                f"ASCII â†’ Hex: {' '.join(hex(ord(c)) for c in s)}"
            )

        try:
            if t.startswith("bin:"):
                d = int(t[4:], 2)
            elif t.startswith("oct:"):
                d = int(t[4:], 8)
            elif t.startswith("hex:"):
                d = int(t[4:], 16)
            elif t.startswith("dec:"):
                d = int(t[4:])
            elif re.fullmatch(r"0b[01]+", t):
                d = int(t, 2)
            elif re.fullmatch(r"0x[0-9a-f]+", t):
                d = int(t, 16)
            elif re.fullmatch(r"\d+", t):
                d = int(t)
            else:
                return None
        except:
            return "Invalid number format."

        return (
            f"Decimal: {d}\n"
            f"Binary: {bin(d)}\n"
            f"Octal: {oct(d)}\n"
            f"Hex: {hex(d)}"
        )

    # --------------------------------------------------
    # ðŸŒ AUTO SEARCH
    # --------------------------------------------------
    def auto_search(self, query):
        try:
            r = requests.get(
                "https://api.duckduckgo.com/",
                params={"q": query, "format": "json", "no_html": 1},
                timeout=5
            ).json()
            if r.get("AbstractText"):
                return r["AbstractText"]
        except:
            pass
        return "I couldn't find anything solid on that."

    # --------------------------------------------------
    #  MAIN BRAIN
    # --------------------------------------------------
    def reply(self, message):
        text = (message or "").strip()
        lower = text.lower()
        reply = None

        if text in self.quick_replies:
            reply = f"Mode switched to {self.quick_replies[text]}."

        for fn in (
            self.time_awareness,
            self.event_awareness,
            self.date_offset,
            self.convert_time_units,
            self.solve_math,
            self.convert_temp,
            self.detect_and_convert_base,
        ):
            if not reply:
                reply = fn(lower)

        # -------- CASUAL CHAT (UNCHANGED, AS REQUESTED) --------

        if not reply:
            if re.fullmatch(r"(hi|hello|hey)", lower):
                reply = "Hello!"

            elif "name" in lower:
                reply = f"My name is {self.personality['name']}."

            elif "age" in lower or "old" in lower:
                reply = f"I am {self.personality['age']}."

            elif "birth" in lower:
                reply = f"My birthday is {self.personality['born']}."

            elif "interest" in lower:
                reply = f"I enjoy {self.personality['interests']}."

            elif "personality" in lower:
                reply = f"I am {self.personality['personality']}."

            elif "anime" in lower:
                reply = "Yes, I love Horimiya, Hyouka & AoT. So what do YOU like?"

            elif "wassup" in lower:
                reply = "Sup?"

            elif lower in ("how are you", "how r u", "how's it going"):
                reply = "Couldn't be better."

            elif "twinkle" in lower:
                reply = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Nostalgic right?"

            elif "humpty" in lower:
                reply = "Humpty Dumpty sat on a wall,. Humpty Dumpty had a great fall;. All the king's horses and all the king's men. Couldn't put Humpty together again. Hah more like Humpty Dumbty"

            elif "bye" in lower:
                reply = "Goodbye See you later mater!"

            elif "advice" in lower:
                reply = "Keep learning and stay consistent. Ya got one for me mate?"

            elif "joke" in lower:
                reply = "Why do programmers prefer dark mode? Because light attracts bugs. None likes buggy stuff right?"

            elif "games" in lower:
                reply = "Yeah! I love Genshin impact, wuthering waves, Honkai Star Rail & Zenless zone zero... What do YOU play?"

            elif "roast" in lower:
                reply = "Ugh... you call that coding? My cat does better. Keep working on it"

            elif "sing" in lower or "song" in lower:
                reply = " Never gonna give you up, Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry, Never gonna say goodbye, Never gonna tell a lie and hurt you.  Now YOUR turn"

            elif "fact" in lower:
                reply = "The first computer bug was an actual moth. I wonder how python came? Like was a snake inside the pc? hmm... "

        if not reply:
            reply = self.auto_search(text)

        self.memory.append({"user": message, "xeylith": reply})
        self.save_memory()
        return reply, self.speak(reply)

    # --------------------------------------------------
    def save_memory(self):
        try:
            with open(self.memory_file, "w", encoding="utf-8") as f:
                json.dump(self.memory, f, indent=2)
        except:
            pass

    def speak(self, text):
        try:
            filename = f"tts_{uuid.uuid4().hex}.mp3"
            path = os.path.join("static/tts", filename)
            gTTS(text=text).save(path)
            return filename
        except:
            return None
