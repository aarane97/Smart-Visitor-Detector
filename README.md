# Smart-Visitor-Detector

## Aim 
Home automation is a blooming market nowadays. Visitor detection technologies, though, have not become prevalent due to it being expensive. Our project aims to provide a low-cost solution to the problems mentioned above, by giving the user options to communicate with the user or to raise an alarm, depending on what the user wants. This would enable the technology to be more prevalent, and would also ensure the peace of mind when the user is away from his workplace/home.

## Approach
Automation is widely used in many fields nowadays. It enables people to spend less time on chores and enables them to maximise their productivity. This project also further aims to increase the productivity and improve security of the workplace/home by letting people know who visits them and when, while simultaneously providing many options.   
The system first detects a visitor using a sensor. After an object has been sensed, a picture is clicked and compared with threshold values to ensure that false triggering has not taken place. The photo will then be compared with a set of faces stored in the database, using a facial recognition algorithm. If the face matches, no further action is taken. If the face does not match with any face in the database, then the photo along with a timestamp is uploaded to a server.   
An app created especially for this project will check the server continuously. Once the picture is uploaded, it will be retrieved by the app along with the date and time stamp. The user can then check the photo along with the details and can then carry out one of the three operations.   
The user first has a choice of taking no action, where the app will revert to the original sensing mode after waiting for a specified amount of time.   
The second option is to communicate with the visitor, whereby the user can have a conversation with the visitor, and give him the necessary directions.   
Lastly, if the visitor is identified as a miscreant by the user, he can then inform the relevant authorities and/or trip the alarm. If the call authorities’ button is pressed, then the number will be loaded onto the dialler. The user has to then just press the call button to communicate. After the call is over, the app reverts to the screen showing the three options.
All these actions can be carried out directly via an app created especially for this project. As all the computation is carried out on the hardware, any device supporting the app can be used for this purpose.   

## Block diagram of Smart Visitor Detector
![image](https://user-images.githubusercontent.com/61768243/77686130-d6dd3e80-6f72-11ea-8903-3b1079f18cbe.png)

## Working
### Detection of Person
The ultrasonic sensor is used to detect the person who is present in front of the ultrasonic sensor. The output of ultrasonic sensor is analog in nature. As Raspberry Pi cannot work with analog signals, Arduino is used to convert this analog voltage change to digital format. The final output is in terms of distance in inches. This is the distance at which the object has been detected. If the distance is less than the threshold distance specified, the Raspberry Pi instructs the webcam to take the picture of the person present in front of the webcam.
### Face Recognition
A database of familiar faces is created in Raspberry Pi. After the camera takes the picture of the person, facial recognition is carried out. If the face in the image matches with one of the faces in the known database, the Raspberry Pi takes no action. Otherwise, the Raspberry Pi will upload the newly clicked image to the server. This image can then be viewed on the app.
### Working of Application
An application is designed especially for this system. It will give the users the option to control and take action with the help of the system. The recent images of unknown people are shown on the app. This further includes the following options:
1) Take action
2) Communicate via Intercom
3) Add to known
* Take action:
Alarm that is interfaced with the hardware of the project will be triggered on pressing this button. The purpose of this alarm is to alert the neighbours of some sort of danger being present at the house/workplace. Furthermore, the user of the app can press ‘inform the police’ button. Using this, the user can make a call and inform the police.
* Communicate via Intercom:
The user is presented with a third option in the app that will allow the user to talk to the visitor using the intercom. The user can give instructions to the visitor. The visitor cannot call the user in any case. After ending the call, the user will be returned back to the screen with the three options again.
* Add to known:
This option is used in case the image that was clicked needs to be added to the known
person database. This option can be helpful if we do not need notifications if the person visits next time.

