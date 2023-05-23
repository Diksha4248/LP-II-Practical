# import datetime
import webbrowser
from datetime import datetime


def wishme():
    # hour = int(datetime.datetime.now().hour)

    now = datetime.now()
    current_time = now.strftime("%H:%S:%S")

    print("current time is : ",current_time)

    # if hour>=0 and hour<12:
    #     print("Good Morning!")

    # elif hour>=12 and hour<18:
    #     print("Good Afternoon!")   

    # else:
    #     print("Good Evening!")  

    print("Hi , I am your assistant. Please tell me how may I help you ?")  


questions = {
    "how are you ?" :"I am fine",
    "tell me your name " : " Chattzz is my name",
    "whats your age" : "I was created today , so my age is 0 days",
    "what is your favorite food":"dosa"
}

if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = input() #Converting user query into lower case

        print("the query is :",query)

        # Logic for executing tasks based on query
        if 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")    

        elif query in questions.keys():
            print(questions[query])    

        else:
            print("Enter a valid command")    
