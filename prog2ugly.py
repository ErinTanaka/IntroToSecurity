import sys
import qrcode
import hashlib
import time
import base64
import struct
import binascii
import hmac

debug = 0

def fuckotp(key, time):
    print("okay lets do this \nkey: ", key, "\ntime: ", time)

    actualKey = base64.b32decode(key.encode('ascii')) #convert key to bytes and decode to base 32
    print("Key: ", actualKey)

    # time2 = bytes([time]) first attempt from stack overflow
    # print(time2)

    timeinbytes = struct.pack('>q', time) #2nd method from stack overflow
    print("time in bytes: ", timeinbytes)

    hObject = hmac.new(actualKey, timeinbytes, hashlib.sha1)
    myhmac = hObject.digest()

    print(myhmac)

    print("now for moving shit around")
    # get last nibble of mac
    offset = myhmac[-1] & 0x0F
    print("Offset: ", offset, type(offset))
    truncatedHash = myhmac[offset:offset+4]
    print("truncatedHash: ", truncatedHash)

    decTruncatedHash = struct.unpack('>L', truncatedHash)[0] # take bytes and 'convert' to dec
    print("truncatedHash as dec: ", decTruncatedHash, type(decTruncatedHash))

    codeINT = decTruncatedHash % 1000000
    print(codeINT)
    codeSTR = str(codeINT)
    if len(codeSTR) != 6:
        print("padding with zeroes")
        while(len(codeSTR) != 6):
            codeSTR = '0' + codeSTR
    else:
        print("length is 6!")
    print("padded code: ", codeSTR)

def fuckQRCode(key):
    print("in the shit")
    str = "otpauth://totp/cs370prog2qrcode@google.com?secret="+key+"&issuer=TanakaErinProg2"
    print(str)
    myQR = qrcode.make(str)
    myQR.save("qrcode.png")

def main():
    currentTime = int(time.time()) // 30
    myKey = "SECRETZZ"

    cmd = sys.argv[1]
    if cmd == "--generate-qr":
        print("generating qr code")
        fuckQRCode(myKey)

    if cmd == "--get-otp":
        print("getting otp")
        while(1==1):
            currentTime = int(time.time()) // 30
            fuckotp(myKey, currentTime)
            for i in range(1,31):
                print(i)
                time.sleep(1)
main()
