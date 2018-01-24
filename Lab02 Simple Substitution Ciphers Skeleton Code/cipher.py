alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Cipher(object):
    
    def __init__(self, codestring):
        code = {b:a for (a,b) in zip(codestring, alphabet)}
        inverse = {b:a for (a,b) in zip(alphabet, codestring)}
        self.code = code
        self.inverse = inverse
                
    def encode(self, plaintext):
        result = []
        for i in plaintext.upper():
            if i in self.code:
                result.append(self.code[i])
            elif i == " ":
                result.append("-")
            else:
                result.append(i)
        return ("".join(result))       

    def decode(self, ciphertext):
        result = []
        for i in ciphertext.upper():
            if i in self.inverse:
                result.append(self.inverse[i])
            elif i == "-":
                result.append(" ")
            else:
                result.append(i)
        return ("".join(result))


c = Cipher("BCDEFGHIJKLMNOPQRSTUVWXYZA")
c.decode("CDE")
c.decode("ZZZAB")
c.decode("ABC")

c = Cipher("JMBCYEKLFDGUVWHINXRTOSPZQA")
c.decode("JMB,-CY::")
c.decode("---APS#$!")
c.decode("1234567...")

c = Cipher("JMBCYEKLFDGUVWHINXRTOSPZQA")
c.decode("jMb,-cy::")
c.decode("---Aps#$!")

c = Cipher("BCDEFGHIJKLMNOPQRSTUVWXYZA")
c.encode("DEF")
c.encode("ABC")

c = Cipher("JMBCYEKLFDGUVWHINXRTOSPZQA")
c.encode("ABC, DE::")
c.encode("   ZWV#$!")
c.encode("1234567...")

c = Cipher("JMBCYEKLFDGUVWHINXRTOSPZQA")
c.encode("Abc, De::")
c.encode("   zwv#$!")
c.encode("   APS#$!")

c = Cipher("JMBCYEKLFDGUVWHINXRTOSPZQA")
c.encode("Ab3c, De1::6")
c.decode("--Ap4s#$!")
