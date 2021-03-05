import os

from datetime import datetime

list_of_directories=[]
dt=datetime.today()
month=dt.strftime('%B')

def folder_maker(src, filename, folder_destination):
    everything = os.listdir(folder_destination)
    #Adding all directories to a single list
    for item in everything:
        if os.path.isdir(item):
            list_of_directories.append(item)
    #If this current month doesnt exist, create a directory after it.
    if not month in list_of_directories:
        os.mkdir(folder_destination + '/' + month)
        folder_destination = folder_destination + '/' + month
    else:
        folder_destination = folder_destination + '/' + month
    #The actual moving of files
    src= src + '/' + filename
    new_destination = folder_destination + '/' + filename
    os.rename(src,new_destination)
    

#def sorting_algorithm(src, filename, folder_destination):
#    src=folder_to_track + '/' + filename
#    new_destination = folder_destination + '/' + filename
#    os.rename(src,new_destination)