import pyttsx3



if __name__=="__main__" :
    print("Welcome to RoboSpeaker , created by Professor ")
    engine = pyttsx3.init()
    while True :
        x = input("What would you like me to speak : ")
        if x == "exit" :
            engine.say("Goodbye my dear Friend")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()    


# pyttsx3 is a library that converts text --> speech

# say() is an inbuilt function in the pyttsx3 , where the system speaks to user.

# runAndwait() is a inbuilt function in the pyttsx3 , is a start speech synthesis engine and block application until engine (system) has finished speaking.

# init() is a factory function to get a reference to pyttsx3.

# if _name_ == '__main__' to only run the code inside the if statement when the program is run directly by the Python interpreter.



