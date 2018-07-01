
# User enters main network address. NOTE: must be Class C
MainNetwork = input("What is the main network id address?")
# User enters number of subnets they desire.
# NOTE: the script will produce the user's desired number of subnets +  main network address
SubnetsDesired = input("How many subnets do you want to create?")

# Instantiating variables type(list) to store output of functions.
GoodNets = []
Ranges = []
BroadcastAddresses = []

# AvailableNetworks()
# takes SubnetsDesired and finds first number of subnets in NetArray >= SubnetsDesired
# This shows number of subnets that will be created (not included the main network address)
# Grabs the index of NetArray and finds index + 1 in host array.
# This yields number of hosts on each subnet.
# The number of hosts in each network is added to the last 8 bits of the network address before it.
# This produces a network address for each subnet.
# The results are stored in Goodnets for later printing.
def AvailableNetworks():
    NetArray = [2, 4, 8, 16, 32, 64, 128, 256]
    HostArray = [256, 128, 64, 32, 16, 8, 4, 2]
    for i in NetArray:
        if i >= int(SubnetsDesired):
            NumbSubnets = i
            SubnetIndex = NetArray.index(i)
            NumIps=HostArray[SubnetIndex + 1]
            ipaddy = MainNetwork.split(".")
            ipaddy = list(map(int, ipaddy))
            for i in range(NumbSubnets-1):
                ipaddy[-1] += NumIps
                GoodNets.append('.'.join(str(i) for i in ipaddy))
            break

# SubnetRanges()
# Takes SubnetsDesired and finds first number of subnets in NetArray >= SubnetsDesired
# This shows number of subnets that will be created (not including the main network address)
# Grabs the index of NetArray and finds index + 1 in host array.
# This yields number of hosts on each subnet.
# The number of hosts in each network is added to the last 8 bits of the network address before it.
# Then, a range of host ips for each subnet are assembled.
# These host ips do not include the network address and the broadcast address are assembled.
# The results are stored in Goodnets for later printing.
def SubnetRanges():
    NetArray = [2, 4, 8, 16, 32, 64, 128, 256]
    HostArray = [256, 128, 64, 32, 16, 8, 4, 2]
    ipaddy = MainNetwork.split(".")
    ipaddy = list(map(int, ipaddy))
    for i in NetArray:
        if i >= int(SubnetsDesired):
            NumbSubnets = i
            SubnetIndex = NetArray.index(i)
            NumIps = HostArray[SubnetIndex + 1]
            for i in range(NumbSubnets -1):
                Range = "." + str(ipaddy[-1] + 1) + "-" + "." + str(ipaddy[-1] + NumIps - 2)
                Ranges.append(Range)
                ipaddy[-1] += NumIps
            break

# BroadcastAddy()
# Takes SubnetsDesired and finds first number of subnets in NetArray >= SubnetsDesired
# This shows number of subnets that will be created (not included the main network address)
# Grabs the index of NetArray and finds index +1 in host array.
# This yields number of hosts on each subnet.
# The number of hosts in each network - 1 is added to the last 8 bits of the network address before it.
# This produces a list of the broadcast addresses for each subnet.
# The results are stored in BroadcastAddresses for later printing.
def BroadcastAddy():
    NetArray = [2, 4, 8, 16, 32, 64, 128, 256]
    HostArray = [256, 128, 64, 32, 16, 8, 4, 2]
    for i in NetArray:
        if i >= int(SubnetsDesired):
            NumbSubnets = i
            SubnetIndex = NetArray.index(i)
            NumIps = HostArray[SubnetIndex + 1]
            ipaddy = MainNetwork.split(".")
            ipaddy = list(map(int, ipaddy))
            for i in range(NumbSubnets - 1):
                ipaddy[-1] += NumIps -1
                BroadcastAddresses.append('.'.join(str(i) for i in ipaddy))
                ipaddy[-1] += 1
            break

# Cider()
# Takes SubnetsDesired and finds first number of subnets in NetArray >= SubnetsDesired
# The index of NetArray that is returned represents the number of bits
# that will be 1 in last byte of subnet mask.
# The function then grabs the equivalent index in ciderlist and prints results.
def Cider():
    NetArray = [2, 4, 8, 16, 32, 64, 128, 256]
    ciderlist = ["/25", "/26", "/27", "/28", "/29", "/30", "/31", "/32"]
    for i in NetArray:
        if i >= int(SubnetsDesired):
            CiderIndex = NetArray.index(i)
            print("CIDR Notation:", ciderlist[CiderIndex])
            break

# SubNetMask()
# Takes SubnetsDesired and finds first number of subnets in NetArray >= SubnetsDesired
# The index of NetArray that is returned represents the number of bits
# that will be 1 in last byte of subnet mask.
# The function then grabs the equivalent index in MaskValues and saves as BitValue
# The bit value is concatenated to the end of "255.255.255" to produce subnet mask.
def SubNetMask():
    NetArray = [2, 4, 8, 16, 32, 64, 128, 256]
    MaskValues = [128, 64, 32, 16, 8, 4, 2, 1]
    BitValue = 0
    MaskIndex = 0
    for i in NetArray:
        if i >= int(SubnetsDesired):
            MaskIndex = NetArray.index(i)
            break
    for i in range(MaskIndex):
        BitValue += MaskValues[i]
    print("Subnet Mask:", '255.255.255.' + str(BitValue))

if __name__== '__main__':
    AvailableNetworks()
    SubnetRanges()
    BroadcastAddy()


# Instantiated lists are combined into matched triplets by zip()
    FinalReport = zip(GoodNets, Ranges, BroadcastAddresses)

# zip() creates immutable tuples that will give you hell if you try to run them through .format()
# So convert FinalReport is converted back into list of lists
    FinalReport = [list(elem) for elem in FinalReport]

# Formatted, when combined with .format() will create 3 columns.
    formatted = "{:<30}{:<30}{:<30}"

# Print the column headers.
    print(formatted.format("Network ID", "Range", "Broadcast Address"))

# Print the results of AvailableNetworks() SubnetRanges() and BroadcastAddy() by iterating
# through FinalReport
    for list in FinalReport:
        print(formatted.format(list[0], list[1], list[2]))

# Execute cider() and SubNetMask to produce cider notation and subnet mask in final output.
    print()
    Cider()
    print()
    SubNetMask()