# number conversion
# xyan831

class base_convert:
    """
    class for number conversion
    num10 = input base 10 number
    num2 = base 2 number
    num8 = base 8 number
    num16 = base 16 number
    get_convert = convert base10 to base2/8/16
    reverse_convert = convert base2/8/16 to base10
    """
    def __init__(self, num10):
        self.hexd = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
        self.num10 = num10
        self.num2 = self.get_convert(num10, 2)
        self.num8 = self.get_convert(num10, 8)
        self.num16 = self.get_convert(num10, 16)
    def get_convert(self, num, base):
        convert_list = []
        while num/base != 0:
            convert_list.append(str(num%base))
            num = num // base
        convert_list.reverse()
        for item in self.hexd:
            convert_list = [self.hexd[item] if x==item else x for x in convert_list]
        convert_num = "".join(convert_list)
        return convert_num
    def reverse_convert(self, num, base):
        num_list = [item for item in str(num)]
        num_list.reverse()
        convert_list = []
        for item in self.hexd:
            num_list = [item if x==self.hexd[item] else x for x in num_list]
        count=0
        for i in num_list:
            convert_list.append(int(i)*(base**count))
            count+=1
        convert_num = sum(convert_list)
        return convert_num

if __name__ == "__main__":
    # number conversion example
    num10 = 88
    print(bin(num10), oct(num10), hex(num10))
    f1 = base_convert(num10)
    print(f1.num2, f1.num8, f1.num16)
    # check reverse conversion
    f1_rev2 = f1.reverse_convert(f1.num2, 2)
    f1_rev8 = f1.reverse_convert(f1.num8, 8)
    f1_rev16 = f1.reverse_convert(f1.num16, 16)
    print(f1_rev2, f1_rev8, f1_rev16)

