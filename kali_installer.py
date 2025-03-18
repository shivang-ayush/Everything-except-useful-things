import tkinter as tk
import random
import time
import threading
import os
from playsound import playsound

# Fake logs and error messages
LOG_MESSAGES = [
    "Checking disk partitions...",
    "Mounting file system...",
    "Extracting core packages...",
    "Installing bootloader...",
    "Configuring network settings...",
    "Setting up user accounts...",
    "Downloading additional drivers...",
    "Configuring system services...",
    "Finalizing installation...",
    "Cleaning up temporary files..."
]

ERROR_MESSAGES = [
    "ERROR: Unable to mount partition...",
    "WARNING: Missing firmware detected...",
    "ERROR: Package download failed, retrying...",
    "WARNING: Low disk space detected...",
    "ERROR: Bootloader installation failed...",
    "WARNING: Unstable network connection..."
]

class KaliInstaller:
    def __init__(self, root):
        self.root = root
        self.root.title("Kali Linux Installer")
        self.root.configure(bg="black")
        self.root.attributes('-fullscreen', True)  # Fullscreen mode to "trap" the user

        self.progress = 0

        # Title Label
        self.title_label = tk.Label(root, text="Installing Kali Linux...", fg="lime", bg="black", font=("Courier", 16))
        self.title_label.pack(pady=10)

        # Progress Bar (Fake)
        self.progress_bar = tk.Canvas(root, width=600, height=30, bg="gray")
        self.progress_bar.pack()

        # Status Label
        self.status_label = tk.Label(root, text="Initializing installation...", fg="lime", bg="black", font=("Courier", 12))
        self.status_label.pack(pady=10)

        # Terminal Log
        self.terminal = tk.Text(root, height=10, width=80, bg="black", fg="lime", font=("Courier", 10), state=tk.DISABLED)
        self.terminal.pack(pady=10)

        # Fake Command Input
        self.command_input = tk.Entry(root, width=50, bg="black", fg="lime", font=("Courier", 12))
        self.command_input.pack(pady=10)
        self.command_input.insert(0, "Type commands here (but nothing works!)")
        self.command_input.bind("<Return>", self.fake_command)

        # Start Installation
        self.update_installation()

    def update_installation(self):
        if self.progress < 99:
            self.progress += random.randint(5, 15)
            if self.progress > 99:
                self.progress = 99
            
            # Update UI
            self.progress_bar.delete("progress")
            self.progress_bar.create_rectangle(0, 0, self.progress * 6, 30, fill="lime", tags="progress")
            self.status_label.config(text=f"Installing... {self.progress}%")

            # Generate log messages
            log = random.choice(LOG_MESSAGES) if random.random() < 0.8 else random.choice(ERROR_MESSAGES)
            self.log_message(log)

            # Randomly play beep sounds
            if random.random() < 0.3:
                threading.Thread(target=self.play_beep_sound).start()

            # Continue progress
            self.root.after(random.randint(500, 2000), self.update_installation)
        else:
            self.status_label.config(text="💀 Kernel Panic!")
            threading.Thread(target=self.play_error_sound).start()
            self.root.after(3000, self.show_kernel_panic)

    def log_message(self, message):
        self.terminal.config(state=tk.NORMAL)
        self.terminal.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {message}\n")
        self.terminal.config(state=tk.DISABLED)
        self.terminal.yview(tk.END)

    def fake_command(self, event):
        command = self.command_input.get()
        self.terminal.config(state=tk.NORMAL)
        self.terminal.insert(tk.END, f"\n$ {command}\nCommand not found.\n")
        self.terminal.config(state=tk.DISABLED)
        self.terminal.yview(tk.END)
        self.command_input.delete(0, tk.END)

    def play_error_sound(self):
        playsound("https://www.soundjay.com/button/beep-09.wav")  # Beep sound
        time.sleep(1)
        playsound("https://www.soundjay.com/misc/sounds/fail-buzzer-01.mp3")  # Long error sound

    def play_beep_sound(self):
        playsound("https://www.soundjay.com/button/beep-07.wav")

    def show_kernel_panic(self):
        self.root.configure(bg="red")
        self.title_label.config(text="💀 KERNEL PANIC: SYSTEM FAILURE", fg="white", bg="red", font=("Courier", 20))
        self.status_label.config(text="Rebooting in 10...9...8...", fg="white", bg="red")
        self.root.after(8000, self.show_bios_error)

    def show_bios_error(self):
        self.root.configure(bg="black")
        self.title_label.config(text="🚨 BIOS ERROR: Bootloader Corrupted!", fg="red", bg="black", font=("Courier", 20))
        self.status_label.config(text="System Halted. Press CTRL + ALT + DEL to restart.", fg="red", bg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = KaliInstaller(root)
    root.mainloop()
