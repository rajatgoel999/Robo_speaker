import win32com.client # type: ignore

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    x = str(input("Enter what you want me to say (or enter 'q' to quit): "))
    if x == 'q':
        speaker.Speak("Bye Bye")
        break
    speaker.Speak(x)