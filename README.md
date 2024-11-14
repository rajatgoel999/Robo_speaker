Text-to-Speech Python Script
This repository contains a simple Python script that uses the Windows Speech API (SAPI.SpVoice) to convert text input into speech. Users can type text into the console, and the computer will read it aloud. The program continues running until the user enters 'q' to quit.

---Requirements---
1. Python: Ensure you have Python installed (version 3.x recommended).

2. Windows OS: This script relies on the Windows Speech API, so it only works on Windows.
win32com.client library: Install the pywin32 package to enable the win32com.client library.

---Installation---
1. Clone the repository:
    git clone https://github.com/yourusername/text-to-speech-python.git
    cd text-to-speech-python
   
3. Install the pywin32 library:
   pip install pywin32
   
---Usage---
1. Run the script:
    python tts_script.py
   
3. Follow the prompt in the console:
    Enter text to have it spoken aloud.
    Type 'q' and press Enter to quit the program.

---Example---

  -->Enter what you want me to say (or enter 'q' to quit): Hello, World!
  
  -->*Computer speaks*: "Hello, World!"
  
  -->Enter what you want me to say (or enter 'q' to quit): q
  
  -->*Computer speaks*: "Bye Bye"
