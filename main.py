from intent_recognition import IntentClassifier

def main():
    # recognizer = IntentClassifier()
    # recognizer.train()
    # recognizer.save("classifier.pickle")
    recognizer = IntentClassifier.load("classifier.pickle")
    # recognizer.update([("How are you?", "hello")])
    # recognizer.addResponse("Sometimes, cry out loud might help.", "sad")
    print("Test Accuracy:", recognizer.test())

    # User Interaction
    text = input("\nDemo\nInput: ")
    while text:
        print("Intent:", recognizer.classify(text))
        print("Response:", recognizer.response(text) + "\n")
        text = input("Input: ")

if __name__ == "__main__":
    main()

