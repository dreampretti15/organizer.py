import os
import shutil

#this helps me organize my "Downloads" folder.

def organize_files(directory_path):
file_types={ "pdf":"Documents",
             "docs":"Documents",
             "jpg":"images",
             "png":"Images",
             "zip":"Archieves",
             "py":"Scrips",}

#Check if the path actually exists
if not os.path.exists(directory_path):
   print(f"Error:The path {directory_path}does not exist)
return

for filename in os.listdir(directory_path):
   extension=os.path.splitext(filename)

if extension.lower() in file_types:
   folder name=folder_types[extension.lower()]
   folder path=os.path.join(directory_pat,folder_name)

#Create the folder if its not there
if not os.path.exists(folder_path):
   os.makedirs(folder_path)

original_files=os.path.join(directory_path,filename)
target_location=os.path.join(folder_path,filename)

shutil.move(original_file,target_location)
   print(f"Moved:{filename} to {folder_name}/")

if__name__=="__main__":
  my folder="./test_folder"
  organize_files(my_folder)
