import os 
import sys 
import csv
import json
import requests
import socket
import pywifi
import getpass 
import psycopg2  
import pandas as pd 
import subprocess 
import multiprocessing
import cv2, imutils, socket
import numpy as np
import time
import base64
import random 
import pywifi 
from PyQt5.QtCore import Qt, QSize, QTimer, QThread
from PyQt5 import QtCore, QtWidgets, uic,Qt,QtGui 
from PyQt5.QtWidgets import QApplication,QTreeView,QDirModel,QFileSystemModel,QVBoxLayout, QTreeWidget,QStyledItemDelegate, QTreeWidgetItem,QLabel,QGridLayout,QLineEdit,QDial,QComboBox,QTextEdit,QTabWidget,QLineEdit,QPushButton
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap,QIcon,QImage,QPalette,QBrush
from pyqtgraph.Qt import QtCore, QtGui  
import pyqtgraph as pg 
from pyqtgraph.flowchart import Flowchart, Node 
import pyqtgraph.flowchart.library as fclib 
from pyqtgraph.flowchart.library.common import CtrlNode
import pyqtgraph.metaarray as metaarray
import pyqtgraph.opengl as gl
from paramiko import SSHClient, AutoAddPolicy
import win32api 
drives = win32api.GetLogicalDriveStrings() 
drives = drives.split('\000')[:-1] 
  
DATABASE_URL = "postgres://wwpxpsshftlinh:b85574f77cd76ccbaef7a0f661086c6b28724d236c730c74c2d8021934e8bbe1@ec2-18-215-96-54.compute-1.amazonaws.com:5432/d8rl9i6joj63v8"
Host = "ec2-18-215-96-54.compute-1.amazonaws.com"
Database = "d8rl9i6joj63v8"
Password = "b85574f77cd76ccbaef7a0f661086c6b28724d236c730c74c2d8021934e8bbe1"
Port = "5432"
username = getpass.getuser()
print(username)
memwrite = []
OS_name = [] 
network_name = []
dict_cc = {} 
ip = [] 
Memhostpartip = [] 
Gateway_router = []
wifidict = {}
username = getpass.getuser()
print(username)
PATH_SD_CARD = "/media/"+str(username)  
name = "name"
code = "code"
ssidmem = [] 
dict_components = {}  
Check_found_components = [] 
Concatinate_components = []  
Classified_list_components = []
components = ['Imagesensor','Board','Computeronboard','ActuatorDriverIC','CellularLTEmod','SensorArray','Navigationsensor','AmplifiermoduleIC','Battery','BMSmodule'] # Getting the components  
Software_data = ['Objectdetection','Objectrecognition','Facerecognition','Posedetection','Poserecognition'] # Getting the data of software camera detection components 
communication_component = ['Serial-baudrate','CANBUS-baudrate']

