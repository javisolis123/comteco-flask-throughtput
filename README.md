# Bandwidth and throughtput meter


**Description**

Tool that helps technicians and specialists in the area of telecommunications to be able to make the certifications of a communication 
channel at the IP level, in addition to being able to generate real-time graphs of the behavior of the channel for a greater and easy 
understanding for the technician or specialist.

**BANDWIDTH**

Bandwidth is measured as the amount of data that can be transferred between two points on a network in a specific
time. Bandwidth is typically measured in bits per second (bps) and expressed as a bit rate.
Bandwidth denotes the transmission capacity of a connection and is an important factor in determining the 
quality and speed of a network.
Bandwidth was originally measured in bits per second and expressed as bps. However, today's networks often 
have much higher bandwidth than can be comfortably expressed using such small units. Today, it is common to 
see larger numbers denoted with metric prefixes such as Mbps (megabits per second), Gbps (gigabits per second),
or Tbps (terabits per second).

```
K = kilo = 1,000 bits
M = mega = 1,000 kilo = 1,000,000 bits
G = giga = 1,000 mega = 1,000,000,000 bits
T = tera = 1,000 giga = 1,000,000,000,000 bits
```
After terabit there is petabit, exabit, zettabit and yottabit, each representing an additional power of 10.
Bandwidth can also be expressed in bytes per second, which is usually denoted by a capital B. For example, 
10 megabytes per second would be expressed as 10 MB/s or 10 MBps.

**REQUIRED HARDWARE**

The software was programmed and designed to operate on two raspberry pi 3B+, but it is also 
compatible with computers that have i3 processors or higher with 1 GB of RAM and 10 MB of disk 
space and a minimum Gigabit Ethernet connection.

**REQUIRED SOFTWARE**

* 1.- Linux OS (Debian or Ubuntu)
* 2.- MariaDB
* 3.- Python 3

**INSTALLATION**

* 1.- Virtual Environment
```
$ sudo apt install virtualenv
```
* 2.- Clone the repository
```
$ git clone https://github.com/javisolis123/comteco-flask-throughtput.git
```
* 3.- Execute de repository installation
```
pip install -r requirements.txt
```
* 4.- Import de DataBase.
* 5.- Enjoy It!.


