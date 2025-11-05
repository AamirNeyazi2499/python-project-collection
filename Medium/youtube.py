import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading...")
            ydl.download([url])
        print("Video downloaded successfully")
    except Exception as e:
        print(f"Error: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    video_url = input("Please enter a YouTube url: ")
    
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    
    print("Please select a folder for download...")
    save_dir = open_file_dialog()
    root.destroy()
    
    if save_dir:
        print("Started download... ")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location")












#######################################################################################

# This is also the running program


# import yt_dlp

# def download_video(url, save_path):
#     try:
#         ydl_opts = {
#             'format': 'best[ext=mp4]',
#             'outtmpl': f'{save_path}/%(title)s.%(ext)s',
#         }
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#         print("Video downloaded successfully")
#     except Exception as e:
#         print(e)

# url = "https://www.youtube.com/shorts/_DypXKotEN0"
# save_path = r"C:\Users\Aamir Neyazi\Downloads"

# download_video(url, save_path)

#########################################################################################

# from pytube import YouTube
# import tkinter as tk
# from tkinter import filedialog

# def download_video(url, save_path):
#     try:
#         yt = YouTube(url)
#         streams = yt.streams.filter(progressive=True, file_extension="mp4")
#         highest_res_stream = streams.get_highest_resolution()
#         highest_res_stream.download(output_path=save_path)
#         print("Video downloaded successfully")
#     except Exception as e:
#         print(e)

# def open_file_dialog():
#     folder = filedialog.askdirectory()
#     if folder:
#         print(f"Selected folder: {folder}")
#     return folder

# if __name__ == "__main__":
#     video_url = input("Please enter a YouTube url: ")
    
#     root = tk.Tk()
#     root.attributes('-topmost', True)
#     root.withdraw()
    
#     print("Please select a folder for download...")
#     save_dir = filedialog.askdirectory(parent=root, title="Select Download Folder")
#     root.destroy()
    
#     if save_dir:
#         print(f"Selected folder: {save_dir}")
#         print("Started download... ")
#         download_video(video_url, save_dir)
#     else:
#         print("Invalid save location")

##############################################

