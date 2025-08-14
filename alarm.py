#adding alarm feature

import tkinter as tk
from tkinter import messagebox
from time import strftime
import threading
import time
import winsound  # Works on Windows; for Mac/Linux, you can use `playsound`

alarm_time = None
alarm_active = False

# Function to update the clock
def update_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    if alarm_active and current_time == alarm_time:
        threading.Thread(target=ring_alarm).start()
    label.after(1000, update_time)

# Function to set the alarm
def set_alarm():
    global alarm_time, alarm_active
    alarm_time = alarm_entry.get().strip()
    if alarm_time:
        alarm_active = True
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    else:
        messagebox.showerror("Error", "Please enter a valid time (HH:MM:SS AM/PM)")

# Function to stop the alarm
def stop_alarm():
    global alarm_active
    alarm_active = False
    messagebox.showinfo("Alarm Stopped", "Alarm has been stopped.")

# Function to play alarm sound
def ring_alarm():
    global alarm_active
    messagebox.showinfo("Alarm!", "Wake up!")
    for _ in range(5):  # Repeat 5 times
        winsound.Beep(1000, 500)  # 1000 Hz for 0.5 seconds
        time.sleep(0.5)
    alarm_active = False

# Tkinter UI setup
root = tk.Tk()
root.title("Digital Clock with Alarm")

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center', pady=20)

frame = tk.Frame(root)
frame.pack(pady=10)

alarm_entry = tk.Entry(frame, font=('calibri', 14))
alarm_entry.grid(row=0, column=0, padx=5)
set_btn = tk.Button(frame, text="Set Alarm", command=set_alarm)
set_btn.grid(row=0, column=1, padx=5)
stop_btn = tk.Button(frame, text="Stop Alarm", command=stop_alarm)
stop_btn.grid(row=0, column=2, padx=5)

update_time()

root.mainloop()