listcommatch = {"Board":"Boarddata","Computeronboard":"Computernode","Imagesensor":"Imagecameramodule","Sensors":"Sensormodule","Acousticamplifier":"Acousticampmodule","Navigationsensor":"Navigationmodule","CellularLTEmod":"Cellularmodule","Battery":"Batterymodule","BMSmodule":"BMSmoduledata","ActuatorDriverIC":"Actuatormodule","SensorArray":"Sensorarraymodule","Materials":"MaterialsSkin"}
Matching_component_list = {}
country = [{name: 'Afghanistan', code: 'AF'}, 
  {name: 'Åland Islands', code: 'AX'}, 
  {name: 'Albania', code: 'AL'}, 
  {name: 'Algeria', code: 'DZ'}, 
  {name: 'American Samoa', code: 'AS'}, 
  {name: 'AndorrA', code: 'AD'}, 
  {name: 'Angola', code: 'AO'}, 
  {name: 'Anguilla', code: 'AI'}, 
  {name: 'Antarctica', code: 'AQ'}, 
  {name: 'Antigua and Barbuda', code: 'AG'}, 
  {name: 'Argentina', code: 'AR'}, 
  {name: 'Armenia', code: 'AM'}, 
  {name: 'Aruba', code: 'AW'}, 
  {name: 'Australia', code: 'AU'}, 
  {name: 'Austria', code: 'AT'}, 
  {name: 'Azerbaijan', code: 'AZ'}, 
  {name: 'Bahamas', code: 'BS'}, 
  {name: 'Bahrain', code: 'BH'}, 
  {name: 'Bangladesh', code: 'BD'}, 
  {name: 'Barbados', code: 'BB'}, 
  {name: 'Belarus', code: 'BY'}, 
  {name: 'Belgium', code: 'BE'}, 
  {name: 'Belize', code: 'BZ'}, 
  {name: 'Benin', code: 'BJ'}, 
  {name: 'Bermuda', code: 'BM'}, 
  {name: 'Bhutan', code: 'BT'}, 
  {name: 'Bolivia', code: 'BO'}, 
  {name: 'Bosnia and Herzegovina', code: 'BA'}, 
  {name: 'Botswana', code: 'BW'}, 
  {name: 'Bouvet Island', code: 'BV'}, 
  {name: 'Brazil', code: 'BR'}, 
  {name: 'British Indian Ocean Territory', code: 'IO'}, 
  {name: 'Brunei Darussalam', code: 'BN'}, 
  {name: 'Bulgaria', code: 'BG'}, 
  {name: 'Burkina Faso', code: 'BF'}, 
  {name: 'Burundi', code: 'BI'}, 
  {name: 'Cambodia', code: 'KH'}, 
  {name: 'Cameroon', code: 'CM'}, 
  {name: 'Canada', code: 'CA'}, 
  {name: 'Cape Verde', code: 'CV'}, 
  {name: 'Cayman Islands', code: 'KY'}, 
  {name: 'Central African Republic', code: 'CF'}, 
  {name: 'Chad', code: 'TD'}, 
  {name: 'Chile', code: 'CL'}, 
  {name: 'China', code: 'CN'}, 
  {name: 'Christmas Island', code: 'CX'}, 
  {name: 'Cocos (Keeling) Islands', code: 'CC'}, 
  {name: 'Colombia', code: 'CO'}, 
  {name: 'Comoros', code: 'KM'}, 
  {name: 'Congo', code: 'CG'}, 
  {name: 'Congo, The Democratic Republic of the', code: 'CD'}, 
  {name: 'Cook Islands', code: 'CK'}, 
  {name: 'Costa Rica', code: 'CR'}, 
  {name: 'Cote D\'Ivoire', code: 'CI'}, 
  {name: 'Croatia', code: 'HR'}, 
  {name: 'Cuba', code: 'CU'}, 
  {name: 'Cyprus', code: 'CY'}, 
  {name: 'Czech Republic', code: 'CZ'}, 
  {name: 'Denmark', code: 'DK'}, 
  {name: 'Djibouti', code: 'DJ'}, 
  {name: 'Dominica', code: 'DM'}, 
  {name: 'Dominican Republic', code: 'DO'}, 
  {name: 'Ecuador', code: 'EC'}, 
  {name: 'Egypt', code: 'EG'}, 
  {name: 'El Salvador', code: 'SV'}, 
  {name: 'Equatorial Guinea', code: 'GQ'}, 
  {name: 'Eritrea', code: 'ER'}, 
  {name: 'Estonia', code: 'EE'}, 
  {name: 'Ethiopia', code: 'ET'}, 
  {name: 'Falkland Islands (Malvinas)', code: 'FK'}, 
  {name: 'Faroe Islands', code: 'FO'}, 
  {name: 'Fiji', code: 'FJ'}, 
  {name: 'Finland', code: 'FI'}, 
  {name: 'France', code: 'FR'}, 
  {name: 'French Guiana', code: 'GF'}, 
  {name: 'French Polynesia', code: 'PF'}, 
  {name: 'French Southern Territories', code: 'TF'}, 
  {name: 'Gabon', code: 'GA'}, 
  {name: 'Gambia', code: 'GM'}, 
  {name: 'Georgia', code: 'GE'}, 
  {name: 'Germany', code: 'DE'}, 
  {name: 'Ghana', code: 'GH'}, 
  {name: 'Gibraltar', code: 'GI'}, 
  {name: 'Greece', code: 'GR'}, 
  {name: 'Greenland', code: 'GL'}, 
  {name: 'Grenada', code: 'GD'}, 
  {name: 'Guadeloupe', code: 'GP'}, 
  {name: 'Guam', code: 'GU'}, 
  {name: 'Guatemala', code: 'GT'}, 
  {name: 'Guernsey', code: 'GG'}, 
  {name: 'Guinea', code: 'GN'}, 
  {name: 'Guinea-Bissau', code: 'GW'}, 
  {name: 'Guyana', code: 'GY'}, 
  {name: 'Haiti', code: 'HT'}, 
  {name: 'Heard Island and Mcdonald Islands', code: 'HM'}, 
  {name: 'Holy See (Vatican City State)', code: 'VA'}, 
  {name: 'Honduras', code: 'HN'}, 
  {name: 'Hong Kong', code: 'HK'}, 
  {name: 'Hungary', code: 'HU'}, 
  {name: 'Iceland', code: 'IS'}, 
  {name: 'India', code: 'IN'}, 
  {name: 'Indonesia', code: 'ID'}, 
  {name: 'Iran, Islamic Republic Of', code: 'IR'}, 
  {name: 'Iraq', code: 'IQ'}, 
  {name: 'Ireland', code: 'IE'}, 
  {name: 'Isle of Man', code: 'IM'}, 
  {name: 'Israel', code: 'IL'}, 
  {name: 'Italy', code: 'IT'}, 
  {name: 'Jamaica', code: 'JM'}, 
  {name: 'Japan', code: 'JP'}, 
  {name: 'Jersey', code: 'JE'}, 
  {name: 'Jordan', code: 'JO'}, 
  {name: 'Kazakhstan', code: 'KZ'}, 
  {name: 'Kenya', code: 'KE'}, 
  {name: 'Kiribati', code: 'KI'}, 
  {name: 'Korea, Democratic People\'S Republic of', code: 'KP'}, 
  {name: 'Korea, Republic of', code: 'KR'}, 
  {name: 'Kuwait', code: 'KW'}, 
  {name: 'Kyrgyzstan', code: 'KG'}, 
  {name: 'Lao People\'S Democratic Republic', code: 'LA'}, 
  {name: 'Latvia', code: 'LV'}, 
  {name: 'Lebanon', code: 'LB'}, 
  {name: 'Lesotho', code: 'LS'}, 
  {name: 'Liberia', code: 'LR'}, 
  {name: 'Libyan Arab Jamahiriya', code: 'LY'}, 
  {name: 'Liechtenstein', code: 'LI'}, 
  {name: 'Lithuania', code: 'LT'}, 
  {name: 'Luxembourg', code: 'LU'}, 
  {name: 'Macao', code: 'MO'}, 
  {name: 'Macedonia, The Former Yugoslav Republic of', code: 'MK'}, 
  {name: 'Madagascar', code: 'MG'}, 
  {name: 'Malawi', code: 'MW'}, 
  {name: 'Malaysia', code: 'MY'}, 
  {name: 'Maldives', code: 'MV'}, 
  {name: 'Mali', code: 'ML'}, 
  {name: 'Malta', code: 'MT'}, 
  {name: 'Marshall Islands', code: 'MH'}, 
  {name: 'Martinique', code: 'MQ'}, 
  {name: 'Mauritania', code: 'MR'}, 
  {name: 'Mauritius', code: 'MU'}, 
  {name: 'Mayotte', code: 'YT'}, 
  {name: 'Mexico', code: 'MX'}, 
  {name: 'Micronesia, Federated States of', code: 'FM'}, 
  {name: 'Moldova, Republic of', code: 'MD'}, 
  {name: 'Monaco', code: 'MC'}, 
  {name: 'Mongolia', code: 'MN'}, 
  {name: 'Montserrat', code: 'MS'}, 
  {name: 'Morocco', code: 'MA'}, 
  {name: 'Mozambique', code: 'MZ'}, 
  {name: 'Myanmar', code: 'MM'}, 
  {name: 'Namibia', code: 'NA'}, 
  {name: 'Nauru', code: 'NR'}, 
  {name: 'Nepal', code: 'NP'}, 
  {name: 'Netherlands', code: 'NL'}, 
  {name: 'Netherlands Antilles', code: 'AN'}, 
  {name: 'New Caledonia', code: 'NC'}, 
  {name: 'New Zealand', code: 'NZ'}, 
  {name: 'Nicaragua', code: 'NI'}, 
  {name: 'Niger', code: 'NE'}, 
  {name: 'Nigeria', code: 'NG'}, 
  {name: 'Niue', code: 'NU'}, 
  {name: 'Norfolk Island', code: 'NF'}, 
  {name: 'Northern Mariana Islands', code: 'MP'}, 
  {name: 'Norway', code: 'NO'}, 
  {name: 'Oman', code: 'OM'}, 
  {name: 'Pakistan', code: 'PK'}, 
  {name: 'Palau', code: 'PW'}, 
  {name: 'Palestinian Territory, Occupied', code: 'PS'}, 
  {name: 'Panama', code: 'PA'}, 
  {name: 'Papua New Guinea', code: 'PG'}, 
  {name: 'Paraguay', code: 'PY'}, 
  {name: 'Peru', code: 'PE'}, 
  {name: 'Philippines', code: 'PH'}, 
  {name: 'Pitcairn', code: 'PN'}, 
  {name: 'Poland', code: 'PL'}, 
  {name: 'Portugal', code: 'PT'}, 
  {name: 'Puerto Rico', code: 'PR'}, 
  {name: 'Qatar', code: 'QA'}, 
  {name: 'Reunion', code: 'RE'}, 
  {name: 'Romania', code: 'RO'}, 
  {name: 'Russian Federation', code: 'RU'}, 
  {name: 'RWANDA', code: 'RW'}, 
  {name: 'Saint Helena', code: 'SH'}, 
  {name: 'Saint Kitts and Nevis', code: 'KN'}, 
  {name: 'Saint Lucia', code: 'LC'}, 
  {name: 'Saint Pierre and Miquelon', code: 'PM'}, 
  {name: 'Saint Vincent and the Grenadines', code: 'VC'}, 
  {name: 'Samoa', code: 'WS'}, 
  {name: 'San Marino', code: 'SM'}, 
  {name: 'Sao Tome and Principe', code: 'ST'}, 
  {name: 'Saudi Arabia', code: 'SA'}, 
  {name: 'Senegal', code: 'SN'}, 
  {name: 'Serbia and Montenegro', code: 'CS'}, 
  {name: 'Seychelles', code: 'SC'}, 
  {name: 'Sierra Leone', code: 'SL'}, 
  {name: 'Singapore', code: 'SG'}, 
  {name: 'Slovakia', code: 'SK'}, 
  {name: 'Slovenia', code: 'SI'}, 
  {name: 'Solomon Islands', code: 'SB'}, 
  {name: 'Somalia', code: 'SO'}, 
  {name: 'South Africa', code: 'ZA'}, 
  {name: 'South Georgia and the South Sandwich Islands', code: 'GS'}, 
  {name: 'Spain', code: 'ES'}, 
  {name: 'Sri Lanka', code: 'LK'}, 
  {name: 'Sudan', code: 'SD'}, 
  {name: 'Suriname', code: 'SR'}, 
  {name: 'Svalbard and Jan Mayen', code: 'SJ'}, 
  {name: 'Swaziland', code: 'SZ'}, 
  {name: 'Sweden', code: 'SE'}, 
  {name: 'Switzerland', code: 'CH'}, 
  {name: 'Syrian Arab Republic', code: 'SY'}, 
  {name: 'Taiwan, Province of China', code: 'TW'}, 
  {name: 'Tajikistan', code: 'TJ'}, 
  {name: 'Tanzania, United Republic of', code: 'TZ'}, 
  {name: 'Thailand', code: 'TH'}, 
  {name: 'Timor-Leste', code: 'TL'}, 
  {name: 'Togo', code: 'TG'}, 
  {name: 'Tokelau', code: 'TK'}, 
  {name: 'Tonga', code: 'TO'}, 
  {name: 'Trinidad and Tobago', code: 'TT'}, 
  {name: 'Tunisia', code: 'TN'}, 
  {name: 'Turkey', code: 'TR'}, 
  {name: 'Turkmenistan', code: 'TM'}, 
  {name: 'Turks and Caicos Islands', code: 'TC'}, 
  {name: 'Tuvalu', code: 'TV'}, 
  {name: 'Uganda', code: 'UG'}, 
  {name: 'Ukraine', code: 'UA'}, 
  {name: 'United Arab Emirates', code: 'AE'}, 
  {name: 'United Kingdom', code: 'GB'}, 
  {name: 'United States', code: 'US'}, 
  {name: 'United States Minor Outlying Islands', code: 'UM'}, 
  {name: 'Uruguay', code: 'UY'}, 
  {name: 'Uzbekistan', code: 'UZ'}, 
  {name: 'Vanuatu', code: 'VU'}, 
  {name: 'Venezuela', code: 'VE'}, 
  {name: 'Viet Nam', code: 'VN'}, 
  {name: 'Virgin Islands, British', code: 'VG'}, 
  {name: 'Virgin Islands, U.S.', code: 'VI'}, 
  {name: 'Wallis and Futuna', code: 'WF'}, 
  {name: 'Western Sahara', code: 'EH'}, 
  {name: 'Yemen', code: 'YE'}, 
  {name: 'Zambia', code: 'ZM'}, 
  {name: 'Zimbabwe', code: 'ZW'} 
]
selectedcountry = [] 
os_list = [' ','Linux Ubuntu x64 x86','Linux Debian x64 x86','Linux Ubuntu arm 32','Linux Debian arm 32','Linux Ubuntu arm 64','Linux Debian arm 64'] #The list of the operaring system on the system 
osmem = []
os.system("echo Hello"+"\t"+str(username))
parent_dir = "/Users/"+username+"/AppData/Local/Programs/" 
directory = ["Wifi_devices_connects","Robotics_nodes_json"]
mode = 0o777
for dric in range(0,len(directory)):
   try:
      print("Now creating.....",str(directory[dric]))  
      path = os.path.join(parent_dir, directory[dric]) 
      os.mkdir(path,mode)
   except:
       print(directory[dric]+" directory  was created")
