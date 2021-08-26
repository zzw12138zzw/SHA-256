import ctypes


verbose = False

dict = {"A" : 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35}

ini = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,

				   0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,

				   0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,

				   0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,

				   0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,

				   0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,

				   0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,

				   0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def get_num_value(thing):
	if is_int(thing):
		return int(thing)
	else:
		return dict[thing.upper()]


def round(times, plain_text):
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    for ii in range(0, len(plain_text)):
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7
        test_input = split_equally(plain_text[ii], 32)


        #test_input[0] = "10000000000000000000000000000000"
        #print("_+_+_+" + len(test_input))

        for jj in range(16, 64):
            s0 = xor(xor(right_rotate(test_input[jj - 15], 7), right_rotate(test_input[jj - 15], 18)), right_shift(test_input[jj - 15], 3))

            s1 = xor(xor(right_rotate(test_input[jj - 2], 17), right_rotate(test_input[jj - 2], 19)), right_shift(test_input[jj - 2], 10))

            test_input.append(addd(addd(addd(test_input[jj - 16], s0), test_input[jj - 7]), s1))

        #print("_+_+_+" + len(test_input))
        for ll in range(0, times):
            s0 = (integer_right_rotate(a, 2)^integer_right_rotate(a, 13)^integer_right_rotate(a, 22))
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = s0 + maj
            s1 = (integer_right_rotate(e, 6)^integer_right_rotate(e, 11)^integer_right_rotate(e, 25))
            ch = (e & f)^((e ^ 0xffffffff) & g)
            if verbose:
                print("s0: " + integer_to_hex_string(s0))
                print("maj: " + integer_to_hex_string(maj))
                print("s1: " + integer_to_hex_string(s1))
                print("ch: " + integer_to_hex_string(ch))
                input()
            t1s = (h& 0x00000000ffffffff)  + (s1 & 0x00000000ffffffff) + (ch & 0x00000000ffffffff) + (ini[ll] & 0x00000000ffffffff)
            t1s = t1s & 0x00000000ffffffff
            bint1s = "{0:b}".format(t1s)
            if len(bint1s) < 32:
                r = 32 - len(bint1s)
                for kk in range(0, r):
                    bint1s = "0" + bint1s
#            elif (len(bint1s) > 32):
 #               t1s = t1s & 0xffffffff
  #              bint1s = "{0:b}".format(t1s)
                
            t1 = addd(bint1s, test_input[ll])

            t1t = hexfy(t1);
            x = t1t[2]
            t = get_num_value(x)

            t1i = 0
            if t > 7:
                t1 = hexfy(subb(t1, "01111111111111111111111111111111"))
                t1i = int(t1, 16)
                t1i = t1i - 1 + 0x80000000
                t1i = t1i & 0x00000000ffffffff
                
            else:
                t1 = hexfy(t1)
                t1i = int(t1, 16)

            h = g
            g = f
            f = e
            e = d + t1i
            d = c
            c = b
            b = a
            a = t1i + t2
            e = e & 0x00000000ffffffff
            a = a & 0x00000000ffffffff

            
        #print(integer_to_hex_string(h4))
        h0 = h0 + a
        h1 = h1 + b
        h2 = h2 + c
        h3 = h3 + d
        h4 = h4 + e
        h5 = h5 + f
        h6 = h6 + g
        h7 = h7 + h
        h0 = h0 & 0x00000000ffffffff
        h1 = h1 & 0x00000000ffffffff
        h2 = h2 & 0x00000000ffffffff
        h3 = h3 & 0x00000000ffffffff
        h4 = h4 & 0x00000000ffffffff
        h5 = h5 & 0x00000000ffffffff
        h6 = h6 & 0x00000000ffffffff
        h7 = h7 & 0x00000000ffffffff
        

    print("\nHere is your result: ")
    hh0 = integer_to_hex_string(h0)
    hh1 = integer_to_hex_string(h1)
    hh2 = integer_to_hex_string(h2)
    hh3 = integer_to_hex_string(h3)
    hh4 = integer_to_hex_string(h4)
    hh5 = integer_to_hex_string(h5)
    hh6 = integer_to_hex_string(h6)
    hh7 = integer_to_hex_string(h7)
    if len(integer_to_hex_string(h0)) < 8:
        for nn in range(0,8-len(integer_to_hex_string(h0)),1):
            hh0 = "0"+integer_to_hex_string(h0)
    if len(integer_to_hex_string(h1)) < 8:
        for nn in range(0,8-len(integer_to_hex_string(h1)),1):
            hh1 = "0"+integer_to_hex_string(h1)
    if len(integer_to_hex_string(h2)) < 8:
        for nn in range(0,8-len(integer_to_hex_string(h2)),1):
            hh2 = "0"+integer_to_hex_string(h2)
    if len(integer_to_hex_string(h3)) < 8:
        for nn in range(0,8-len(integer_to_hex_string(h3)),1):
            hh3 = "0"+integer_to_hex_string(h3)
    if len(integer_to_hex_string(h4)) < 8:
        for nn in range(0,8-len(integer_to_hex_string(h4)),1):
            hh4 = "0"+integer_to_hex_string(h4)
    if len(integer_to_hex_string(h5)) < 8:
        for nn in range(0,8-len(integer_to_hex_string(h5)),1):
            hh5 = "0"+integer_to_hex_string(h5)
    if len(integer_to_hex_string(h6)) < 8:
        for nn in range(0,8-len(integer_to_hex_string(h6)),1):
            hh6 = "0"+integer_to_hex_string(h6)
    if len(integer_to_hex_string(h7)) < 8:
        for nn in range(0,8-len(integer_to_hex_string(h7)),1):
            hh7 = "0"+integer_to_hex_string(h7)
    
    print(hh0 + hh1 + hh2 + hh3 + hh4 + hh5 + hh6 + hh7)
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