## Implementation
The project was divided into different modules. The problem statement was properly defined and studied, and various methods to implement each module successfully and efficiently were studied. The various modules and their implementation in this project are explained below.
### Detection of Person
For detection of the person who is present in front of ultrasonic sensor, “Newping.h” library on Arduino is used to initialize the ultrasonic sensor. “Serial” module on Python was used to accept serial input from the Arduino.
“Newping.h” library has following features:
* Works with many different ultrasonic sensor models.
* Option to interface with all but the SRF06 sensor using only one Arduino pin.
* Doesn't lag for a full second if no ping echo is received like all other ultrasonic libraries.
* Uses port registers when accessing pins for faster execution and smaller code size.
* Allows setting of a maximum distance where pings beyond that distance are read as no ping "clear".
* Ease of using multiple sensors (example sketch with 15 sensors).
* More accurate distance calculation (cm, inches & uS).
Raspberry Pi doesn’t support analog input, processor speed ranges from 700 MHz to 1.4 GHz for the Pi 3 Model B+; on-board memory ranges from 256 MB to 1 GB RAM. Secure Digital (SD) cards are used to store the operating system and program memory in either SDHC or MicroSDHC sizes. The boards have one to four USB ports. So, change in analog voltage due to the object would be detected by Arduino and this signal is then sent in digital form to the Raspberry Pi. After verifying that the sensor has not been triggered by insects by comparing the input of Arduino to a threshold value, the Raspberry Pi instructs the webcam to take the picture of the person present in front of the webcam.
### Clicking Pictures
If the distance measured is less than a threshold value, then a command is given to click a photo using the webcam connected to the Raspberry Pi. The webcam is mounted on some surface to ensure proper image can be clicked when the system is triggered. “Open CV” library of python is used for this purpose.
### Face Recognition
To detect the face of the person, a database of familiar faces is created in Raspberry Pi. After the camera takes the picture of the person, facial recognition is carried out using wavelet transform. Wavelet transform has been used to realize feature extraction, because wavelet transform is localized in both time and frequency, as compared to Discrete Cosine Transform or Discrete Fourier Transform. Thus, it is more efficient and effective for facial recognition. Wavelet transform has obvious advantages in 2D images processing. First, wavelet transform is a multi-resolution. Second, wavelet transform calculates faster than other transforms. Third, wavelet transform extends the recognition’s range of target images. And after wavelet transform, data does not increase, and maybe reduce the computation. Forth, wavelet transform can realize denoise processing for images, so it could improve the accuracy of the facial recognition. “Face_recognition” module in Python has been used for this purpose. Further, to add the date and timestamp to the image, the “datetime” module has been used. “Numpy” module has been used to keep the output data of the face recognition part in matrices. If the face matches with a face in the database, the Raspberry Pi will take no action, but if it does not match then the photo is uploaded to Github or Firebase.
### Working of Application
App is programmed in such a way that it will fetch information from the servers. Server is a version-control system for tracking changes in computer files and coordinating work on those files among multiple people. It is primarily used for source-code management in software development, but it can be used to keep track of changes in any set of files. Here, MySQL has been used to fetch the images in the database. Also, the app has been created using Android Studio, and uses JSON script to pass PHP into the app. The information fetched by the app will consist of image with time and date. The app will then notify the user of the visitor. The user will be able to view the image of the visitor along with time and date stamp on his or her smartphone. In the case that visitor is offline or unable to use the phone then the images of unknown visitors can be seen in the app. In the app, after analysing the image, the user will have three buttons to press. The three buttons will perform the following actions:
1) Take action
2) Communicate via Intercom
3) Add to known images
* Take action:
Alarm that is interfaced with the hardware of the project will be triggered on pressing this
button. Each Pi device has a row of general-purpose input output (GPIO) pins which acts as an interface between the pi and the outside world. We can connect alarm to these pins and program them according to our requirements. The purpose of this alarm is to alert the neighbours of some sort of danger being present at the house/workplace. Furthermore, the user of the app can press ‘inform the police’ button. After this button is pressed, the dialling screen of the phone will open loaded with police’s number, so that the user can make a call and inform the police.
* Communicate via Intercom:
The user is presented with a second option in the app that will allow the user to talk to the visitor using the intercom. This intercom is set up at the door with the camera and Raspberry Pi. The intercom is connected to the internet via Wi-Fi or LAN network. VoIP will be used for this communication. We have used a third-party app called “Linphone” to set up a connection using SIP protocol. VoIP uses codecs to encapsulate audio into data packets, transmit the packets across an IP network and decapsulate the packets back into audio at the other end of the connection. By eliminating the use of circuit-switched networks for voice, VoIP reduces network infrastructure costs, enables providers to deliver voice services over their broadband and private networks, and allows enterprises to operate a single voice and data network. After ending the call, the user will be returned back to the screen with the three options again.
* Add to known images:
The user can press this button to add the clicked image to the known images database. This ensures that the person is detected as known the next time he/she visits. 

## Results
The results of various modules are elaborated below.
### Detection of Person
The object detection module includes both Arduino and the Raspberry Pi. The output is taken from the serial port of Arduino and seen on the Raspberry Pi.
As seen in the figure, the output in inches is seen on the Raspberry Pi. The system will continue taking this input till a value lesser than threshold is obtained.
As soon as a distance lesser than threshold distance is encountered, the system begins further operation by clicking the picture for analysis. In our case, we have kept the threshold distance as 10 inches.

