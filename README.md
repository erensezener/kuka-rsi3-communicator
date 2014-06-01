## KUKA RSI-3 Communicator

KUKA RSI-3 Communicator (KR3C) enables controlling KUKA robot manipulators in real-time. KR3C is developed for the Robot Sensor Interface (RSI) 3 add-on. RSI is the official KUKA add-on technology package that is used for data exchange between an external PC and the robot controller. Please note that the content of RSI changed dramaticaly since RSI 2. Therefore, toolboxes written for RSI 2 require significant changes to make it compatible with RSI 3. As of May 2014, KR3C is the only open-source toolbox that enables real-time control via RSI 3.

###Components
Basically, KR3C does to things. First, it communicates with the robot controller in a loop by sending XML strings through UDP. If the controller does not receive any strings, it gives a timeout error. Second, it accepts position update commands through another socket; then sends the update commands to the robot controller in the correct XML format.

####Main Components
The files below are necessary for sending commands to the controller.

1. main.py
2. server.py
3. client.py
4. settings.py
5. ExternalData.py

####Kuka Controller Components 

6. kuka_files/*: All of these files should be copied to  C:\KRC\Roboter\Config\User\Common\SensorInterface

####Auxillary Components
The files below can be used to test the KR3C server or to develop applications.

7. development\_files/broadcast_listener.py
8. development\_files/kuka_emulator.py
9. development\_files/tcp_sender.py
10. development\_files/hello_world.py

###Setting up

1. Copy ./kuka-files/RSI_Ethernet.src to C:\KRC\ROBOTER\KRC\R1\Program
2. Copy rest of the files (except RSI\_Ethernet.src) in ./kuka\_files to C:\KRC\Roboter\Config\User\Common\SensorInterface in the robot controller. (Selecting Minimize HMI option from the pendant will take you to the Windows interface running on the controller. 
3. Make sure that the controller and the external PC are in the same local network.
4. Set the controllers IP to 10.100.48.100. (Different IP's are also OK as long as the first three quadrants of the controllers IP and the external PC's are the same)
5. Set your PC's IP to 10.100.48.101. If you want to use a different IP address, make sure to also change the IP's in RSI\_EthernetConfig.xml and settings.py. Defaul gateway should be 255.255.255.0.

###Running
1. Start the KR3C server by running main.py via ```python main.py```
2. Select RSI_Ethernet.src, and execute commands until RSI\_MOVECORR(). When there are warnings click on "Confirm All".
3. If RSI\_MOVECORR() does not raise an error, then you have successfully started the communication.
4. Send command strings to the KR3C server through TCP to update the position of the robot manipulator. See Position Update Commands section for more information.

###Position Update Commands

KR3C creates a socket (default port no:5005, see settings.py) and listens for packets.
To update the position of the robot manipulator, send strings such as the following:
```
a,0,0,0,0,0,0.5
```
Here, 'a' stands for angle and implies that the values are angle corrections. There are 6 values and they respectively correspond to A1, A2,.., A6. The example above, updates the angle of the 6th axis by 0.5 degrees.

It is possible to send cartesian coordinate corrections. To do this, configuration files on the controller should be modified accordingly, and the command strings should start with 'r' instead of 'a'. For example, 
```
r,0.5,0,0,0,0,0
```
command updates the X coordinate by 0.5 mm.

####Absolute vs Relative Updates
There are two ways to update the coordinates of the KUKA robot: Absolute and Relative commands. In the Absolute command mode, the coordinates of the robot when RSI is initialized is set as 0,0,0,0,0,0. All updates are given in absolute, that is relative to the initial coordinates. On the contrary, in the Relative command mode, updates are given with respect to the previous configurations.
For example, if you send a,1,0,0,0,0,0 string to the server in the absolute mode, A1 will be updates by 1, then the A1 will remain as 1.




Corresponding developer: Eren Sezener (erensezener@gmail.com)