import tkinter as tk
import os

def shutdown():
  os.system("shutdown /s /t 1")

def restart():
  os.system("shutdown /r /t 1")

def logout():
  os.system("shutdown -l")

def execute_command(command):
  os.system(command)

root = tk.Tk()
root.title("Shutdown App")

# Create the buttons
shutdown_button = tk.Button(root, text="Shutdown", command=shutdown)
restart_button = tk.Button(root, text="Restart", command=restart)
logout_button = tk.Button(root, text="Logout", command=logout)

# Place the buttons
shutdown_button.pack()
restart_button.pack()
logout_button.pack()

# Add a command entry field
command_entry = tk.Entry(root)
command_entry.pack()

# Add a button to execute the command
command_button = tk.Button(root, text="Execute", command=lambda: execute_command(command_entry.get()))
command_button.pack()

root.mainloop()