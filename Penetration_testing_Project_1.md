Penetration Testing Project 1

Project Title: Ddos and Telnet exploit 

Objective: Assess the security posture of a network to identify and address potential vulnerabilities.

Scope: The assessment covered internal network infrastructure, TCP/IP and access controls. This involved testing Telnet vulnerabilities and potential attack vectors that could be exploited by an attacker. Also wanted to show how Wireshark can identify a Ddos attack with Syn flood.

Tools and Techniques:

Nmap: Used for network discovery and identifying open ports and services. 
Metasploit: Utilized for exploiting discovered vulnerabilities and validating their impact.
Wireshark: Network Analysis tool
 

Using Metasploitable on Kali linux, I wanted to do a Ddos attack on the Windows Machine, and Capture the packets with Wireshark.

So on Kali linux I used the Metasploit framwork, start it with the command msfconsole, and was looking for a Ddos attack.

I found the a Synflood attack, so I gave the target IP set RHOST, and started the attack.

Wireshark successfully captured the packets.

![Screenshot 2023-11-25 172446](https://github.com/messor89/Portfolio/assets/52599741/4bf427c5-d896-4275-b36e-da6ccf02f765)

After I was just thinking to do a port scan, using nmap

![Screenshot 2023-11-25 175644](https://github.com/messor89/Portfolio/assets/52599741/bf53d3c4-8a1b-4dd5-b364-aba962ee302d)

As We can see, we have a lot of open ports, so I was just going with the first one which was FTP port 21 version vsftpd2.4.3

I straight checked for any known vulnerabilities on Exploit+DB (https://www.exploit-db.com), and I have found one:

![Screenshot 2023-11-25 175723](https://github.com/messor89/Portfolio/assets/52599741/4470b082-9b25-429c-8d6a-1eddaa37f4ed)

CVE 2011-2523 : vsftpd 2.3.4 - Backdoor Command Execution (Metasploit)

Straight way back to the Metasploit framework, and was looking for this exploit. 

As We can see, I have found the exploit, so I checked the options, with the "show options" command, and All I needed to do is to set the RHOST.


![Screenshot 2023-11-25 180135](https://github.com/messor89/Portfolio/assets/52599741/2e893dc9-fc11-4f6d-b5a7-bd78435c960c)

After I just run the command "exploit", and We got the connection, and root priveleges.

![Screenshot 2023-11-25 180222](https://github.com/messor89/Portfolio/assets/52599741/16158edf-7f0a-4c00-bb10-7012501640f7)




