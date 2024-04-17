import os


class BinaryConversor:

    def __init__(self, integer_len=4, float_len=4, signal=True):
        self.integer_len = integer_len
        self.float_len = float_len

    def float_part(self, num):
        rest = num
        bitmap=[]
        for i in range(1, self.float_len + 1):
            count = 2 ** -i
            if (count <= rest):
                rest -= count
                bitmap.append(1)
            else:
                bitmap.append(0)
        return bitmap
    
    def int_part(self, num):
        rest = abs(num)
        bitmap=[]
        for i in range(self.integer_len, -1, -1):
            count = 2 ** i
            if (count <= rest):
                rest -= count
                bitmap.append(1)
            else:
                bitmap.append(0)
        return bitmap
    
    def getSignal(self, num):
        if num >= 0:
            return 0
        else:
            return 1
        
    def convertBinary(self, num):
        index = num.find(",")
        if index != -1:
            i = num[:index]
            j = "0." + num[index+1:]

            num = int(i)
            dec = float(j)

            bitmap = f"{self.getSignal(num)} | {self.int_part(num)} | {self.float_part(dec)}"
            return bitmap
        else:
            return False

    
x = BinaryConversor(integer_len=7, float_len=7)
os.system("cls")
print("\tCONVERSOR BINÁRIO\n")
num = input("Digite o numero que deseja representar em binário no formato [sinal] | [parte inteira] | [parte decimal]: ")
print(x.convertBinary(num))