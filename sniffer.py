import socket
import struct
import sys
if __name__ == "__main__":
    myIpaddress = "";
    localaddresses = ["192.168.1.1",
                      "192.168.2.2",
                      "192.168.2.1"]
    # print(f"Arguments given: {len(sys.argv)}")
    onlyincoming = False
    onlyoutgoing = False
    onlyunknown = False
    all = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "-i":
            onlyincoming = True
            print("Only capturing incoming packets...")
        elif sys.argv[1] == "-o":
            onlyoutgoing = True
            print("Only capturing outgoing packets...")
        elif sys.argv[1] == "-u":
            onlyunknown = True
            print("Only capturing unknown packets...")
        elif sys.argv[1] == "-a" or not onlyincoming and not onlyoutgoing and not onlyunknown:
            all = True
    else:
        all = True

    onlyudp = False
    onlytcp = False
    onlyicmp = False
    alllayers = False
    if len(sys.argv) > 2:
        if sys.argv[2] == "-udp" or sys.argv[2] == "-u":
            onlyudp = True
            print("Only capturing UDP packets...")
        elif sys.argv[2] == "-tcp" or sys.argv[2] == "-t":
            onlytcp = True
            print("Only capturing TCP packets...")
        elif sys.argv[2] == "-icmp" or sys.argv[2] == "-i":
            onlyicmp = True
            print("Only capturing ICMP packets...")
        else:
            alllayers = True
    else:
        alllayers = True
    # the public network interface
    HOST = socket.gethostbyname(socket.gethostname())
    # create a raw socket and bind it to the public interface
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

    s.bind((HOST,0))

    # Include IP headers
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # receive all packages
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    

    while(True):
        data=s.recvfrom(65565)
        packet=data[0]
        address= data[1]
        header=struct.unpack('!BBHHHBBHBBBBBBBB', packet[:20])
        addressfrom = str(address[0])
        addressto = str(header[12]) + "." + str(header[13]) + "." + str(header[14]) + "." + str(header[15])
        protocol = "TCP" if header[6] == 6 else "UDP" if header[6] == 17 else "ICMP" if header[5] == 1 else "Unknown";
        incoming = "Incoming packet" if addressto == myIpaddress else "Outgoing packet" if addressfrom == myIpaddress else "Unknown";
        if addressto == addressfrom:
            incoming = "Self sent packet"
        printstatement = "Protocol " + protocol + " - " + incoming + " - From address: " + addressfrom + " - To address: " + addressto;
        if (onlyincoming == True and incoming == "Incoming packet" or onlyoutgoing == True and incoming == "Outgoing packet" or all):
            if alllayers == True or protocol == "UDP" and onlyudp or protocol == "TCP" and onlytcp or protocol == "ICMP" and onlyicmp:
                print(printstatement);