nodelist = os.listdir(os.path.join(parent_dir,directory[1]))  
nodelist.append(" ")
storage_path = drives     
try:
 for re in range(0,len(storage_path)):
    generic_storage = os.listdir(storage_path[re]) 
    generic_mem = []
    generic_mem.append(" ")
    generic_mem.append("Generic storage"+str(generic_storage[re]))
except:
  print("Storage devices not found") 

devices = subprocess.check_output("arp -a",shell=True)
extract_devices = devices.decode('utf-8')
devices_list = extract_devices.split("wlo1")
hostname_mem = [] 
hostip_mem = []
automateip_add = {}
hoste_selected =[]
host_password =[]
host_remote = []
robothostname = []

wifi_mem = []
wifi_password = []
Sensors_data = [] 
global sensor_data_info, datasize
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
command_exec = ["roboreactorfirmware.sh","./roboreactorfirmware.sh","sudo service supervisorctl start","sudo service supervisor stop","sudo supervisorctl reread","sudo service supervisor restart"]   #Command to activate the service automaticly and accessing the data inside the singleboard computer via ssh  
r = requests.get('https://raw.githubusercontent.com/KornbotDevUltimatorKraton/Firmwareoflaptop/main/FirmwareNongpuserver.sh')
firmware = requests.get('https://raw.githubusercontent.com/KornbotDevUltimatorKraton/Firmwareoflaptop/main/FirmwareNongpuserver.sh')
try:
  Create_file_storage = os.mkdir(storage_path+"/"+"Roboreactor",mode) #Current storage data # Creating the file inside the directory  
  Current_wifi_path = os.mkdir(storage_path+"/"+"Roboreactor"+"/"+"Wifi_scan",mode) #
