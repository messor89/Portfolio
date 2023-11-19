This is my first Project, in Cisco Packet Tracer.

This is a projeckt topology for a Bank, which contains a Reception and an Office area, also provides free wifi for Quests. 
<br>The Reception and the Office are separated for two different networks, which can reach each other and also the DNS server with the bank's website. 
Also there is an attacker machine, which broke the weak wpa password of the office wifi and will try to do an ARP spoofing attack. 


![Screenshot 2023-11-19 130851](https://github.com/messor89/Portfolio/assets/52599741/f8cadd02-e4ee-4d04-a375-95164db50f5c)
<br>
<br>
In the next picture, showing, how I configure the routers, that Both Office and Reception side can see each other, and reach the Bank's server, with their website.
![Screenshot 2023-11-19 133855](https://github.com/messor89/Portfolio/assets/52599741/13d90c4f-85d5-42d8-8f0d-3b3cc3e2edb1)
![Screenshot 2023-11-19 133948](https://github.com/messor89/Portfolio/assets/52599741/e0921a12-ea14-4041-bc4f-cf30d57a4156)
![Screenshot 2023-11-19 134230](https://github.com/messor89/Portfolio/assets/52599741/23e3f05c-146b-4d09-88fc-9b0332aeff0b)
![Screenshot 2023-11-19 134308](https://github.com/messor89/Portfolio/assets/52599741/27c5ad35-b6fd-4a01-8b0d-32b05a77b31f)
![Screenshot 2023-11-19 134345](https://github.com/messor89/Portfolio/assets/52599741/686b35f2-4066-4312-8837-a092f8aefcf7)
<br>
<br>
The next step was, The attacker machine do some arp-spoofing, changing their MAC address to the router MAC address.
<br>
So I am gonna change the MAC address of the attacker machine to the MAC address of Router6
0060.5C6D.2A60---0060.3E39.9501, so the attacker will be a Man-in-the-middle, and might catch important informations.
![Screenshot 2023-11-19 135139](https://github.com/messor89/Portfolio/assets/52599741/7ae27a6c-39b9-4cd8-b263-05e8d8a34c4e)
![Screenshot 2023-11-19 140216](https://github.com/messor89/Portfolio/assets/52599741/4c28535a-8016-4467-a319-ca4e13c76b6f)
<br>
<br>
Conclusion: With a SIEM tool like Wireshark, Spunk, QRadar, Microsoft Sentinel etc, you can identify the attacker and can take further action to avoid any attack/event/loss happenes. Forexample use a strong encryption key for your wifi connections, MAC address filtering.
 








