import os
import shutil

source_folder = r"C:\Users\Abc\Downloads"       #path of extraction 
new_source = r"C:\Users\Abc\Downloads\organized_files"  

new_source_image=r"C:\Users\Abc\Downloads\organized_files\images"
new_source_docs = r"C:\Users\Abc\Downloads\organized_files\docs"
new_source_videos= r"C:\Users\Abc\Downloads\organized_files\videos"
new_source_audios = r"C:\Users\Abc\Downloads\organized_files\audios"
new_source_code = r"C:\Users\Abc\Downloads\organized_files\code"
new_source_othes = r"C:\Users\Abc\Downloads\organized_files\others"

os.makedirs(new_source,exist_ok=True)
if not os.path.exists(new_source):
    os.mkdir(new_source)
    print(f"dir {new_source} created")
else:
    print(f"dir {new_source} exist")

if not os.path.exists(new_source_image):
    os.mkdir(new_source_image)
    print(f"new dir {new_source_image} created")
else:
    print(f"dir {new_source_image} exist")
if not os.path.exists(new_source_docs):
    os.mkdir(new_source_docs)
    print(f"new dir {new_source_docs} created")
else:
    print(f"dir {new_source_docs} exist")
if not os.path.exists(new_source_videos):
    os.mkdir(new_source_videos)
    print(f"new dir {new_source_videos} created")
else:
    print(f"dir {new_source_videos} exist")
if not os.path.exists(new_source_code):
    os.mkdir(new_source_code)
    print(f"new dir {new_source_code} created")
else:
    print(f"dir {new_source_code} exist")
if not os.path.exists(new_source_othes):
    os.mkdir(new_source_othes)
    print(f"new dir {new_source_othes} created")
else:
    print(f"dir {new_source_othes} exist")

file_lists = []
folder_lists = []
images = []
documents = []
videos = []
code = []
audio = []
others = []
for file_name in os.listdir(source_folder):
    full_path = os.path.join(source_folder,file_name)
    if os.path.isfile(full_path):
        file_lists.append(file_name)
    else:
        folder_lists.append(file_name)

for i in file_lists:
    if i.lower().endswith((".jpg",".png")):
        images.append(i)
    elif i.endswith((".pdf","txt",".ppt",".pptx",".docx",".csv",".sav",".mplstyle",".db",".md",)):
        documents.append(i)
    elif i.lower().endswith((".mp4","mov","vid")):
        videos.append(i)
    elif i.lower().endswith((".mkv",".mp3","wav")):
        audio.append(i)
    elif  i.lower().endswith((".py",".c",".cpp",".java","ipynb")):
        code.append(i)
    else:
        others.append(i)
        