except:
    print("File created inside the directory")
client_username = []
port_mem = [] 
host = 'local host'
port = 5000 
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip)
        print(str(host_ip)) 
        ip.append(str(host_ip))
        print("Host part ip "+str(host_ip).split(".")[2])
        Memhostpartip.append(str(host_ip).split(".")[2]) 
        if Memhostpartip != [] and ip != []:
            if len(Memhostpartip) and len(ip) >=2: 
               ip.remove(ip[0]) 
               Memhostpartip.remove(Memhostpartip[0])
    except: 
        print("Unable to get Hostname and IP") 

class MainWindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()
        self.setFixedSize(1028, 670)

        uic.loadUi('Roboticfirmwaregenerator.ui', self)
        self.setWindowTitle('Roboreactor firmware generator  User:'+"\t"+client_username[0])
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkGray)
        self.setPalette(p)
        self.setPalette(p)
        oImage = QImage("bg2_new.jpeg")
        oImage.scaled(300,200)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)
        
        self.camera = self.findChild(QLabel,"label_5")
        self.camera.setFixedSize(751,551) 
        self.pushButton.clicked.connect(self.Writeimage)
        self.pushButton_2.clicked.connect(self.Remoteconfig) 
        self.pushButton_3.clicked.connect(self.Start_remote_robot) 
        self.pushButton_4.clicked.connect(self.Stop_remote_robot)
        self.pushButton_5.clicked.connect(self.Scan_host_machine) 
        self.pushButton_6.clicked.connect(self.Scan_wifi) 
        self.pushButton_7.clicked.connect(self.Logout) 
        self.pushButton_8.clicked.connect(self.Visual1)
        self.pushButton_9.clicked.connect(self.Restart_services) 
        self.pushButton_10.clicked.connect(self.Analyze_sensors)
        self.gridLayout = self.findChild(QGridLayout,"gridLayout")
        

        self.combo1 = self.findChild(QComboBox, "comboBox")
        self.combo2 = self.findChild(QComboBox,"comboBox_2")
        self.combo3 = self.findChild(QComboBox,"comboBox_3")
        self.combo4 = self.findChild(QComboBox, "comboBox_4")
        self.combo5 = self.findChild(QComboBox,"comboBox_5")
        self.combo7 = self.findChild(QComboBox,"comboBox_7")

        self.text6= self.findChild(QTextEdit,"textEdit_6") 
        self.text3 = self.findChild(QLineEdit,"lineEdit_2")  
        self.text3.setEchoMode(QLineEdit.Password) 
        self.text4 = self.findChild(QLineEdit,"lineEdit") 
        self.text4.setEchoMode(QLineEdit.Password) 
        self.text5 = self.findChild(QTextEdit,"textEdit_5")  
             #Tab widget 
        self.tabwidget = self.findChild(QTabWidget,'tabWidget') 
        self.cameras = self.findChild(QWidget,'Camera')
        self.nodes_robot = self.findChild(QWidget,'nodes') 
        
     
        
        self.combo1.activated.connect(self.Operatingsystem)
        self.combo1.addItems(os_list)
        self.combo2.activated.connect(self.Storage_generic)
        try:
           print("Access external storage devices")
           self.combo2.addItems(generic_mem)
        except:
           print("")
        self.combo3.activated.connect(self.robotnodes)
        self.combo3.addItems([" "])
        self.combo3.addItems(nodelist) 
        self.combo5.activated.connect(self.countrychoose) 
        
       
        print(host_password,wifi_password,robothostname)
        for countries in range(0,len(country)):
                       print(country[countries])
                       dict_cc[country[countries].get('name')] = country[countries].get('code')
        print(dict_cc)
        self.combo5.addItems(list(dict_cc))  
        self.combo4.activated.connect(self.hostname_data)
       
       
        get_Host_name_IP()
        for i in range(0,256): 
                 checkip_data = subprocess.check_output("nslookup 192.168."+str(Memhostpartip[0])+"."+str(i),shell=True) 
                 print(checkip_data.decode().split(" ")) 
                 gettingdata  = checkip_data.decode().split(" ") 
                 if len(gettingdata) > 6:
                    print("Detect the devices connected to the network")
                    print(gettingdata[0],gettingdata[2].split("\r\n"),gettingdata[4].split("\r\n"),gettingdata[8].split("\r\n"),gettingdata[10].split("\r\n"))       
                    print("Host detected: ",gettingdata[8].split("\r\n"),gettingdata[10].split("\r\n"))
                    hostip_mem.append(gettingdata[8].split("\r\n")[0])
                    automateip_add[gettingdata[8].split("\r\n")[0]] = gettingdata[10].split("\r\n")[0] 
                    time.sleep(0.05) 


        self.combo4.addItems(automateip_add.keys())  
        print(automateip_add)
        self.combo7.activated.connect(self.wifissid)
       
       
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        iface.scan()
        time.sleep(0.5)
        results = iface.scan_results()
        for er in range(0,3):
          for i in results:
             bssid = i.bssid
             ssid  = i.ssid
            
             wifidict[ssid] = bssid
        print(wifidict)
        print("Show list wifi scanner")
        for i in list(wifidict):
                     print(i) 
                     self.combo7.addItems([" "]) 
                     self.combo7.addItems(list(wifidict))
                     print(list(wifidict))
        
       

    def Visual1(self): 
        
           print("Connecting the ip camera")
           self.Worker1 = Worker1() 
           self.Worker1.start()
           self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
    def ImageUpdateSlot(self, Image):
            self.pixmap = QPixmap.fromImage(Image)
            self.camera.setPixmap(self.pixmap) 
    def wifissid(self,wifi_index):
             print(list(wifidict)[wifi_index])
             if len(network_name) < len(list(wifidict)):
                   network_name.append(list(wifidict)[wifi_index-1]) 
             if len(network_name) >1:
                   network_name.remove(network_name[0]) 
             print(network_name)      
    def hostip_data(self,hostip_index):
         try: 
             print(automateip_add.keys()[hostip_index-1])
         except: 
             print("Host scan ip cannot be using on the window operating system")    
    def hostname_data(self,host_index):
             print(host_index)
             print(automateip_add.get(list(automateip_add)[host_index])) 
             
             if str(automateip_add.get(list(automateip_add)[host_index])) not in list(automateip_add):
                       hostip_mem.append(automateip_add.get(list(automateip_add)[host_index]))
                       print(hostip_mem)
             if len(automateip_add.keys()) > 1:
                       hostip_mem.remove(hostip_mem[0])
             
    def Storage_generic(self,index_storage):
                print(generic_mem[index_storage])
    def robotnodes(self,nodes_list):
        print(nodelist[nodes_list]) 
        print("Start generate node components data")
       
        f = open(parent_dir+"Robotics_nodes_json"+"/"+nodelist[nodes_list])
       
        data_components = json.load(f)     
        
        fc = Flowchart(terminals={
            'GPIO_2': {'io': 'in'},
            'Sensor1': {'io': 'out'}    
        })
        
        w = fc.widget() 
        self.gridLayout.addWidget(fc.widget(), 0, 0, 2, 1)


    def Operatingsystem(self,osp):
             print(os_list[osp])
             if osmem !=[]:
                   osmem.append(os_list[osp])
             if len(osmem) > 1:
                  osmem.remove(osmem[len(osmem)-1]) 
             print(osmem)    
    def countrychoose(self,countries_cc):
                 
              try:
                 print(list(dict_cc)[countries_cc])
                 get_extracted = list(dict_cc)[countries_cc]
                 selected_cc = dict_cc.get(get_extracted)
                 print(selected_cc)
                 selectedcountry.append(selected_cc)
                 print("Store country breviation successfully....")
              except: 
                   print("Store country breviation error")
    def Remoteconfig(self):
       print("Operating remote config on the robot......") 
       if len(robothostname) <=0:
                    robothostname.append(self.text5.toPlainText())
       if len(robothostname) >1:
                    robothostname.remove(robothostname[0])
       if len(host_password) <=0:
                 host_password.append(self.text3.text()) 
       if len(host_password) >1:
                 host_password.remove(host_password[0])
       try:     
           print(robothostname[0],hostip_mem[0],host_password[0])          
           with SSHClient() as client:
                     client.set_missing_host_key_policy(AutoAddPolicy())
                     print(robothostname)
                     print(hostip_mem[0],robothostname[0],host_password[0])
                     client.connect(hostname=str(hostip_mem[0]),username=str(robothostname[0]),password=str(host_password[0]),look_for_keys=False)  
                     command = ["ls","python3 wifiscanner.py","lsusb"]
                    
                     try:
                         print("Remote chmod permission")
                         stdin, stdout, stderr = client.exec_command("sudo -S <<< " +str(host_password[0])+" chmod +x "+command_exec[0],get_pty=True)
                         lines = stdout.readlines()
                         print(lines)
                        
                        
                         msgbox = QtWidgets.QMessageBox()
                         msgbox.setText('Finish robogenerator firmware generated')
                         msgbox.setTextInteractionFlags(QtCore.Qt.NoTextInteraction) 
                         stdin, stdout, stderr = client.exec_command(command[0],get_pty=True)
                         lines = stdout.readlines()
                         for dataremote in range(0,len(lines)):   
                              msgbox.setDetailedText(lines[dataremote]+"\n")
                         msgbox.exec() 
                       
                         
                     except:
                         print("Remote chmod permission fail")
                     
       except: 
            print("You haven't upload firmware and config to the SD card")
    def Analyze_sensors(self): 
      try:
        
        print("Start generate node components data")
        Classification_components_func(username) 
        
        k = 4         
        
        fc = Flowchart(terminals={      
            'dataIn':{'io':'in'},
            'dataOut':{'io':'out'}
        })
        win = QtGui.QMainWindow() 
        win.setWindowTitle('Robot nodes flowchart')
        w = fc.widget() 
        self.gridLayout.addWidget(fc.widget(), 0, 0, 2, 1)
       
        datacomponents = Classification_components_func(username)
        if Classified_list_components !=[]: 
                Classified_list_components.clear()
        for rt in range(0,len(list(datacomponents))):
                 if list(datacomponents)[rt].split(',')[0] in components: 
                            print("Found components: ",list(datacomponents)[rt].split(',')[0]) 
                            Matching_component_list[list(datacomponents)[rt].split(",")[0]+"_"+str(rt)] = list(datacomponents)[rt] 
                            Classified_list_components.append(list(datacomponents)[rt].split(',')[0])
        
        print("Components found: ",len(Classified_list_components))
       
        for re in range(0,len(Classified_list_components)): 
         
           print("Components name and amount: ", datacomponents.get(list(Matching_component_list.values())[re])) 
           
           exec("v"+str(re)+"="+"pg."+"ImageView"+"()")  
           if re%2 == 0:
               exec("self.gridLayout.addWidget(v"+str(re)+","+str(re)+", "+str(re%2+1)+")")
           if re%2 == 1: 
               exec("self.gridLayout.addWidget(v"+str(re)+","+str(re-1)+", "+str(re%2+1)+")")
        
        library = fclib.LIBRARY.copy() 
        library.addNodeType(Computeronboard,[('Display',)]) 
        library.addNodeType(Board,[('Display,')])
        library.addNodeType(CellularLTEmod,[('Display',)])
        library.addNodeType(ActuatorDriverIC,[('Display',)])
        library.addNodeType(Imagesensor,[('Display',)])
        library.addNodeType(BMSmodule,[('Display',)])
        library.addNodeType(Battery,[('Display',)])
        library.addNodeType(SensorArray,[('Display',)])
        library.addNodeType(Materials,[('Display',)])
        library.addNodeType(Acousticamplifier,[('Display',)])
        library.addNodeType(Navigationsensor,[('Display',)])

        fc.setLibrary(library)
       
       
        posparameter = k*len(Classified_list_components)
        if len(Classified_list_components) == 1: 
            for rww in range(0,len(Classified_list_components)):

                     print(Classified_list_components[rww],listcommatch.get(Classified_list_components[rww]))
                     number_list = random.sample(range(-150-posparameter,150+posparameter),len(Classified_list_components))
                   
                     vNode = fc.createNode(listcommatch.get(Classified_list_components[rww]),pos=(number_list[0],number_list[1]))  
        
        if len(Classified_list_components) > 1:
           for rww in range(0,len(Classified_list_components)):
                     print(Classified_list_components[rww],listcommatch.get(Classified_list_components[rww]))
                     number_list = random.sample(range(-150-posparameter,150+posparameter),len(Classified_list_components))
                   
                     vNode = fc.createNode(listcommatch.get(Classified_list_components[rww]),pos=(number_list[0],number_list[1]))
        
      except: 
          print("host machine ip "+hostip_mem[0]+':5000')
          print("Host mechine may not config firmware to report sensors data")
    
    def Scan_wifi(self): 
        print('Mapping wifi") #Start mapping wifi')  
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        iface.scan()
        time.sleep(0.5)
        results = iface.scan_results()
        for er in range(0,3):
          for i in results:
             bssid = i.bssid
             ssid  = i.ssid
           
             wifidict[ssid] = bssid
             
        print(wifidict)
        
                    
    def Start_remote_robot(self): 
        print("Start service robot to operating at boot services")
        print("Sending the activate ip port")
      
    def Restart_services(self): 
           print("Restart service robot operating at boot services")
    def Stop_remote_robot(self):
           print("Stop service robot to operating at boot services")
    def Scan_host_machine(self):
        print("Start scanning the host machine") #
       
        for i in range(0,256): 
                 checkip_data = subprocess.check_output("nslookup 192.168."+str(Memhostpartip[0])+"."+str(i),shell=True)
                 print(checkip_data.decode().split(" ")) 
                 gettingdata  = checkip_data.decode().split(" ") 
                 if len(gettingdata) > 6:
                    print("Detect the devices connected to the network")
                    print(gettingdata[0],gettingdata[2].split("\r\n"),gettingdata[4].split("\r\n"),gettingdata[8].split("\r\n"),gettingdata[10].split("\r\n")) 
                    hostip_mem.append(gettingdata[8].split("\r\n")[0])
                    automateip_add[gettingdata[8].split("\r\n")[0]] = gettingdata[10].split("\r\n")[0] 
                    time.sleep(0.02) 
                    print(automateip_add)
    def Logout(self):
          print("Logging out from the system")
          self.w = MainWindow()
          self.w.show() 
          self.hide() 
    def Writeimage(self):
           
            if len(wifi_password) <=0:
                     wifi_password.append(self.text4.toPlainText())
            if len(wifi_password) >1:
                     wifi_password.remove(wifi_password[0]) 

            print(host_password,wifi_password)
            if memwrite ==[]:
                    memwrite.append("Write")
            if len(memwrite) >1:
                   memwrite.remove(memwrite[len(memwrite)]) 
            print("Start writing the firmware on boot........") 
                
            target_rpi = ["boot","rootfs","/home/pi","system-boot","writable"]   
            list_seek_boot = os.listdir(PATH_SD_CARD) 
            print("Seek dir",list_seek_boot)
            print(network_name[0])
            print(wifi_password[0])
            for re in range(0,len(list_seek_boot)):
                                                          
                                      if list_seek_boot[re] == str(target_rpi[1]):
                                                  print("Found "+str(list_seek_boot[re])+" Now operating firmware injection.......")
                                                  bashwriter = open(PATH_SD_CARD+"/"+list_seek_boot[re]+target_rpi[2]+"/"+"roboreactorfirmware.sh",'w') 
                                                  bashwriter.write(r.text)
                                                  bashwriter.close() 
                                      if list_seek_boot[re] == str(target_rpi[0]):
                                                  print("Found "+str(list_seek_boot[re])+" Now operating setting SSH and WiFi.......")
                                                  filessh = open(PATH_SD_CARD+"/"+list_seek_boot[re]+"/"+"ssh","w") 
                                                  filessh.write(" ")
                                                  filessh.close()

                                                  filewpa_supplicant = open(PATH_SD_CARD+"/"+list_seek_boot[re]+"/"+"wpa_supplicant.conf",'w')
                                                  print(selectedcountry)
                                                  filewpa_supplicant.write("country="+selectedcountry[0]+"\n") #Getting the country
                                                  filewpa_supplicant.write("ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev"+"\n")
                                                  filewpa_supplicant.write("update_config=1"+"\n")
                                                  filewpa_supplicant.write("network={"+"\n")
                                                  SSIDs = '"' + network_name[0] +'"'
                                                  SIDpass = '"' + wifi_password[0] + '"'
                                                  filewpa_supplicant.write("ssid="+SSIDs+"\n")  
                                                  filewpa_supplicant.write("psk="+SIDpass+"\n")  
                                                  filewpa_supplicant.write("key_mgmt=WPA-PSK"+"\n")
                                                  filewpa_supplicant.write("}"+"\n")  
                                                  filewpa_supplicant.close()
                                                 
                                                  cmdfileconfig = open(PATH_SD_CARD+"/"+list_seek_boot[re]+"/"+"cmdline.txt",'w') 
                                                  cmdfileconfig.write("root=PARTUUID=f4481065-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet init=/usr/lib/raspi-config/init_resize.sh splash plymouth.ignore-serial-consoles") 
                                                  cmdfileconfig.close() 
                                                  configfile = open(PATH_SD_CARD+"/"+list_seek_boot[re]+"/"+"config.txt",'w') 
                                                  configfile.write("#Uncomment some or all of these to enable the optional hardware interfaces")
                                                  configfile.write("dtparam=i2c_arm=on"+"\n")
                                                  configfile.write("#dtparam=i2s=on"+"\n")
                                                  configfile.write("dtparam=spi=on"+"\n")
                                                  configfile.write("dtparam=audio=on"+"\n")
                                                  configfile.write("[pi4]"+"\n")
                                                  configfile.write("#Enable DRM VC4 V3D driver on top of the dispmanx display stack"+"\n")
                                                  configfile.write("dtoverlay=vc4-fkms-v3d"+"\n")
                                                  configfile.write("max_framebuffers=2"+"\n")
                                                  configfile.write("[all]"+"\n")
                                                  configfile.write("#dtoverlay=vc4-fkms-v3d"+"\n")
                                                  configfile.write("start_x=1"+"\n")
                                                  configfile.write("gpu_mem=128"+"\n")
                                                  configfile.write("enable_uart=1"+"\n")
                                                  configfile.close() 

                                    
                                      if list_seek_boot[re] == str(target_rpi[3]):                                
                                                   print("system-boot",list_seek_boot[re]) 

                                      if list_seek_boot[re] == str(target_rpi[4]):
                                                   print("writable",list_seek_boot[re])
                                      

