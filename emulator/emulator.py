
DRX = bytearray()
TRX = bytearray("GED\x03hG\x15&Ka =;\x0c\x1a31o*5M", "utf-8")



def mov_drx_trx():
    global DRX
    global TRX
    DRX = TRX

def mov_trx_drx():
    global DRX
    global TRX
    TRX = DRX

def mov_drx_string(string):
    global DRX
    string = string.strip('"')
    DRX = bytearray(string, "utf-8")

def mov_trx_string(string):
    global TRX
    string = string.strip('"')
    TRX = bytearray(string, "utf-8")

def reverse_drx():
    global DRX
    DRX = DRX[::-1]

def reverse_trx():
    global TRX
    TRX = TRX[::-1]

def xor_drx_trx():
    global TRX
    global DRX
    for i in range(len(TRX)):
        DRX[i] = DRX[i] ^ TRX[i]

def xor_trx_drx():
    global TRX
    global DRX
    for i in range(len(DRX)):
        TRX[i] = DRX[i] ^ TRX[i]

with open("Crypto.asm") as reader:
    for line in reader.readlines():
        line = line.strip()
        instruction = line.split(" ")[0]
        if "XOR" in instruction:
            xor_destination = line.split(" ")[1]
            xor_source = line.split(" ")[2]
            if "DRX" in xor_source:
                xor_trx_drx()
            if "TRX" in xor_source:
                xor_drx_trx()
        if "REVERSE" in instruction:
            reverse_destination = line.split(" ")[1]
            if "DRX" in reverse_destination:
                reverse_drx()
            if "TRX" in reverse_destination:
                reverse_trx()
        if "MOV" in instruction:
            mov_source = line.split(" ")[2]
            mov_destination = line.split(" ")[1]
            if "DRX" in mov_destination:
                if "TRX" in mov_source:
                    mov_drx_trx()
                else:
                    mov_drx_string(mov_source)
            if "TRX" in mov_destination:
                if "DRX" in mov_source:
                    mov_trx_drx()
                else:
                    mov_trx_string(mov_source)
        
        print("Instruction: "+ line + "  -----  " + "DRX: " + str(DRX) + " TRX: " + str(TRX))