<p align="center">
<img align="center" width="700" height="500" src="https://user-images.githubusercontent.com/61768243/77687376-abf3ea00-6f74-11ea-8de8-6be4fd3835e6.png">
</p>
<div align="center">Input from serial port of Arduino Uno when distance is greater than threshold</div>

<p align="center">
<img align="center" width="700" height="500"  src="https://user-images.githubusercontent.com/61768243/77688007-bc589480-6f75-11ea-9ac3-169c720e3b43.png">
</p>
<div align="center">Input from serial port of Arduino Uno when distance is less than threshold</div>

### Clicking of photo
After the distance is found to be lesser than threshold, an image is clicked by the webcam. The image as seen on the Raspberry Pi is shown in figure.

<p align="center">
<img align="center" width="700" height="500" src="https://user-images.githubusercontent.com/61768243/77688204-0ccff200-6f76-11ea-9ad1-fe9d9b0c91a4.png">
</p>
<div align="center">Image clicked using webcam as seen on Raspberry Pi</div>

###Face Recognition
The notification is sent to the app only if the person is unknown. The face recognition module checks whether the person is known by comparing with images in the known images database. If the face matches with the images in the known database, then the output is “1”, as shown in figure.

<p align="center">
<img align="center" width="700" height="100" src="https://user-images.githubusercontent.com/61768243/77688305-39840980-6f76-11ea-8295-56836727ae9f.png">
</p>
<div align="center">Output when face is present in the database</div>

Similarly, if the image does not match with the database, then the output is “0” as shown in the figure.

<p align="center">
<img align="center" width="700" height="100" src="https://user-images.githubusercontent.com/61768243/77688366-5e787c80-6f76-11ea-883e-ee74576280c1.png">
</p>
<div align="center">Output when face is not present in the database</div>

If the output is “0”, then the image is uploaded to the server and shown through the app to
the user.
### Application
The app first shows the images present in the database. On clicking the image, the app layout is as shown in the figure below.

<p align="center">
<img align="center"  src="https://user-images.githubusercontent.com/61768243/77688451-7d770e80-6f76-11ea-8c44-d5f04669ea89.png">
</p>
<div align="center">App Interface</div>

On pressing the buttons, the actions as mentioned above are carried out. Hence, entire project was successfully implemented.

##Conclusion
People visiting when a person is not present at their home or workplace is a common problem nowadays. Our project provides a low-cost and efficient solution to this problem, while simultaneously giving the user a variety of options to respond to the visitor. Depends on who is visiting, the user can either take no action, communicate with the person, or alert people if needed.   
Furthermore, one would not be disturbed if a familiar person visits, as in that case the system would not take any action using the face recognition software.   
The project ensures that one is always aware as to who visits the premises of their home/workplace and when, and thus alleviates the fear of missing an important delivery. Also, it enables a presence of any unscrupulous people in the vicinity.
Our project provides a low-cost alternative to the users, while providing a non-intrusive approach.
## Future Scope
The system can be made more efficient in the future.
* The face recognition algorithm can be made more efficient and the current success rate of 95% can be increased to be as close as possible to 100%
* The object detection module can be made more efficient.
## Applications
Apart from the application to work as a visitor detector at home/businesses, the app can be easily modified for other applications.
* By increasing number of object detectors and cameras, this system can be expanded to work as a low-cost security measure. The main advantage of this system is that it is non- intrusive, and hence the person coming into the bank can be recognised as he is walking in.
* This can also be implemented in airports as a security measure, in a similar way as mentioned in the previous point.

