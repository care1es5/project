# Spoof Proof - 60

```
The police have retrieved a network trace of some suspicious activity. Most of the traffic is users viewing their own profiles on a social networking website, but one of the users on the network downloaded a file from the Thyrin Labs VPN and spoofed their IP address in order to hide their identity. Can you figure out the last name of person that accessed the Thyrin files, and the two source IP addresses they used?
[Example valid flag format: "davis,192.168.50.6,192.168.50.7"]

PCAP file available here. You can also view it on CloudShark
```

Wireshark or Cloudshark either one is fine but I used Cloudshark because I was so lazy.

Challenge sugessts Attacker "spoofed" the IP addresses.

Open up the pcap in either one of theses and filter arp (Address Resolution Protocol). 

You will find mac address of 08:00:27:2b:f7:02 with Who has 192.168.50.10 and two ip address: 192.168.59.3, 192.168.50.4

In order to find the name of an attacker, we have to filter the packet with ip address 192.168.150.3.

```
ip.addr=="192.168.50.3"
```

The name of the attacker is John Johnson.

```
Flag:Johnson,192.168.50.4,192.168.50.3
```

