import os, gzip, shutil

dire_name = r'C:\Users\yourFileLocation'





def gz_extract(directory):
    extension = ".gz"
    os.chdir(directory)
    for item in os.listdir(directory): # loop through items in dir
      if item.endswith(extension): # check for ".gz" extension
          gz_name = os.path.abspath(item) # get full path of files
          file_name = (os.path.basename(gz_name)).rsplit('.',1)[0] #get file name for file within
          with gzip.open(gz_name,"rb") as f_in, open(file_name,"wb") as f_out:
              shutil.copyfileobj(f_in, f_out)
          os.remove(gz_name) # delete zipped file



for root, dirs, files in os.walk(dire_name):
    for dir_name in dirs:
        print (dire_name,dir_name)
        os.chdir(os.path.join(dire_name,dir_name))
        gz_extract(os.path.join(dire_name, dir_name))