def Classification_components_func(username): 
    f = open("C:/Users/"+username+"/AppData/Local/Programs/Robotics_nodes_json/codeconfiggen.json") 
    
    datacom = json.load(f)
    print(datacom)
    Check_found_components = [] 
    Concatinate_components = []  
    
    components = ['Imagesensor','Board','Computeronboard','ActuatorDriverIC','CellularLTEmodule','SensorArray','Navigationsensor','AmplifiermoduleIC','Battery','BMSmodule']
    Software_data = ['Objectdetection','Objectrecognition','Facerecognition','Posedetection','Poserecognition'] 
    communication_component = ['Serial-baudrate','CANBUS-baudrate']
    for ire in range(0,len(datacom)): 
        print(datacom[ire])
        if len(datacom[ire]) == 2: 
                dict_components[datacom[ire][0]] = datacom[ire][1] 
        if len(datacom[ire]) >2: 
                 getsplit_com = datacom[ire].split(":")
                 top_dat = datacom[ire][0]
                 dict_components[getsplit_com[0]] = getsplit_com[1] 
    print(dict_components) 
    print(list(dict_components)) 
    for ir in list(dict_components): 
         if ir.split(",")[0] in components: 
                    print("Found the components",ir.split(",")[0])
    for rex in list(dict_components): 
         Concatinate_components.append(rex+","+dict_components.get(rex)) 
    print(Concatinate_components)
    for listdata in range(0,len(Concatinate_components)): 
           print(Concatinate_components[listdata])

    for commu in list(dict_components): 
        if commu in communication_component: 
                  print("Found communication protocol",commu,dict_components.get(commu))
    print(dict_components) 
    return dict_components
           
