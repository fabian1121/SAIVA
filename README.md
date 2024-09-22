# SAIVA: Smart Artificially Intelligent Voice Assistant

SAIVA is a Smart Artificially Intelligent Voice Assistant designed to perform a wide range of tasks using voice commands and gesture controls. This AI-based virtual personal assistant (VPA) allows users to efficiently manage day-to-day activities, offering features like facial authentication, weather updates, email management, voice-based system commands, and more. The project was developed using Python and various libraries, offering seamless interaction between users and their laptops through natural voice commands and gestures.

## Overview
SAIVA is an AI-powered virtual assistant built for laptop users to facilitate tasks via voice and gesture commands. The assistant enhances productivity by providing features such as voice-based system control, task scheduling, email management, and multimedia operations. The assistant can interact with various APIs to fetch information like weather updates, current news, mathematical calculations, translations, and more.

## Features
- **Facial Authentication**: SAIVA uses facial recognition to unlock the system securely.
- **Voice Commands**: Control your system through voice, including opening applications, fetching files, sending emails, and more.
- **Gesture Controls**: Allows volume and brightness control via gestures recognized by the webcam.
- **Weather and News Updates**: Get the latest weather and news using voice commands.
- **Selfie Function**: Capture a selfie using the webcam with a simple voice command.
- **Translate and Define Functions**: Translate words between languages and get word definitions using built-in voice commands.
- **Mathematical Functions**: Solve mathematical problems with just a voice request.
- **Email Management**: Compose, send, and manage emails through voice commands.
- **System Information**: Get battery status and system info on request.
- **Wikipedia Lookup**: Use voice commands to search for information on Wikipedia.
- **Map Directions**: Ask for directions between two places, and SAIVA will provide the best routes.

## Technologies and Python Libraries Used
- **Pyttsx3**: Text-to-speech conversion library used to provide SAIVA's voice response.
- **SpeechRecognition**: Used to recognize and process the user's spoken commands.
- **PyAudio**: Provides audio input/output, essential for capturing voice commands and audio playback.
- **OpenCV**: Used for gesture recognition and facial authentication through the laptop's webcam.
- **NewsAPI**: Fetches the latest news based on user preferences.
- **OpenWeatherAPI**: Provides real-time weather updates.
- **Wolfram Alpha API**: For performing advanced mathematical functions.
- **Tkinter**: GUI library used to build the interface for interaction.

## Commands
SAIVA can execute a wide variety of voice commands, including but not limited to:
- **"What’s the weather today?"** – Fetches current weather.
- **"Show me the news."** – Displays the top 10 headlines.
- **"Solve [mathematical problem]"** – Solves a mathematical problem using the Wolfram Alpha API.
- **"Translate [word] to [language]"** – Translates words into the requested language.
- **"Take a selfie"** – Captures a selfie using the webcam.
- **"Send an email"** – Manages email sending and recipient info.
- **"Define [word]"** – Provides definitions of words.
- **"What’s the battery percentage?"** – Displays battery information.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/saiva.git
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run SAIVA:
   ```bash
   python main.py
   ```

## Demo Video
For a detailed walkthrough of SAIVA's features, [click here to watch the demo](https://shorturl.at/Zjb5t).

## Future Scope
- **Improved NLP**: Enhanced Natural Language Processing for more natural conversations and responses.
- **Home Automation**: Integrating SAIVA with home automation tools to control smart devices.
- **Medical Assistance**: Future versions can aid medical professionals by tracking patient data and providing insights.
- **Self-Driving Integration**: In the long run, SAIVA can be integrated with autonomous driving systems to assist drivers.
- **Enhanced AI with Machine Learning**: Incorporating machine learning models to improve performance and adaptability with continuous user interactions.



