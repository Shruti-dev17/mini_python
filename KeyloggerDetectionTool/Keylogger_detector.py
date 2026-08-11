
import customtkinter as ctk
import os
import glob
import time
import threading

#****************************************************************
# Keylogger Detection Application (Real-Time Monitoring)
#****************************************************************
class KeyloggerDetector:

    def __init__(self, gui_callback):
        self.running = False
        self.gui_callback = gui_callback
        self.files_status = {}
    def start(self):
        self.running = True
        t=threading.Thread(target=self.monitor ,daemon=True)
        t.start()

    def stop(self):
        self.running = False

    def monitor(self):
        while self.running:
            self.check_logs()
            time.sleep(5)  # Check every 5 seconds

    def check_logs(self):
        current_dir = os.getcwd()
        for file in glob.glob(os.path.join(current_dir,"*.txt")):
            try:
                stat=os.stat(file)
                last_modified=stat.st_mtime
                size=stat.st_size
                if file not in self.files_status:
                    self.files_status[file] = (last_modified, size)
                else:
                    prev_modified, prev_size = self.files_status[file]
                    if last_modified != prev_modified or size != prev_size:
                        self.files_status[file] = (last_modified, size)
                        self.gui_callback(f"[ALERT] File modified: {file} ")

            except FileNotFoundError:
                continue


#****************************************************************
# GUI Application
# ****************************************************************


class DetectorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Keylogger Detection(text file monitoring)")
        self.geometry("700x500")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.detector = KeyloggerDetector(self.add_alert)

        #Title Label
        self.label = ctk.CTkLabel(self, text="Keylogger Detection", font=("Arial", 24 ,"bold"))
        self.label.pack(pady=20)

        #Buttons 
        self.start_button = ctk.CTkButton(self, text="Start Detection", command=self.start_detection, width=200, height=40)
        self.start_button.pack(pady=10)

        self.stop_button = ctk.CTkButton(self, text="Stop Detection", command=self.stop_detection, width=200, height=40)
        self.stop_button.pack(pady=10)

        #Status Box
        self.status_label = ctk.CTkLabel(self, text="Detection Status:Stopped", font=("Arial", 18))
        self.status_label.pack(pady=10)

        #Alerts Box
        self.alerts_box = ctk.CTkTextbox(self, width=600, height=250, font=("consolas", 16))
        self.alerts_box.pack(pady=10)

    def start_detection(self):
        self.detector.start()
        self.status_label.configure(text="Detection Status: Running/Monitoring..." )   

    def stop_detection(self):
        self.detector.stop()
        self.status_label.configure(text="Detection Status: Stopped") 

    def add_alert(self, message):
        msg=f"[ALERT] file change detected: {message}"
        self.alerts_box.insert("end" , msg + "\n")
        self.alerts_box.see("end")

#****************************************************************
# Main Function
# ****************************************************************   

if __name__ == "__main__":
    app = DetectorApp()
    app.mainloop() 

        