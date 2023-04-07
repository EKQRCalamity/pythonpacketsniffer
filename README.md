<div align="center">

# Simple Pythong Packet Sniffer
A simple python sniffer with command line arguments to filter output. Currently detects UDP, TCP and ICMP packets.
Please change the variable myIpaddress on line 5 to your PCs IP address on the network.
##### Command line arguments are expected to be used in following order: [incoming/outgoing] [protocol]
## Incoming Arguments
-i for incoming<br>
-o for outgoing<br>
-u for unknown<br>
anything else will be regarded as all

## Protocol Arguments
-icmp / -i for ICMP packets<br>
-tcp  / -t for TCP packets<br>
-udp  / -u for UDP packets<br>
</div>
