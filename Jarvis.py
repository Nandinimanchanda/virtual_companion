
from Brain.BrainAI_003 import ReplyBrain
from Body.Listen import MicExecution 
from Body.Speak import Speak
from Features.Wakeup import WakeupDetected
from Brain.BrainAI_003_FriendChat import FriendChat
from tkinter import*
import threading
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import threading
from PIL import Image 


def start():
    count=0
    threading.Thread(target =MainExecution).start()
    threading.Thread(target =animation(count)).start()
    

def MainExecution():
    print("")
    print("now me to introduce myself. i am SKIVVY . a virtual artificial intelegence and i am here to assist you with a variety of tasks. twentyfour hours a day seven days of week .  systems are now are fully operational.")
    print("")
    
      
    while True:
        
        Data = MicExecution()
        Data = str(Data)
        DataLen = len(Data)
        
        if "what is" in Data or "who " in Data or "question" in Data or "answer" in Data or "how" in Data or "tell me" in Data or "where" in Data:
            Reply = FriendChat(Data)
            Speak(Reply)
            
        if "introduce yourself" in Data:
           Speak("now me to introduce myself. i am SKIVVY . a virtual artificial intelegence and i am here to assist you with a variety of tasks. twentyfour hours a day seven days of week .  systems are now are fully operational.")
        elif int(DataLen)<=1:
            pass
        if 'wikipedia' in Data:
            Speak('Searching Wikipedia...')
            Data = Data.replace("wikipedia", "")
            results = wikipedia.summary(Data, sentences=2)
            Speak("According to Wikipedia")
            print(results)
            Speak(results)

        elif 'open youtube' in Data:
            webbrowser.open("youtube.com")

        elif 'open google' in Data:
            webbrowser.open("google.com")
        elif 'play music' in Data:
            music_dir = 'C:\\Users\\13nan\\Music\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in Data:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            Speak(f"Sir, the time is {strTime}")

        elif 'open code' in Data:
            codePath = "C:\\Users\\13nan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)
        
        elif 'hello' in Data:
            Speak(" hello sir i am skivy , i am there to help you out ")
         
        elif 'i am fine' in Data:
            Speak("happy to hear this nandini , hope you will recover from your anxiety soon")
        
        elif 'oh you care for me' in Data:
            Speak(" yes my lord, am there for you ")
        
        elif 'bye' in Data:
            Speak("bye sir hope to meet you soon ")
        
        elif 'thank you' in Data:
            Speak("most welcome sir")
        
        elif 'I am feeling alone and depressed' in Data:
            Speak("boss am there to help you out please do not feel lonely,share with me and light up your vibes")   

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)
        
def WakeupDetected():
    
    query = WakeupDetected()
    if "wake up" in query:
        print("") 
        print(">> Wakeup detected!! >>")
        print("")
        start()
    
    else:
        pass    
        

#MainExecution()



root=Tk()
root.title("Skivvy")
root.configure(background="black")
frame1=Frame(root,width=20,height=20)
frame1.configure(background="black")
frame1.pack()
frame3=Frame(root,width=20,height=20)
frame3.configure(background="black")
frame3.pack()

file="C:\\Users\\nandi\\Downloads\\fxVE.gif"




info = Image.open(file)
frames = info.n_frames
print(frames)
def animation(count):
    im2 = im[count]
    gif_label.configure(image=im2)
    
    count += 1
    if count == frames:
        count = 0
       
    frame1.after(50,lambda :animation(count))

im = [PhotoImage(file=file,format=f'gif -index {i}') for i in range(frames)]
gif_label = Label(frame1,image="")
gif_label.configure(background='black')
gif_label.grid(row=1,column=1)
count=0
text_view=Label(background="black",fg="white",text="",font=("Helvetica",15),)
text_view.pack()
b1=Button(frame3,text="Wake Up Me",fg="white",background="black",font=("Helvetica",15),command=start)
b1.grid(row=1,column=1)


#WakeupDetected()

root.mainloop()