# Xeylith — AI Character Companion

Xeylith is an experimental AI companion project exploring conversational AI, character personality, useful everyday utilities, and interactive web experiences.

🌐 **Live Demo:** https://xeylith.onrender.com

## Current Features

- **Web-based chat:** Talk to Xeylith through a browser-based interface.
- **Character personality:** Cheerful, curious, playful responses with gaming and anime-inspired conversations.
- **Quick-reply modes:** Use emoji controls to switch between Playful 😜, Serious 😎, and Artist 🎨 modes.
- **Time and date awareness:** Ask for the current time, day, or date.
- **Date calculations:** Calculate future dates using day, week, month, or year inputs.
- **Time-unit conversion:** Convert time values into seconds, minutes, hours, and days.
- **Mathematical calculations:** Evaluate basic arithmetic expressions.
- **Temperature conversion:** Convert between Celsius, Fahrenheit, and Kelvin.
- **Number-system conversion:** Convert supported decimal, binary, octal, and hexadecimal values.
- **ASCII conversion:** Convert text characters into their decimal, binary, and hexadecimal representations.
- **Event awareness:** Respond to selected dates and occasions, including New Year, Halloween, Christmas, and Xeylith's birthday.
- **Casual interactions:** Try greetings, jokes, facts, advice, anime and gaming conversations, songs, and playful roasts.
- **Text-to-speech:** Attempts to generate spoken replies using Google Text-to-Speech (gTTS).
- **Conversation logging:** The backend saves conversation entries to a local JSON memory file when file access is available.

## What Can You Ask Xeylith?

Enter a message in the chat interface. These are examples of supported input patterns.

| Input example | Function |
|---|---|
| `time` | Current time |
| `day` | Current day of the week |
| `date` or `today` | Current date |
| `7 days from now` | Future-date calculation |
| `60 sec` | Time-unit conversion |
| `25 * 4` | Arithmetic calculation |
| `32 c` | Temperature conversion |
| `bin:1010` | Binary-to-number conversion |
| `hex:FF` | Hexadecimal-to-number conversion |
| `dec:42` | Decimal-to-number conversion |
| `oct:17` | Octal-to-number conversion |
| `ascii:Hello` | ASCII representations of text |
| `joke` | A programming joke |
| `anime` | Anime-related conversation |
| `games` | Gaming-related conversation |
| `😜` | Switch to Playful mode |
| `😎` | Switch to Serious mode |
| `🎨` | Switch to Artist mode |

Some commands use specific input formats. General conversational questions may receive a predefined response or trigger the web-search fallback. Search results, speech generation, and persistent storage depend on network access and deployment configuration.

## Technologies

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Text-to-speech:** gTTS
- **Web-search fallback:** DuckDuckGo Instant Answer API
- **Data storage:** Local JSON file for conversation entries

## Run Locally

### Requirements

- Python installed on your system
- Dependencies listed in `XeylithWeb/requirements.txt`

### Installation

1. Clone or download this repository.
2. Open PowerShell in the repository directory.
3. Install the dependencies:

   ```powershell
   cd XeylithWeb
   python -m pip install -r requirements.txt
   ```

4. Start the Flask application:

   ```powershell
   python app.py
   ```

5. Open the following address in your browser:

   `http://127.0.0.1:5000`

## Development Status

Xeylith is a work in progress. The features listed above describe the current codebase; availability may vary depending on the environment and configuration.

The 3D avatar, VSeeFace integration, advanced AI reasoning, richer long-term memory, and additional interactive character features are experimental or planned and should not be considered fully available in the online version unless separately verified.

## Roadmap

- Improve conversational quality and context handling.
- Improve reliability and usability.
- Expand character interactions and personality controls.
- Explore more capable AI integrations.
- Develop and verify 3D character and avatar integration.
- Explore future desktop and mobile application options.

These are future goals, not claims of completed functionality.

## Attribution and License

Xeylith is based on the ai-waifu project by Yaroslav Demchenko, originally released under the MIT License.

Xeylith includes modifications and additional work built upon the original project. The original copyright notice and MIT license terms are preserved.

See the root-level `LICENSE` file for the applicable license notice.
