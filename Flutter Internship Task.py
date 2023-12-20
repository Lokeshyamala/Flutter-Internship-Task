import tkinter as tk
from tkinter import ttk
import datetime
import winsound  

def set_reminder():
    selected_day = day_var.get()
    selected_time = time_var.get()
    selected_activity = activity_var.get()

    now = datetime.datetime.now()
    reminder_time = datetime.datetime.strptime(f"{selected_day} {selected_time}", "%A %H:%M")

    
    if now > reminder_time:
        reminder_time += datetime.timedelta(days=1)

    time_difference = reminder_time - now
    seconds_until_reminder = time_difference.total_seconds()

    
    root.after(int(seconds_until_reminder * 1000), play_sound)

def play_sound():
    winsound.PlaySound("sound.wav", winsound.SND_FILENAME)


root = tk.Tk()
root.title("Daily Reminder App")


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_var = tk.StringVar()
day_dropdown = ttk.Combobox(root, textvariable=day_var, values=days)
day_dropdown.set("Monday")
day_dropdown.grid(row=0, column=0, padx=10, pady=10)


times = [f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in range(0, 60, 5)]
time_var = tk.StringVar()
time_dropdown = ttk.Combobox(root, textvariable=time_var, values=times)
time_dropdown.set("08:00")  
time_dropdown.grid(row=0, column=1, padx=10, pady=10)

activities = ["Wake up", "Go to gym", "Breakfast", "Meetings", "Lunch", "Quick nap", "Go to library", "Dinner", "Go to sleep"]
activity_var = tk.StringVar()
activity_dropdown = ttk.Combobox(root, textvariable=activity_var, values=activities)
activity_dropdown.set("Wake up")  
activity_dropdown.grid(row=0, column=2, padx=10, pady=10)


reminder_button = tk.Button(root, text="Set Reminder", command=set_reminder)
reminder_button.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()
