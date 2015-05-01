from Crypto.Cipher import DES

      

def decrypt():

    data = open("data.dex", "rb").read()

    key = "XPA087T24433PASS"[:8]

    data = DES.new(key, DES.MODE_ECB).decrypt(data)

    f = open("data.txt", "wb")

    f.write(data)

    f.close()

 

if __name__ == "__main__":

    decrypt()