import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    # listen for the user's input
    audio = r.listen(source)

    try:
        # use Google Speech Recognition to convert audio to text
        text = r.recognize_google(audio)
        print("You said: " + text)

        # write the text to a file
        with open("output.txt", "w") as file:
            file.write(text)
            print("Text written to file.")

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
