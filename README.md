#What is KUKA RSI-3 Communicator

KUKA RSI-3 Communicator (KR3C) enables controlling KUKA robot manipulators in real-time from an external PC via UDP protocol. KR3C is developed for the Robot Sensor Interface (RSI) 3 add-on. RSI is the official KUKA add-on technology package that is used for data exchange between an external PC and the robot controller. The content of RSI changed dramatically since RSI 2. Therefore, toolboxes written for RSI 2 require significant changes to make it compatible with RSI 3. As of May 2014, KR3C is the only open-source toolbox that enables real-time control via RSI 3.

##Components
Basically, KR3C does two things. First, it communicates with the robot controller in a loop by sending XML strings through UDP. If the controller does not receive any strings, it gives a timeout error. Second, it accepts position update commands through another socket; then sends the update commands to the robot controller in the correct XML format.

###Main Components
The files below are necessary for sending commands to the controller.

1. main.py: run this program to start the KR3C
2. server.py: communicates with the robot controller
3. client.py: communicates with the external pc
4. settings.py: IP's, ports etc are configured here
5. ExternalData.xml: contains the default XML string that will be sent when the server is started

###Kuka Controller Components 

6. kuka_files/*: All of these files should be copied to  C:\KRC\Roboter\Config\User\Common\SensorInterface
(To be updated)

###Auxiliary Components
The files below are examples which can be used to test the KR3C server or to develop applications.

7. development\_files/kuka_emulator.py: acts like the robot controller, prints the coordinates
8. development\_files/tcp_sender.py: gets update values (such as ```a,0,0,0,0,0,0.5```) and sends them to KR3C

##Setting up

1. Copy ./kuka-files/RSI_Ethernet.src to C:\KRC\ROBOTER\KRC\R1\Program
2. Copy rest of the files (except RSI\_Ethernet.src) in ./kuka\_files to C:\KRC\Roboter\Config\User\Common\SensorInterface in the robot controller. (Selecting Minimize HMI option from the pendant will take you to the Windows interface running on the controller.) 
3. Make sure that the controller and the external PC are in the same local network.
4. Set the controller's IP to 10.100.48.100. (Different IP's are also OK as long as the first three quadrants of the controllers IP and the external PC's are the same)
5. Set your PC's IP to 10.100.48.101. If you want to use a different IP address, make sure to also change the IP's in RSI\_EthernetConfig.xml and settings.py. Default gateway should be 255.255.255.0.

##Running
1. Start the KR3C server by running main.py via ```python main.py```
2. Select RSI_Ethernet.src from the pad, and execute commands until RSI\_MOVECORR(). When there are warnings click on "Confirm All".
3. If RSI\_MOVECORR() does not raise an error, then you have successfully started the communication.
4. Send command strings to the KR3C server through TCP to update the position of the robot manipulator. See Position Update Commands section for more information. Use demo.py to see a demo. 
5. See demo.py to see an example of getting the current position. It prints the output to stdout. You can redirect the output to a file or a pipe if needed.
```
demo.py > log.txt  
```

###Position Update Commands

KR3C creates a socket (default port no:5005, see settings.py) and listens for packets.
To update the position of the robot manipulator, send strings such as the following:
```
a,0,0,0,0,0,0.5
```
Here, 'a' stands for angle and implies that the values are angle corrections. There are 6 values and they respectively correspond to A1, A2,.., A6. The example above, updates the angle of the 6th axis by 0.5 degrees.

It is possible to send cartesian coordinate corrections. To do this, change the xml setting file from RSI_Ethernet.src file. And the command strings should start with 'r' instead of 'a'. For example, 
```
r,0.5,0,0,0,0,0
```
command updates the X coordinate by 0.5 mm.

###Absolute vs Relative Updates
There are two ways to update the coordinates of the KUKA robot: Absolute and Relative commands. In the Absolute command mode, the coordinates of the robot when RSI is initialized is set as 0,0,0,0,0,0. All updates are given in absolute, that is relative to the initial coordinates. On the contrary, in the Relative command mode, updates are given with respect to the previous configurations.  
For example, if you send a,1,0,0,0,0,0 string to the server in the absolute mode, A1 value will initially be increased by 1, then it will remain as 1.

To change the update mode, open RSI\_Ethernet.src and give #RELATIVE or #ABSOLUTE as a parameter of RSI_ON().

```
# use one of the below
ret = RSI_ON(#RELATIVE)
ret = RSI_ON(#ABSOLUTE)
```

Note: In both modes, KR3C saves the last command and sends it repeatedly. In Absolute mode, this will cause the robot to stay still. In Relative mode, this will move the robot continuously. As a general advice use of absolute mode is more preferable.

See the RSI 3 manual to learn more about the differences.


###Using a Custom Trajectory

Put your trajectory functions in generateTrajectory.py. Your generator functions should take the current time as input as it will be called each cycle. A sample usage is shown in demo.py  


##Troubleshooting
If your angle or cartesian references are not appropriate you will get torque errors. Make sure your reference position is realizable in 4 msec. If you need to run just a little faster try to run it at T2 or AUTO mode (see Kuka docs).

Another error you may get is out of workspace error. Workspace limits are set conservatively to be on the safe side. If you need to change the limits, update the rsi file and upload it to SensorInterface folder again.

When using cartesian control make sure your trajectory does not get close to singular points. If your home position is at singularity it will give torque error for 2 joints because they are aligned. If it stops suddenly with torque error while moving, you will know it from the alignment.

###Authors
Eren Sezener (erensezener@gmail.com, erensezener.com)

Osman Kaya (osmankaya89@gmail.com)

Ozyegin University Robotics Laboratory (robotics.ozyegin.edu.tr)

