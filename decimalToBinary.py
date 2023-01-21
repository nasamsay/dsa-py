from stack import Stack

def convert_int_to_bin(dec_num):
    s = Stack()
    bin_num = ""
    while dec_num > 0:
        s.push(dec_num % 2)
        dec_num = dec_num//2   
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num

print(convert_int_to_bin(121))