## References
[1] Behzad Shoarian Satari, Nor Azlina Abd Rahman, Zety Marla Zainal Abidin, “Face Recognition for Security Efficiency in Managing and Monitoring Visitors of an Organization”, IEEE 2014   
[2] Koluguri Neelima, K.Ashok Kumar, “Advance Security System with Intruder Image Capture and Forward Through Email”, IJMETMR 2016   
[3] Nareshkumar R. M., Apoorva Kamat, Dnyaneshvari Shinde, “Smart Door Security Control System Using Raspberry Pi”, IJIACS 2017   
[4] Swapnil Bilbile, Arti Barde, Shubham Waghmare, Monali Gabhane, Snehal Sahastrabudhey, “DOOR BELL NOTIFY WITH IMAGE CAPTURE AND FORWARD THROUGH EMAIL”, IJARIIE 2018   
[5] Nalini Bagal, Prof. Shivani Pandita, "Real-Time Transmission of Voice Over 802.11 Wireless Networks Using Raspberry Pi”, IJETST 2015   
[6] Ahmed Shabaan Samra, Salah El Taweel Gad Allah, Rehab Mahmoud Ibrahim, “Face Recognition Using Wavelet Transform, Fast Fourier Transform and Discrete Cosine Transform”, IEEE 2004   
[7] Ruolin Zhang, Jian Ding, “Facial Recognition Based on Wavelet Transform”, IEEE 2012   
[8] Alaeldden Abduelhadi, Mohmmed Elnour, “Smart Motion Detection”, IOSR-JEEE 2017   
[9] M. Vadivel, M. Poongodhai, R. Madhumitha, V. Nivetha, J.Kamila Banu, “IOT BASED HOME VISITOR MONITORING SYSTEM USING RASPBERRY PI”, IRJET 2018   
[10] Hyoung-Ro Lee, Chi-Ho Lin, Won-Jong Kim, “Development of an IoT-based Visitor Detection System”, IEEE 2016   
[11] Vaibhav A. Vyavahare, " Live Audio and Video Transmission System Using Raspberry Pi", IJIRCCE 2016   
[12] Nagula Shyam Kumar, Nivedita.M, ” IOT Based Advance Security System by Using Raspberry PI”, IJMETMR 2016   
[13] Documentation for app developers, Android developers, developer.android.com   
[14] Xiang-fei Nie, “Face recognition using wavelet transform and Kernel Principal Component Analysis”, IEEE 2010   
[15] Pallavi D. Wadkar, Megha Wankhade, “FACE RECOGNITION USING DISCRETE   
WAVELET TRANSFORMS”, IJAET 2012
[16] VOIP (Voice over Internet Protocol) Architecture and Features, esds.co.in   
[17] "What is a Raspberry Pi?", Raspberry Pi, 2019. [Online]. Available: https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/   
[18] "Arduino Uno", En.wikipedia.org, 2019. [Online]. Available: https://en.wikipedia.org/wiki/Arduino_Uno   
[19] R. Burnett and M. Inc., "Understanding How Ultrasonic Sensors Work - MaxBotix Inc.", MaxBotix Inc., 2019. [Online]. Available: https://www.maxbotix.com/articles/how-ultrasonic-sensors-work.html   
[20] M. Design, "EDIMAX - Wireless Adapters - N150 - N150 Wi-Fi Nano USB Adapter, Ideal for Raspberry Pi", Edimax.com, 2019. [Online]. Available: https://www.edimax.com/edimax/merchandise/merchandise_detail/data/edimax/global/wireless_adapters_n150/ew-7811un   
[21] "ATMega328P Microcontroller Pinout, Pin Configuration, Features & Datasheet", Components101.com, 2019. [Online]. Available: https://components101.com/microcontrollers/atmega328p-pinout-features-datasheet.   
[22] Akash v Bhatkule - Home Based Security Control System using Raspberry Pi and GSM, International Journal of Innovative Research in Computer and Communication Engineering, vol. 4, pp. 16259-16263, 2016   
[23] Anuradha.R.S, Bharathi.R - Optimized Door Locking and Unlocking Using IoT for Physically Challenged People, International Journal of Innovative Research in Computer and Communication Engineering, vol. 4, pp. 3397-3401, 2016.   
[24] S. Nazeem Basha, Dr. S.A.K. Jilani - An Intelligent Door System using Raspberry Pi and Amazon Web Services IoT, International Journal of Engineering Trends and Technology (IJETT), vol. 33, pp. 84-89, 2016   
[25] Nisarg Shroff, Pradeep Kauthale- IOT Based Home Automation system using Raspberry Pi-3, International Research Journal of Engineering and Technology (IRJET), vol. 4, pp. 2824-2826, 2017.   
[26] Rajendra Nayak, Neema Shetty - Secured Smart Home Monitoring System Using Raspberry-PI, International Journal Innovative Research and Development (IJIRD), vol. 5, pp. 339-342, 2016.   
[27] Zhao, Yanbo, and Zhaohui Ye. "A low-cost GSM/GPRS based wireless home security system." IEEE Transactions on Consumer Electronics 54.2 (2008).   
[28] Chowdhury, MdNasimuzzaman, MdShibleeNooman, and SrijonSarker. "Access Control of Door and Home Security by Raspberry Pi Through Internet." Int. J. Sci. Eng. Res 4 (2013): 550-558.   
[29] Patel, Urvija J., and Nehal G. Chitaliya. "Smart Sensing System using Internet of Things."   
[30] Rayte, Swapnali, et al. "Crime Monitoring and Controlling System by Mobile Device."   
[31] Piyare, Rajeev. "Internet of things: ubiquitous home control and monitoring system using android based smart phone." International Journal of Internet of Things 2.1 (2013): 5-11.   
[32] Prasad, Sanjana, et al. "Smart Surveillance Monitoring System Using Raspberry PI and PIR Sensor." Int. J. Comput. Sci. Inf. Technol 5 (2014): 7107-7109.   
[33] Ansari, Aamir Nizam, et al. "An Internet of things approach for motion detection using Raspberry Pi." Intelligent Computing and Internet of Things (ICIT), 2014 International Conference on. IEEE, 2015.   
[34] Friess, Peter. Internet of things: converging technologies for smart environments and integrated ecosystems. River Publishers, 2013.   
[35] Yun, Jaeseok, and Sang-Shin Lee. "Human movement detection and identification using pyroelectric infrared sensors." Sensors 14.5 (2014): 8057-8081.   
[36] Hossain, Md Khaled, and Sayed SamialHaq. "Detection of Car Pre-Crash with Human, Avoidance System & Localizing through GSM." International Journal of Scientific and Research Publications 3.7 (2013): 1-4.   
[37] Holton, Jon, and Tim Fratangelo. "Raspberry Pi Architecture." Raspberry Pi Foundation, London, UK (2012).   
[38] Richardson, Matt, and Shawn Wallace. Getting started with raspberry PI. " O'Reilly Media, Inc.", 2012.   
[39] Vaidya, Rohit Ratnakar. "Efficient Embedded Surveillance System with Auto Image Capturing and Email Sending Facility." International Journal of Technical Research and Applications (2015): 109-112.   
[40] Robinson, Andrew, and Mike Cook. Raspberry Pi Projects. John Wiley & Sons, 2013.   
[41] Jadhav, Gaurav, Kunal Jadhav, and Kavita Nadlamani. "Environment Monitoring System using Raspberry-Pi." (2016).   
[42] Rakesh, V. S., P. R. Sreesh, and Sudhish N. George, “An improved real-time surveillance system for home security system using BeagleBoard SBC, Zigbee and FTP webserver,” IEEE Int.Con, 2012, pp. 1240-1244.   
[43] Muheden, Karwan, Ebubekir Erdem, and Sercan Vanin, “Design and implementation of the mobile fire alarm system using wireless sensor networks,” IEEE Int.Symp.Computational Intelligence and Informatcs, 2016, pp. 000243-000246.   
[44] Kumar, Sushant, and S. S. Solanki, “Remote home surveillance system,” IEEE Int. Con. Advances in Computing, Communication, and Automation, 2016, pp. 1-4.   
[45] S. Sruthy , Sudhish N George “Wi-Fi enabled home security surveillance system using Raspberry Pi and IOT module”.   
[46] Muheden, Karwan, Ebubekir Erdem, and Sercan Vanin, “Design and implementation of the mobile fire alarm system using wireless sensor networks,” IEEE Int.Symp.Computational Intelligence and Informatcs, 2016, pp. 000243-000246.   
[47] Kumar, Sushant, and S. S. Solanki, “Remote home surveillance system,” IEEE Int. Con. Advances in Computing, Communication, and Automation, 2016, pp. 1-4.   
[48] S. Sruthy , Sudhish N George “Wi-Fi enabled home security surveillance system using Raspberry Pi and IOT module”.   
[49] RajeebLochan Dash, Mrs. A. RuhanBevi,” Real-time Transmission of Voice over 802.11 Wireless Networks Using Raspberry Pi” IJEDR 2014.   
[50] Available [online]: http: // www. raspberrypi. org /downloads   
[51] Available [online]: http://sourceforge.net/projects/win32diskimager/   
[52] Bhushan R Jichkar., "Proposed System for Placing Free Call over Wi-Fi Network Using VoIP and SIP", Int. Journal of Engineering Research and   
[53] Applications, ISSN:2248-9622, Vol.4, Issue 1( Version 3), pp.132-135, January 2014.   
[54] S.Sundar D.C.E, M. Krishna Kumar, P.Selvinpremkumar, M.Chinnadurai,“Voice Over Ip Via Bluetooth/Wi-Fi Peer To Peer”, IEEE Paper, March 30, 31, 2013.   
[55] Matt Richardson, Shawn Wallace, "Getting Started with Raspberry”, Brian Jepson, O'Reilly Media Inc., United States of America, first edition, pp.10-31, December 2012   
[56] Diptijavale, Bharti Dixit, Pankajjavale, “Performance Evaluation of Wireless Transmission Using Embedded System”, IEEE Paper, November 26, 2009.   
[57] G.SaiPrasanna, S.Karunakar, “Implementation of VoIP Communication on Embedded Systems”, IJRCCT, Jan, 2013.   
