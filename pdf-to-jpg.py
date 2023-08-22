# import module
import os
from pdf2image import convert_from_path
folder1_path = input("Enter pdf folder name: ")
folder1_file_names = set(os.listdir(folder1_path))
for file_name in folder1_file_names:
	print(file_name)
	if not os.path.exists("imgs"):
		os.makedirs(f"imgs")
	pages = convert_from_path(folder1_path+"/"+file_name)
	for i in range(len(pages)):
		pages[i].save("imgs/"+file_name.replace(".pdf","")+(("_"+str(i)) if i > 0 else "")+'.jpg', 'JPEG')