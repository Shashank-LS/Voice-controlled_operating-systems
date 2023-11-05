# Voice-controlled_operating-systems
Basic level

This script allows you to create and open folders using voice commands. The script utilizes the speech_recognition library to capture voice input and executes actions based on the recognized commands.

#Prerequisites
1.Python 3.x
2.speech_recognition library

#Installation
1.You can install the required libraries using pip:
pip install SpeechRecognition

#Usage
1.Run the script.
2.Speak clearly into the microphone when prompted.
3.Issue voice commands such as "create folder {folder_name}" or "open folder {folder_name}".
4.Optionally, specify the directory for folder operations using the command "in directory {directory_path}".

#Available Commands
1.Create Folder: Use the command "create folder {folder_name}" to create a new folder.
2.Open Folder: Use the command "open folder {folder_name}" to open an existing folder.
3.Stop: Say "stop" to exit the program.

#Folder Operations
1.The script creates folders in the specified directory or the default directory (C:/Users/shash/OneDrive/Desktop/Directory).
2.The script opens folders in the specified directory or the default directory.

#Troubleshooting
1.If you encounter any issues or errors, please ensure that the microphone is working correctly and that the speech_recognition library is properly installed.

For more information on the script's functionality, please refer to the comments in the script file.

License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.
