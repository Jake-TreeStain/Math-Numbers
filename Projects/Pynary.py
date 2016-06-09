#Binary to number converter

def Convert(bin_num, to_ascii=False):
    if to_ascii == False:
        bin_num = bin_num[::-1]
        sequence_adder = 1
        num = 0
        for char in bin_num:
            if char == "0":
                pass
            elif char == "1":
                num += sequence_adder
            sequence_adder = sequence_adder * 2
        return num
    else:
        ascii_tmp = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
        out = ""
        ascii_real = [let for let in ascii_tmp]
        for seq in bin_num.split():
            seq_int = Convert(seq)
            out += ascii_real[seq_int - 32]
        return out
            
            


bin_inp = str(input("Binary sequence: "))
ascii_inp = str(input("To Ascii [t/f]: "))
if ascii_inp == "t":
    print(Convert(bin_inp, True))
else:
    print(Convert(bin_inp))
