import os
import speech_recognition as sr

# Function to create a folder
def create_folder(folder_name, path="."):
    try:
        folder_path = os.path.join(path, folder_name)
        os.mkdir(folder_path)
        print(f"Folder {folder_name} created successfully in {os.path.abspath(folder_path)}!")
    except FileExistsError:
        print(f"Folder {folder_name} already exists in {os.path.abspath(path)}!")

# Function to open a folder
def open_folder(folder_name, path="."):
    try:
        folder_path = os.path.join(path, folder_name)
        os.startfile(folder_path)
        print(f"Opening {folder_name} at {os.path.abspath(folder_path)}...")
    except FileNotFoundError:
        print(f"Folder {folder_name} not found in {os.path.abspath(path)}!")

# Function to listen to voice commands
def listen_to_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print(f"Command: {command}")
        if "create folder" in command:
            folder_name = command.replace("create folder ", "")
            if "in directory" in command:
                folder_dir = command.split("in directory")[1].strip()
                create_folder(folder_name, folder_dir)
            else:
                create_folder(folder_name, path="C:/Users/shash/OneDrive/Desktop/Directory")
        elif "open folder" in command:
            folder_name = command.replace("open folder ", "")
            if "in directory" in command:
                folder_dir = command.split("in directory")[1].strip()
                open_folder(folder_name, folder_dir)
            else:
                open_folder(folder_name, path="C:/Users/shash/OneDrive/Desktop/Directory")
        elif "stop" in command:
            print("Closing the program...")
            exit(0)
        else:
            print("Command not recognized.")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Run the main program
if __name__ == '__main__':
    while True:
        listen_to_commands()