def hexfy(vv):
    ww = "0x"
    for ii in range(0, len(vv), 4):
        if vv[ii:ii+4] == "0000":
            ww += "0"
        elif vv[ii:ii+4] == "0001":
            ww += "1"
        elif vv[ii:ii+4] == "0010":
            ww += "2"
        elif vv[ii:ii+4] == "0011":
            ww += "3"
        elif vv[ii:ii+4] == "0100":
            ww += "4"
        elif vv[ii:ii+4] == "0101":
            ww += "5"
        elif vv[ii:ii+4] == "0110":
            ww += "6"
        elif vv[ii:ii+4] == "0111":
            ww += "7"
        elif vv[ii:ii+4] == "1000":
            ww += "8"
        elif vv[ii:ii+4] == "1001":
            ww += "9"
        elif vv[ii:ii+4] == "1010":
            ww += "A"
        elif vv[ii:ii+4] == "1011":
            ww += "B"
        elif vv[ii:ii+4] == "1100":
            ww += "C"
        elif vv[ii:ii+4] == "1101":
            ww += "D"
        elif vv[ii:ii+4] == "1110":
            ww += "E"
        elif vv[ii:ii+4] == "1111":
            ww += "F"
    return ww

def subb(a, b):
    qq = ""
    bor = 0
    v = 0
    for ii in range(len(a) - 1, -1, -1):
        v += 1
        #print("++++++" + a[ii])
        #print("------" + )
        if a[ii] == b[ii]:
            if bor == 0:
                qq += "0"
                bor = 0
            else:
                qq += "1"
                bor = 1
        elif a[ii] == "0":
            if bor == 0:
                qq += "1"
                bor = 1
            else:
                qq += "0"
                bor = 1
        else:
            if bor == 0:
                qq += "1"
                bor = 0
            else:
                qq += "0"
                bor = 0
    return qq[::-1]

def addd(a, b):
    xx = ""
    carry = 0
    for ii in range(len(a) - 1, -1, -1):
        #print("++++++" + a[ii])
        #print("------" + b[ii])
        if a[ii] != b[ii]:
            if carry == 0:
                xx += "1"
                carry = 0
            else:
                xx += "0"
                carry = 1
        elif a[ii] == "0":
            if carry == 0:
                xx += "0"
                carry = 0
            else:
                xx += "1"
                carry = 0
        else:
            if carry == 0:
                xx += "0"
                carry = 1
            else:
                xx += "1"
                carry = 1
    return ''.join(reversed(xx))


def right_shift(uu, d):
    yy = ""
    for ii in range(0, d):
        yy += "0"
    right = uu[0:(len(uu) - d)]
    yy += right
    return yy

def right_rotate(pp, d):
    left = pp[(len(pp) - d):]
    right = pp[0:len(pp) - d]
    return left + right

def xor(a, b):
    zz = ""
    for ii  in range(0, len(a)):
        if a[ii] != b[ii]:
            zz += "1"
        else:
            zz += "0"
    return zz

def split_equally(text, size):
    ret = []
    for ii in range(0, len(text), size):
        ret.append(text[ii:min(len(text), ii + size)])
    return ret

def padding(tt):
    length = len(tt)
    tt += "1"
    rem = (length + 1) % 512

    if rem < 448:
        for ii in range(0, 448 - rem):
            tt += "0"
    binLen = "{0:b}".format(length)
    pad = 64 - len(binLen)
    for ii in range(0, pad):
        tt += "0"
    tt += binLen
    print("Your binary text after padding: ")
    ii = 0
    while True:
        if(ii >= len(tt)):
            break
        for ll in range(0, 4):
            for jj in range(0, 8):
                print(tt[ii + jj], end = "")
            ii = ii + 8
            print(" ", end = "")
        print(" ")
    print("¡ü¡ü¡ü¡ü¡ü¡ü¡ü¡ü Your Binary Texts ¡ü¡ü¡ü¡ü¡ü¡ü¡ü¡ü\n")
    return tt

def to_bin(rr):
    bt = bytes(rr, 'utf-8')
    binary = ""
    output_binary = ""
    for b in bt:
        val = b
        for i in range(0, 8):
            if (val & 128) == 0:
                binary += "0"
                output_binary += "0"
            else:
                binary += "1"
                output_binary += "1"
            val = val << 1
        output_binary += " "
    print("Your plaintext in binary: ")
    print("" + output_binary)
    return binary

def integer_right_rotate(n, d):
    return (n >> d)| (n << (32 - d)) & 0xFFFFFFFF

def integer_to_hex_string(n):
    return '{:x}'.format(int(n))

print("Please use enter in this program for NextStep: ")
print("Please enter the plaintext: ")
user_input = input()
print("\nNow!\nConvert string into binary using ACSII")
input()
not_bin = to_bin(user_input)
print("\nNext!\nPad your binary string to the right length")
input()
not_bin = padding(not_bin)
plain_text = split_equally(not_bin, 512)
print("\nSHA-256 use 64 rounds of encryption")
print("Note that every time you enter a number of rounds, SHA-256 restarts from round 1")
while True:
    print("\nPlease enter an int number for the number of rounds: ")
    times = input()

    if times == "quit" or times == "q" or times == "exit" or times == "shutdown" or times == "shut down":
        print("Thanks!")
        break;

    if isinstance(times, int):
        print("That was not an int number")
        print("Can't trick me with that lmao")
        continue;

    print("\nVerbose shows the result of maj, s0, s1 and ch calculation result for each round")
    print("Verbose or not?(y or n)")

    ver = input()
    if ver == "y" or ver == "yes":
        verbose = True
    else:
        verbose = False
    round(int(times), plain_text)
