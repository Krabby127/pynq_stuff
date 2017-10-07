# Voice Controlled Mobile Robot
Team John Cena

## Objective
Our team's goal was to develop a mobile robot controlled completely by voice commands. 

## Utilized modules and resources
Three principal elements were involved in the project. These were developed in parallel, independently, in anticipation of being integrated into a wholistic control system at a later point in time. The resources and standalone modules that were combined in our final project were:

#### Command Source
* An operator issues commands from a location remote to the robot itself
* A headset was used to capture verbal commands issued by the operator
* WAV file creation was used to store the captured verbal commands to forward to the robot
* Command transmission was facilitated across the wireless network connection

#### ArduMoto Shield
* PWM to control two independently actuated wheels
* Full H-Bridge because a G-Bridge just wouldn't quite cut it

#### Python Verbalizer and Speech Processor
* Python SpeechRecognition library parses and interprets contents of WAV file received from Command Source
* Output text is compared against an array of supported commands
* Appropriate signal is sent to robotic motion controller

## Implementation
We developed a robot on two wheels that is remotely connected to a command source.

## Results
We kluged together the steamiest pile of weehoo that has even been foisted upon the engineering community.

## How to Reproduce
Look at our code. There are like 12 lines, so you should be fine.

# Thanks!
