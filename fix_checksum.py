import sys

#check if file path is given.
if len(sys.argv) < 2:
    print("First argument should be a Pokemon generation 1 save file!")
    
else:
    #instantiate "path" object for file path
    path = sys.argv[1]
    
    #open the save file as "file" in binary mode
    file = open(path, "rb+")

    #make a ram object of type "bytearray" to contain all save file binaries
    ram = bytearray(file.read())
    
    #instantiate a new checksum object with the value of 0(=0x00 in hex)
    checksum = 0x00

    #add up every number in ram f rom adress 0x2598 to 0x3522 from checksum
    for x in ram[0x2598:0x3523]:
        checksum += x
    
    #"mask" the inverse checksum object to only contain an 8-bit value (ex: 1010 0101 0101 => 0101 0101)
    checksum = ~checksum
    checksum = checksum&0xff

    #write new generated checksum to ram object
    ram[0x3523] = checksum

    #write new generated ram bytearray to original save file
    file.seek(0,0)
    file.write(ram)

    #notify user the script finished updating the save file
    print("Save file updated!\nWrote new checksum(" + str(hex(checksum)) + ") to " + str(hex(0x3523)) + " in the save file!")
    
    