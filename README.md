# TeachablePy
A Python Chatbot that can be taught how to respond.

## Installation
1. Make sure you have the latest version of Python 3
2. Clone this repo into your directory and your done! No extra dependencies or installations needed!

## Running the Programs
 To use this you must have 2 programs running at the same time: 
  - The Chat Receiver
  - The Message Sender

The Chat Reciever retrieves the data that others have sent,
while the Message Sender sends your message to the server! 

### To Run on Linux (Ubuntu 18.04 Tested)
Open up two Terminals:

Terminal 1:
- `cd Dweety` or whatever the directory is named.
- `python3 DweetClient_sender.py`

Terminal 2:
- `cd Dweety`
- `python3 DweetClient_receiver.py`

### To Run on Mac (macOs Sierra Tested) and Windows (Not Tested)
Make sure Python 3 IDLE is installed.
Open up two instances of IDLE 3,

On the first instance:
1. Go To `File` and then `Open` and from there choose DweetClient_sender.py in your directory.
2. Run the file by pressing `F5` or run from the dropdown menu

On the second instance:
1. Go To `File` and then `Open` and from there choose DweetClient_reciever.py in your directory.
2. Run that file by pressing `F5` or run from the dropdown menu


## Usage
On The sender program type in a Username (A display name) in the `Username: ` prompt.
Type in what Nest (Server) you would like to join.
Then type in a message you would like to send and press enter!
In a few seconds you will see your Username followed by your message on Receiver Program!
And if people are online then they will see your message too on their Receiver.

## Running In Browser
If you would like to test out Dweety then you can simply run the index.html file in the master directory, in your browser! 
This will give you all the functionality of Dweety without any installation!

## Improvements
By no means is this project finished, there are many things I would like to see done with this project:
- A base knowledge.csv file that has basic responses to common phrases.

If you have any ideas, Let me know in the comments!

## Liscensing
This project is liscensed under the GNU GPLv3 Liscense,
which means you are encouraged to modify this project the way you like.

## Change Log
> 1.0.0: Initial Release <br />
> 1.0.1: Added the ability to choose server, and bug fixes <br />
> 1.0.2: Fixed bug that caused high latency <br />
> 1.0.3: Added simple browser client <br \>