class Board(Node):
    """Node that displays image data in an ImageView widget"""
    nodeName = 'Boarddata'
    
    def __init__(self, name):
        self.view = None
        Node.__init__(self, name, terminals={'data': {'io':'in'}})
        
    def setView(self, view): 
        self.view = view
        
    def process(self, data, display=True):
      
        
        if display and self.view is not None:
            if data is None:
                self.view.setImage(np.zeros((1,1))) 
            else:
                self.view.setImage(data)
    
class Computeronboard(Node):
    """Node that displays image data in an ImageView widget"""
    nodeName = 'Computernode'
    
    def __init__(self, name):
        self.view = None
        Node.__init__(self, name, terminals={'data': {'io':'in'}})
        
    def setView(self, view): 
        self.view = view
        
    def process(self, data, display=True):
      
        if display and self.view is not None:
            if data is None:
                self.view.setImage(np.zeros((1,1)))
                self.view.setImage(data)

class Imagesensor(Node):
    """Node that displays image data in an ImageView widget"""
    nodeName = 'Imagecameramodule'
    
    def __init__(self, name):
        self.view = None
        Node.__init__(self, name, terminals={'data': {'io':'in'}})
        
    def setView(self, view):  
        self.view = view
        
    def process(self, data, display=True):
       
        
        if display and self.view is not None:
            if data is None:
                self.view.setImage(np.zeros((1,1))) 
            else:
                self.view.setImage(data)

