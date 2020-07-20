def googleAuthCode(string secret):
   key = base32decode(secret)
   message=floor(current unix time /30)
   hash = HMAC-SHA1(key, message)
   offset = last nibble of hash
   truncatedHash = hash[offestt..offset+3] #4 bytes starting at offset

