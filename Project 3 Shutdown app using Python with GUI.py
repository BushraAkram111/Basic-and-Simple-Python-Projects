import tkinter as tk
import os

def shutdown():
    """This function shuts down the app."""
    os.system("shutdown /s")

def restart():
    """This function restarts the app."""
    os.system("shutdown /r")

def restart_time(time):
    """This function restarts the app after a specified time."""
    os.system(f"shutdown /r /t {time}")

def logout():
    """This function logs out of the app."""
    os.system("shutdown /l")

root = tk.Tk()
root.title("Shutdown App")
root.geometry("200x200")
root.config(background="Black")

button_shutdown = tk.Button(root, text="Shutdown", command=shutdown)
button_shutdown.pack()

button_restart = tk.Button(root, text="Restart", command=restart)
button_restart.pack()

label_restart_time = tk.Label(root, text="Restart time (in seconds):")
label_restart_time.pack()

entry_restart_time = tk.Entry(root)
entry_restart_time.pack()

button_restart_time = tk.Button(root, text="Restart after", command=lambda: restart_time(int(entry_restart_time.get())))
button_restart_time.pack()

button_logout = tk.Button(root, text="Logout", command=logout)
button_logout.pack()

root.mainloop()