class Sensors(Node):
    """Node that displays image data in an ImageView widget"""
    nodeName = 'Sensormodule'
    
    def __init__(self, name):
        self.view = None
        Node.__init__(self, name, terminals={'data': {'io':'in'}})
        
    def setView(self, view): 
        self.view = view
        
    def process(self, data, display=True):
      
        if display and self.view is not None:
            if data is None:
                self.view.setImage(np.zeros((1,1))) 
            else:
                self.view.setImage(data)

class Acousticamplifier(Node):
    nodeName = 'Acoustticampmodule'
    
    def __init__(self, name):
        self.view = None
        Node.__init__(self, name, terminals={'data': {'io':'in'}})
        
    def setView(self, view):  
        self.view = view
        
    def process(self, data, display=True):
       
        
        if display and self.view is not None:
            if data is None:
                self.view.setImage(np.zeros((1,1))) 
            else:
                self.view.setImage(data)
class Navigationsensor(Node):
    
    nodeName = 'Navigationmodule'
    
    def __init__(self, name):
        self.view = None
        Node.__init__(self, name, terminals={'data': {'io':'in'}})
        
    def setView(self, view): 
        self.view = view
        
    def process(self, data, display=True):
       
        
        if display and self.view is not None:
            if data is None:
                self.view.setImage(np.zeros((1,1))) 
            else:
                self.view.setImage(data)

class CellularLTEmod(Node):
    """Node that displays image data in an ImageView widget"""
    nodeName = 'Cellularmodule'
    
    def __init__(self, name):
        self.view = None
        Node.__init__(self, name, terminals={'data': {'io':'in'}})
        
    def setView(self, view): 
        self.view = view
        
    def process(self, data, display=True):
      
        
        if display and self.view is not None:
            if data is None:
                self.view.setImage(np.zeros((1,1))) 
            else:
                self.view.setImage(data)
class Battery(Node):
    """Node that displays image data in an ImageView widget"""
    nodeName = 'Batterymodule'
    
    def __init__(self, name):
        self.view = None
        Node.__init__(self, name, terminals={'data': {'io':'in'}})
        
    def setView(self, view): 
        self.view = view
        
    def process(self, data, display=True):
    
        if display and self.view is not None:
            if data is None:
                self.view.setImage(np.zeros((1,1))) 
            else:
                self.view.setImage(data)
class BMSmodule(Node):
  
    nodeName = 'BMSmoduledata'
    
    def __init__(self, name):
        self.view = None
        Node.__init__(self, name, terminals={'data': {'io':'in'}})
        
    def setView(self, view):  
        self.view = view
        
    def process(self, data, display=True):
      
        
        if display and self.view is not None:
            if data is None:
                self.view.setImage(np.zeros((1,1)))
            else:
                self.view.setImage(data)
