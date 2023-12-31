#Ramones - "Ramones" playlist
#https://youtube.com/playlist?list=PLBnJv6rImVe-LcbIsBXzIp6BpV6hqZnoO&si=jNymhDVGkVd3QHNn

from pytube import YouTube, Playlist
from sys import exit
from datetime import date
from time import localtime, strftime
from os import environ, chdir, path, mkdir
from math import ceil

def spaces(integer):
    integer = str(integer)
    result = ''
    while len(integer) > 3:
        result = integer[-3:] + " " + result
        integer = integer[:-3]

    result = integer + " " + result 
    return result

branch_link = ""
branch_format = ""
savepath = ""

if environ["OS"][0:7] == "Windows":
    savepath = environ["USERPROFILE"] + r"\\Desktop"
else:
    print("Works only for Windows, sorry!!")
    exit()

chdir(savepath)
link = str(input("Enter the URL of the playlist You want to extract data from: \n>> "))
playlist_obj = Playlist(link) 

if not path.exists(savepath + r"\\" + playlist_obj.title + "_data"):    
    mkdir(playlist_obj.title + "_data")

chdir(playlist_obj.title+ "_data")
playlist_list = playlist_obj.video_urls
number_of_tracks = len(playlist_list)
calendarium = str(date.today())
current_time = strftime("%H:%M:%S", localtime())


with open(f"{playlist_obj.title}_data_extract_{calendarium[:4]}{calendarium[5:7]}{calendarium[8:10]}{current_time[:2]}{current_time[3:5]}{current_time[6:8]}.txt", "w") as f:
    f.write(f"Playlist name: \t\t\t{playlist_obj.title}\n")
    f.write(f"Playlist's url:\t\t\t{link}\n")
    f.write(f"Playlist's owner: \t\t{playlist_obj.owner}, {current_time}\n")
    #f.write(f"Playlist last updated on: \t{playlist_obj.last_updated}\n")
    f.write(f"Time of this data extract: \t{calendarium}, \n")
    f.write(f"Playlist views so far: \t\t{spaces(playlist_obj.views)}\n")
    f.write(f"Current playlist length: \t{number_of_tracks}\n\n\n\n\n")

    halfway = ceil(number_of_tracks/2)
    exception_number = 0

    for index in range(number_of_tracks):
        if index == halfway:
            print("We're halfway there!")
        element = YouTube(playlist_list[index])
        try:
            f.write(f"{index}. {element.title}\n")
            f.write(f"Views: {spaces(element.views)}\n")
            f.write(f"{playlist_list[index]}\n\n")
        except:
            exception_number += 1
            f.write(f"{index}. An error has occurred when trying to download data of a video with URL: {playlist_list[index]}\n\n")

    if exception_number == 0:
        f.write("\n\n\n\nNo errors have occurred during extraction")
    else:
        f.write(f"Number of errors during extraction: {exception_number}")

print(playlist_obj.title + " data has been successfully extracted to Your desktop!")
if exception_number == 0:
    print("No errors have occurred during extraction")
else:
    print(f"Number of errors during extraction: {exception_number}")