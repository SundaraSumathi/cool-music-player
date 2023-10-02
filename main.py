mport pygame
from tkinter import Tk, Button, filedialog, Listbox, Scrollbar, Scale

pygame.init()

current_song_index = 0
is_paused = False

def play_song(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

def pause_song():
    pygame.mixer.music.pause()

def resume_song():
    pygame.mixer.music.unpause()

def add_song():
    root = Tk()
    root.withdraw()
    song_paths = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3;*.wav")])

    for song_path in song_paths:
        playlist.append(song_path)
        song_name = song_path.split("/")[-1]
        playlist_box.insert("end", song_name)

def add_to_queue():
    selected_index = playlist_box.curselection()
    if selected_index:
        song_index = int(selected_index[0])
        queue.append(playlist[song_index])
        queue_box.insert("end", playlist_box.get(selected_index))

def select_song(event):
    global current_song_index
    selected_index = playlist_box.curselection()
    if selected_index:
        current_song_index = int(selected_index[0])
        play_song(playlist[current_song_index])

def play_next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    play_song(playlist[current_song_index])

def play_previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(playlist)
    play_song(playlist[current_song_index])

def set_volume(volume):
    volume = float(volume) / 100.0
    pygame.mixer.music.set_volume(volume)

window = Tk()
window.title("Cool Music Player")
window.configure(bg="black")

button_bg = "#383838"
button_fg = "white"
listbox_bg = "#272727"
listbox_fg = "white"

add_song_button = Button(window, text="Add Song", command=add_song, bg=button_bg, fg=button_fg)
add_to_queue_button = Button(window, text="Add to Queue", command=add_to_queue, bg=button_bg, fg=button_fg)
previous_button = Button(window, text="Previous", command=play_previous_song, bg=button_bg, fg=button_fg)
play_button = Button(window, text="Play", command=lambda: play_song(playlist[current_song_index]), bg=button_bg, fg=button_fg)
pause_button = Button(window, text="Pause", command=pause_song, bg=button_bg, fg=button_fg)
resume_button = Button(window, text="Resume", command=resume_song, bg=button_bg, fg=button_fg)
next_button = Button(window, text="Next", command=play_next_song, bg=button_bg, fg=button_fg)

playlist_box = Listbox(window, width=50, height=10, font=("Arial", 12), bg=listbox_bg, fg=listbox_fg)
playlist_box.bind("<<ListboxSelect>>", select_song)  # Bind the event to call select_song function
scrollbar = Scrollbar(window, orient="vertical", command=playlist_box.yview)
playlist_box.config(yscrollcommand=scrollbar.set)

queue_box = Listbox(window, width=50, height=5, font=("Arial", 12), bg=listbox_bg, fg=listbox_fg)
queue_box.config(yscrollcommand=scrollbar.set)

volume_slider = Scale(window, from_=0, to=100, orient="horizontal", command=set_volume, bg=listbox_bg, fg=listbox_fg, length=200)
volume_slider.set(50)
volume_slider.config(label="Volume")

add_song_button.pack(side="left", padx=10, pady=10)
add_to_queue_button.pack(side="left", padx=10, pady=10)
previous_button.pack(side="left", padx=10, pady=10)
play_button.pack(side="left", padx=10, pady=10)
pause_button.pack(side="left", padx=10, pady=10)
resume_button.pack(side="left", padx=10, pady=10)
next_button.pack(side="left", padx=10, pady=10)
playlist_box.pack(pady=10, padx=10, fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
volume_slider.pack(side="bottom", padx=10, pady=10)
queue_box.pack(pady=10, padx=10, fill="both", expand=True)

playlist = []
queue = []

window.mainloop()