class ActuatorDriverIC(Node):
    nodeName = 'Actuatormodule'
    
    def __init__(self, name):
        self.view = None
        Node.__init__(self, name, terminals={'data': {'io':'in'}})
        
    def setView(self, view): 
        self.view = view
        
    def process(self, data, display=True):
      
        
        if display and self.view is not None:
           
            if data is None:
                self.view.setImage(np.zeros((1,1)))
            else:
                self.view.setImage(data)
class SensorArray(Node):
    
   
    nodeName = 'Sensorarraymodule'
    
    def __init__(self, name):
        self.view = None
        Node.__init__(self, name, terminals={'data': {'io':'in'}})
        
    def setView(self, view): 
        self.view = view
        
    def process(self, data, display=True):
      
        
        if display and self.view is not None:
            if data is None:
                self.view.setImage(np.zeros((1,1))) 
            else:
                self.view.setImage(data)
class Materials(CtrlNode):
    nodeName = 'MaterialsSkin'
    
    def __init__(self, name):
        self.view = None
        Node.__init__(self, name, terminals={'data': {'io':'in'}})
        
    def setView(self, view): 
        self.view = view
        
    def process(self, data, display=True):
       
        
        if display and self.view is not None:
            if data is None:
                self.view.setImage(np.zeros((1,1))) 
            else:
                self.view.setImage(data)


class MainWindow(QtWidgets.QMainWindow):
   
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setFixedSize(496, 310)
        uic.loadUi('Loginpage.ui', self)
        self.setWindowTitle('Welcome to roboreactor User:'+"\t"+username)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkGray)
        self.setPalette(p)
        oImage = QImage("kobuki_new.jpg")
        oImage.scaled(300,200)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)
        self.pushButton.clicked.connect(self.Login)
        self.text = self.findChild(QTextEdit,"textEdit") 
        self.text2 = self.findChild(QLineEdit,"lineEdit") 
        self.text2.setEchoMode(QLineEdit.Password)
        self.label.setStyleSheet("color:white") 
        self.label_2.setStyleSheet("color:white")
        self.label_3.setStyleSheet("color:white")
        query()   
    def Login(self):
            print("Logging into the database......")
            usernamedata = self.text.toPlainText()
            passworddata = self.text2.text()
            print(usernamedata,passworddata) 
            
            conn = psycopg2.connect(
               DATABASE_URL,
               sslmode='require',
            )
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS customers
            (index Text,
            first_name Text,
            last_name Text,
            e_mail Text,
            password Text,
            address Text,
            payment_status Text,
            cardholder Text,
            schedule Text,
            recharge Text);''')
            c = conn.cursor()
            c.execute("SELECT*FROM customers")
            records = c.fetchall() 
            print(records[0])
            print("Amount of customers:",len(records)) 
            am_customers = len(records)
            for rec in range(0,len(records)):
                   if usernamedata == records[rec][3]:
                       print("Username correct!")
                       if passworddata == records[rec][4]:
                               print("Password correct!")
                               if client_username != []: 
                                  client_username.clear() 
                               if client_username == []:
                                  print("Getting the name record into the client username array to get the new title name")
                                  client_username.append(str(records[rec][1]) +"\t"+str(records[rec][2])) 
                               self.w = MainWindow2()
                               self.w.show() 
                               self.hide() 
                               break
                   
            conn.close()
def psi(i, j, k, offset=(50,50,100)):
    x = i-offset[0]
    y = j-offset[1]
    z = k-offset[2]
    th = np.arctan2(z, (x**2+y**2)**0.5)
    phi = np.arctan2(y, x)
    r = (x**2 + y**2 + z **2)**0.5
    a0 = 2
    ps = (1./81.) * 1./(6.*np.pi)**0.5 * (1./a0)**(3/2) * (r/a0)**2 * np.exp(-r/(3*a0)) * (3 * np.cos(th)**2 - 1)
    return ps
           
def pinger(job_q, results_q):
    
    DEVNULL = open(os.devnull, 'w')
    while True:

        ip = job_q.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass


def get_my_ip():
    """
    Find my IP address
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def map_network(pool_size=255):
   

    ip_list = list()

    ip_parts = get_my_ip().split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]

    for p in pool:
        p.start()

    for i in range(1, 255):
        jobs.put(base_ip + '{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    while not results.empty():
        ip = results.get()
        ip_list.append(ip)

    return ip_list
class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        
        #UDP socket client 
        BUFF_SIZE = 65536
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
        host_name = socket.gethostname()
        message = b'Hello'
        port = 9800
        client_socket.sendto(message,(hostip_mem[0],port))
        fps,st,frames_to_count,cnt = (0,0,20,0) 
        self.ThreadActive = True
        while self.ThreadActive:
        
            packet,_ = client_socket.recvfrom(BUFF_SIZE)
            data = base64.b64decode(packet,' /')
            npdata = np.fromstring(data,dtype=np.uint8)
            Image = cv2.imdecode(npdata,1)
            Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
            Image = cv2.putText(Image,'FPS: '+str(fps),(10,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),1)
            FlippedImage = cv2.flip(Image, 1)
            ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
            Pic = ConvertToQtFormat.scaled(751, 551, Qt.KeepAspectRatio) 
            self.ImageUpdate.emit(Pic)
            key = cv2.waitKey(1) & 0xFF 
            if key == ord('q'):
                client_socket.close() 
                break 
            
            if cnt == frames_to_count:
                     try:
                         fps = round(frames_to_count/time.time()-st) 
                         st=time.time() 
                         cnt=0
                     except:
                         pass 
            cnt+=1              
                
    def stop(self):
        self.ThreadActive = False
        self.quit()
def query():
    
      conn = psycopg2.connect(
               DATABASE_URL,
               sslmode='require',
      )
      c = conn.cursor()
      c.execute('''CREATE TABLE IF NOT EXISTS customers
      (index Text,
      first_name Text,
      last_name Text,
      e_mail Text,
      password Text,
      address Text,
      payment_status Text,
      Cardholder Text,
      schedule Text,
      Recharge Text);
      ''')
      conn.commit()
      conn.close()
      

def main():
    app = QtWidgets.QApplication(sys.argv)
     
    main = MainWindow()
    main.show()
    
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
     main()
     