import os
import random
import sys
import tkinter as tk
from PIL import Image, ImageTk  # Make sure Pillow is installed

# Get the path to the directory where the script is located
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Region and champion data
regions = {
    "Demacia": [
        "Aatrox", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", 
        "Garen", "Jarvan IV", "Lux", "Riven", "Sejuani", "Vayne"
    ],
    "Noxus": [
        "Darius", "Draven", "Katarina", "Mordekaiser", "Rumble", "Swain", "Talon", 
        "Kled", "Cassiopeia", "Brand"
    ],
    "Ionia": [
        "Ahri", "Akali", "Akshan", "Irelia", "Karma", "Kennen", "Lee Sin", 
        "Yasuo", "Zed", "Lillia", "Qiyana"
    ],
    "Freljord": [
        "Ashe", "Braum", "Sejuani", "Anivia", "Lissandra", "Tryndamere", 
        "Gnar", "Gragas", "Sivir"
    ],
    "Piltover": [
        "Caitlyn", "Jayce", "Vi", "Jinx", "Heimerdinger", "Ekko", "Seraphine"
    ],
    "Zaun": [
        "Singed", "Twitch", "Ekko", "Jinx", "Rumble", "Zac", "Urgot", 
        "Viktor", "Renata Glass"
    ],
    "Bilgewater": [
        "Miss Fortune", "Gangplank", "Nautilus", "Graves", "Twisted Fate"
    ],
    "Shadow Isles": [
        "Thresh", "Yorick", "Karthus", "Kalista", "Elise", "Viego", 
        "Fiddlesticks", "Morgana", "Malzahar"
    ],
    "The Void": [
        "Kha'Zix", "Cho'Gath", "Vel'Koz", "Rek'Sai"
    ],
    "Targon": [
        "Leona", "Diana", "Taric", "Pantheon"
    ],
    "Bandle City": [
        "Teemo", "Rumble", "Jax", "Lulu"
    ],
    "Runeterra": [
        "Ryze", "Smolder", "Samira", "Sett", "Soraka", "Sylas", 
        "Zeri", "Zilean", "Zoe", "Vex", "Ivern"
    ]
}

# Load and resize the background image
def set_background(root, image_path):
    bg_image = Image.open(resource_path(image_path))  # Use resource_path to find the image
    bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    background_label = tk.Label(root, image=bg_photo)
    background_label.image = bg_photo  # Keep a reference to avoid garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to simulate random region selection
def random_region():
    region = random.choice(list(regions.keys()))
    champions = regions[region]
    region_label.config(text=f"Region: {region}", fg="white", bg="#333")
    champion_label.config(text=f"Champions: {', '.join(champions)}", wraplength=600)
    random_champion_button.place(x=(window_width//2) - 75, y=300)  # Center the button

# Function to simulate random champion selection
def random_champion():
    if region_label.cget("text") != "Region: ":
        current_region = region_label.cget("text").split(": ")[1]
        champions = regions[current_region]
        champion = random.choice(champions)
        champion_label.config(text=f"Champion: {champion}", fg="#FFD700", bg="#333", font=("Arial", 16, "bold"))

# Tkinter GUI setup
root = tk.Tk()
root.title("League of Legends Champion Randomizer")

# Set window size and position it at the center of the screen
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Set background image (runeterra.jpg)
set_background(root, "images/runeterra.jpg")

# Random Region Button (Centered)
region_button = tk.Button(root, text="Random Region", command=random_region, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", pady=10, padx=20)
region_button.place(x=(window_width//2) - 75, y=150)  # Center the button horizontally

# Random Champion Button (Centered but initially hidden)
random_champion_button = tk.Button(root, text="Random Champion", command=random_champion, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", pady=10, padx=20)
random_champion_button.place_forget()  # Hide initially, will be shown after region is picked

# Labels for displaying the selected region and champions (Centered)
region_label = tk.Label(root, text="Region: ", font=("Arial", 18), bg="#333", fg="white", pady=20)
region_label.place(x=(window_width//2) - 200, y=230)

champion_label = tk.Label(root, text="Champion: ", font=("Arial", 16), bg="#333", fg="white", wraplength=600, pady=10)
champion_label.place(x=(window_width//2) - 200, y=350)

root.mainloop()
