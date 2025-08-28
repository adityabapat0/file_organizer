import os
import shutil

def main():
    source_folder = r"C:\Users\Abc\Downloads"       #path of extraction 
    new_source = r"C:\Users\Abc\Downloads\organized_files"  #new folde named organized_files


#new source paths of all the files with regards to their folder
    new_source_image=r"C:\Users\Abc\Downloads\organized_files\images"
    new_source_docs = r"C:\Users\Abc\Downloads\organized_files\docs"
    new_source_videos= r"C:\Users\Abc\Downloads\organized_files\videos"
    new_source_audios = r"C:\Users\Abc\Downloads\organized_files\audios"
    new_source_code = r"C:\Users\Abc\Downloads\organized_files\code"
    new_source_othes = r"C:\Users\Abc\Downloads\organized_files\others"

#creation of the folders inside organized_files folder
    os.makedirs(new_source,exist_ok=True)
    os.makedirs(new_source_image,exist_ok=True)
    os.makedirs(new_source_docs,exist_ok=True)
    os.makedirs(new_source_videos,exist_ok=True)
    os.makedirs(new_source_audios,exist_ok=True)
    os.makedirs(new_source_code,exist_ok=True)
    os.makedirs(new_source_othes,exist_ok=True)


#shit code
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
            file_lists.append(file_name)    #separating files from folders and appending it separately
        else:
            folder_lists.append(file_name)


#separating all the files into their correct format on basis of their extentions 
    for i in file_lists:
        if i.lower().endswith((".jpg",".png")):   
            images.append(i)  #images
        elif i.endswith((".pdf","txt",".ppt",".pptx",".docx",".csv",".sav",".mplstyle",".db",".md",)): 
            documents.append(i)  #documents
        elif i.lower().endswith((".mp4","mov","vid")):
            videos.append(i)  #videos
        elif i.lower().endswith((".mkv",".mp3","wav")):
            audio.append(i)  #audios
        elif  i.lower().endswith((".py",".c",".cpp",".java","ipynb")):
            code.append(i)  #code/programs
        else:
            others.append(i)  #other files such as .exe , applications, zips, etc
            
#moving it to their respective folders
    for img in images:
        old_path = os.path.join(source_folder,img)
        new_path = os.path.join(new_source_image,img)
        shutil.move(old_path,new_path)
    for doc in documents:
        old_path = os.path.join(source_folder,doc)
        new_path = os.path.join(new_source_docs,doc)
        shutil.move(old_path,new_path)
    for vid in videos:
        old_path = os.path.join(source_folder,vid)
        new_path = os.path.join(new_source_videos,vid)
        shutil.move(old_path,new_path)
    for prog in code:
        old_path = os.path.join(source_folder,prog)
        new_path = os.path.join(new_source_code,prog)
        shutil.move(old_path,new_path)
    for oth in others:
        old_path = os.path.join(source_folder,oth)
        new_path = os.path.join(new_source_othes,oth)
        shutil.move(old_path,new_path)
        
if __name__ == "__main__":
    main()
