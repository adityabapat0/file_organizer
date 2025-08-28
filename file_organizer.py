import os
import shutil

source_folder = r"C:\Users\Abc\Downloads"
file_lists = []
folder_lists = []
images = []
documents = []
videos = []
code = []
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
    elif  i.lower().endswith((".py",".c",".cpp",".java","ipynb")):
        code.append(i)
    else:
        others.append(i)
# print(len(images))
# print(len(documents))
# print(others)
# print(len(videos))
# print(len(code))
# print(len(others))

# print(len(file_lists),len(images+documents+videos+code+others))
