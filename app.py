import os
import shutil
path1 = r'C:/Users/91858/OneDrive/Desktop/Lucky_folder'
content=os.listdir(path1)


img_path = path1 + '/' + 'img_file'
x=os.path.exists(img_path)
if x== False :
    os.mkdir(img_path)


text_path = path1 + '/'+'txt_file'
if os.path.exists(text_path)==False:
    os.mkdir(text_path)


excl_path=path1 + '/' + 'excel_file'
if os.path.exists(excl_path)== False:
    os.mkdir(excl_path)

for file in content:
    if '.jpg' in file and not os.path.exists(img_path+'/'+file):
        shutil.move(path1+'/'+file,img_path+'/'+file)
    if '.txt' in file and not os.path.exists(text_path+'/'+file):
        shutil.move(path1+'/'+file,text_path+'/'+file)
    if '.xlsx' in file and not os.path.exists(excl_path+'/'+file):
        shutil.move(path1+'/'+file,excl_path+'/'+file)


    





