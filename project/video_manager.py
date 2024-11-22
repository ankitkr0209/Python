import json
import sqlite3
from tkinter import*


def load_video():

    try:
        with open('video.txt' , 'r') as file:

           test = json.load(file) 
           return test
    except FileNotFoundError:
        return []


def save_video(videos):
    with open('video.txt' , 'w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("\n")
    print("*" *60)

    for index , video in enumerate(videos , 1):
        print(f"{index}. Name : {video['name']} || Duration : {video['time']}")

    print("\n")   
    print("*" *60)

def add_video(videos):
    name = input("enter name of video :- ")
    time = input("enter the duration of the video :- ")
    videos.append({'name': name , 'time': time})
    save_video(videos)


def update_video(videos):
    list_all_videos(videos)

    index = int(input("rnter the index you want to update the video :- "))
    if 1 <= index <= len(videos):
        name = input("enter the new name of video :- ")
        time = input("enter the new duration of thre video :- ")
        videos.append({'name': name , 'time': time})
        save_video(videos)
    else:
        print("invalid choice")

def delete_video(videos):
    list_all_videos(videos)

    index = int(input("enter the index of video you want to delete :- "))
    if 1<= index <= len(videos):
        del videos[index-1]
    
    else:
        print("invalid choice")


videos = load_video()

while True: 
    print("Video Manager / choose an option ")
    print("1 : lis all videos ")
    print("2 : Add video")
    print("3 : update video details")
    print("4 : Delete a video from the list")
    print("5 : Exit")
    choice = input("choose the option :- ")

    match choice:
        case "1":
            list_all_videos(videos)
        
        case "2":
            add_video(videos)

        case "3":
            update_video(videos)

        case "4":
            delete_video(videos)

        case "5":
            break

        case _:
            print("ivalid choice")
