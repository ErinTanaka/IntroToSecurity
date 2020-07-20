import sys
import qrcode
import hashlib
import time
import base64
import struct
import binascii
import hmac

def getOTP(key, time):
    #convert key to bytes and decode to base 32
    actualKey = base64.b32decode(key.encode('ascii'))

    #convert time integer to byte representation
    timeinbytes = struct.pack('>q', time) #2nd method from stack overflow

    #hash key and time with sha 1
    hObject = hmac.new(actualKey, timeinbytes, hashlib.sha1)
    myhmac = hObject.digest()

    # get last nibble to use as offset
    offset = myhmac[-1] & 0x0F
    truncatedHash = myhmac[offset:offset+4]

    #convertbyte representation to decimal int
    decTruncatedHash = struct.unpack('>L', truncatedHash)[0] # take bytes and 'convert' to dec

    #setting first bit to zero
    # print(bin(decTruncatedHash))
    decTruncatedHash &= 0x7FFFFFFF
    # print(bin(decTruncatedHash))

    #mod by 1,000,000
    codeINT = decTruncatedHash % 1000000

    #convert to string for easy paddding
    codeSTR = str(codeINT)
    # print(codeINT)
    # print(codeSTR)
    #Pad with zeroes till length is 6
    if len(codeSTR) != 6:
        while(len(codeSTR) != 6):
            codeSTR = '0' + codeSTR

    return codeSTR

def generateQRCode(key):

    str = "otpauth://totp/cs370prog2qrcode@google.com?secret="+key+"&issuer=TanakaErin"
    myQR = qrcode.make(str)
    myQR.save("./TanakaErinQRcode.jpg")
    print("QR code has been saved into current directory under file name: \n\t TanakaErinQRcode.jpg")

def main():
    currentTime = int(time.time()) // 30
    myKey = "ITSECRET"
    oldOTP= None
    cmd = sys.argv[1]

    if cmd == "--generate-qr":
        print("generating qr code")
        generateQRCode(myKey)

    elif cmd == "--get-otp":
        print("getting otp\n * NOTE: My generator changes about 5-ish seconds faster than the google authenticator app")
        while(1==1):
            currentTime = int(time.time()) // 30
            newOTP = getOTP(myKey, currentTime)
            if (newOTP != oldOTP) :
                print(newOTP[0:3]+' '+newOTP[3:6]+'\n')
                oldOTP = newOTP
    else:
        print("Invalid command line argument")

main()
