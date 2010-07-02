alephbet = ''.join([unichr(letter) for letter in range(0x5d0, 0x5eb)])
open('../data/alephbet.txt','w').write(alephbet.encode('utf-16'))