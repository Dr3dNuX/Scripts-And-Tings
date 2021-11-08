# a very simple script to convet an ip address to binary
# and convert the mask to binairy as well


# getting the ip address/mask strings from the user
ip_add = input("Enter ip: ")
mask = input("Enter mask ")

#splitting the strings using . delimitor then assigning the
#octets to sepret varables

A,B,C,D = ip_add.split(".")
E,F,G,H = mask.split(".")

#formatting and converting the strings to intagers then using
#Binary conversio to convert the new intergers to binary
print("ip address: {:b}.{:b}.{:b}.{:b}".format(int(A),int(B),int(C),int(D)))
print("Subnet mask: {:b}.{:b}.{:b}.{:b}".format(int(E),int(F),int(G),int(H)))