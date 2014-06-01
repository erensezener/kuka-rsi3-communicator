## KUKA RSI-3 Communicator

KUKA RSI-3 Communicator (KR3C) enables controlling KUKA robot manipulators in real-time. KR3C is developed for the Robot Sensor Interface (RSI) 3 add-on. RSI is the official KUKA add-on technology package that is used for data exchange between an external PC and the robot controller. Please note that the content of RSI changed dramaticaly since RSI 2. Therefore, toolboxes written for RSI 2 require significant changes to make it compatible with RSI 3. As of May 2014, KR3C is the only open-source toolbox that enables real-time control via RSI 3.

###Components

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
1. Start the KR3C program via ```python main.py```
2. Select RSI_Ethernet.src, and execute commands until RSI\_MOVECORR(). When there are warnings click on "Confirm All".
3. If RSI\_MOVECORR


