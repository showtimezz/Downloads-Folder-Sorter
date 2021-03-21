# Downloads Folder Sorter

A background process that automatically sorts every file in a given folder by type and date. The program automatically triggers when a file is added, deleted or modified. *Doesn't actually have to be the downloads folder.*

## Getting Started

To start using this program, you need to update the 
```
folder_to_track 
images_destination
music_destination 
documents_destination 
videos_destination 
archive_destination 
```
variables located in the`main.py` file to match your system and needs. 


### Prerequisites



```
geckodriver
Python 3.x
pip
watchdog
os
json
time
```



## How it works
This program uses the python `datetime()` function in order to calculate the month for subdirectories. It does this once every time the program is initiated. To use this as a hands-off background process that initializes itself on start up, you should reboot your PC at least once a month. 


## Using this program on Windows 
Windows uses '\', while linux uses '/' in their paths and folder structures. In theory, changing evey instace of '/' to '\' should do the trick. However, this wasn't tested. 


You could make this program a CRON job, or create a shell/bash script and add that to startup. 
## Contributing

The easiest way to contribute is taking a look at the [issues](https://github.com/showtimezz/Downloads-Folder-Sorter/issues) tab. 




## License

This project is licensed under the MIT License.
