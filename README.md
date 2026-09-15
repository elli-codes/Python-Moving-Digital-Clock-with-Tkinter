# Python-Moving-Digital-Clock-with-Tkinter
A simple Python GUI project that creates a transparent, borderless digital clock using Tkinter.

The clock displays the current system time and continuously moves across the screen. The project demonstrates how to create a custom Tkinter window, update its contents in real time, control window transparency and position, and schedule repeated functions using after().

✨ Features:
🕒 Displays the current time in HH:MM:SS format
🪟 Borderless window
🎨 Custom background and text styling
🌫️ Semi-transparent window
📌 Always stays on top of other windows
➡️ Moves continuously across the screen
🔄 Automatically updates the time every second
♻️ Uses Tkinter's after() method for repeated tasks
📦 Implemented using a simple Python class

🛠️ Technologies Used:
Python 3
Tkinter
time module

No external Python packages are required.

⚙️ How It Works

The program is organized around a Python class:

class my_class:

When the class is created, the application:

Creates the Tkinter window.
Configures the window appearance.
Creates the clock label.
Starts the clock update function.
Starts the window movement function.
Enters the Tkinter event loop.


🌫️ Window Transparency

The transparency is configured using:

self.root.wm_attributes("-alpha", 0.6)

The value:

0.6

makes the window partially transparent.
🖥️📽️YouTube video link:https://youtu.be/wWZHeVyr5Eg 
