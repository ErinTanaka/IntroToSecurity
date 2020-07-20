To Run Program:
	Start virtual environment with command: source my_project/bin/activate

	Generate QR code with command: Python3 programmingAssignment2.py --generate-qr

	Get OTP codes with command: Python3 programmingAssignment2.py --get-otp

Notes:
	--get-otp code is written to run infinitely, displaying the  new code as the getOTP
 	function produces one that is different from the code already printed to the screen

	My get otp changes about 5 seconds sooner than the google authenticator app's codes
	change so, if the program is started within the 5 seconds that they are different it
	syncs up as soon as the next google authenticator code is produced in the app.

Code Explanation:
	I used python to complete this assignment since I knew that it had libraries for
	crypto functions and for generating QR codes.

 	My totp code is based off of the pseudocode for the google authenticator found on
	Wikipedia:

	function GoogleAuthenticatorCode(string secret)
      message := floor(current Unix time / 30)
      hash := HMAC-SHA1(secret, message)
      offset := last nibble of hash
      truncatedHash := hash[offset..offset+3]  //4 bytes starting at the offset
      Set the first bit of truncatedHash to zero  //remove the most significant bit
      code := truncatedHash mod 1000000
      pad code with 0 from the left until length of code is 6
      return code

	(https://en.wikipedia.org/wiki/Google_Authenticator)

	I used a not so secret string that is hard coded but can easily be changed for
	testing purposes. At turn in the secret is "ITSECRET" (line 56)
