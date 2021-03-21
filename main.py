from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from folderChecker import folder_maker
import os, json, time


#music_list, document_list, video_list, image_list=[]
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        file_list=os.listdir(folder_to_track)
        for item in file_list:
            name,extension = os.path.splitext(item)
            if extension=='.mp3':
                #music_list.append(item)
                folder_maker(folder_to_track, item, music_destination)
            elif (extension=='.docx') or (extension=='.xlsx') or (extension=='.pdf') or (extension=='.txt'):
                #document_list.append(item)
                folder_maker(folder_to_track, item, documents_destination)
            elif (extension=='.png') or (extension=='.jpg') or (extension=='.jpeg') or (extension=='.svg') or (extension=='.gif'):
                #image_list.append(item)
                folder_maker(folder_to_track,item, images_destination)
            elif (extension=='.wmv') or (extension=='.mp4') or (extension=='.mov'):
                #video_list.append(item)
                folder_maker(folder_to_track, item, videos_destination)
            elif (extension=='.zip') or (extension=='.tar.gz') or (extension=='.gz'):
                folder_maker(folder_to_track, item, archive_destination)

        


#Path's should be absolute and without the last "/", for example "/home/Downloads", not "/home/Downloads/"
folder_to_track = ''
images_destination= ''
music_destination = ''
documents_destination = ''
videos_destination = ''
archive_destination = ''
event_handler=MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

