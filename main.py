import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
       finishLabel.configure(text="Download Error", text_color="red")
    

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.file_size
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    print(percentage_of_compeletion)
    
# pengaturan sistem
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# frame apk
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding Ui elemenets
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# proggres
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)


# Jalankan apk
app.mainloop();