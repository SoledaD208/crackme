# playing with crackme level VERY EASY - NOOB: http://crackmes.de/users/lafarge/lafarges_crackme_2
# Algorimth: xor, reverse 4 times, add with smt
# then div 0xa to the end
# note1: in Ollydbg, everything is hex (not as when write assembly). EX:
# in assembly: add eax, 30 # means eax = eax + 30 (not eax + 30h)
# but in Ollydbg: add eax, 30 # means eax = eax + 30h
# note2: big endian and little endian very confused, always need to pay attention!!

############## cheers for first blood!!!! ###############
############## soledad ##############
usr_str = b"d53781636dd3b2a71c08d4a7b\x00"
pat1 = [0xAA, 0x89, 0xC4, 0xFE, 0x46]
pat2 = [0x78, 0xF0, 0xD0, 0x03, 0xE7]
pat3 = [0xF7, 0xFD, 0xF4, 0xE7, 0xB9]
pat4 = [0xB5, 0x1B, 0xC9, 0x50, 0x73]

re1 = []
re2 = []
re3 = []
re4 = []
re5 = []


def xor_processor(arr1, arr2):
    dest = []
    len_usr = len(arr1)
    len_pat1 = len(arr2)    
    if len_pat1 < len_usr - 1:
        ins = len_usr - len_pat1
        for i in range(1, ins):
            arr2.append(arr1[i])
        
    # print pat1! just 4 testing
    #for i in pat1:
    #    print hex(ord(i))
    dest.append(arr1[0])
    for i in range(0, len_usr-1):
        dest.append(arr1[i+1] ^ arr2[i])   
    return dest

def reverse_arr(arr):
    tmp_arr = []
    tmp_arr.append(arr[0])
    for i in range(0, len(arr) - 1):
        tmp_arr.append(arr[len(arr) - i - 1])
    return tmp_arr
    
def print_hexarr(hexarr):
    for i in hexarr:
        print hex(i),
    print "\n"

usr = []
for i in usr_str:
    usr.append(ord(i))
                    
re1 = xor_processor(usr, pat1)
#print_hexarr(re1)

tmp = reverse_arr(re1)
#print_hexarr(tmp)
re2 = xor_processor(tmp, pat2)
#print_hexarr(re2)

tmp = reverse_arr(re2)
re3 = xor_processor(tmp, pat3)
#print_hexarr(re3)

tmp = reverse_arr(re3)
re4 = xor_processor(tmp, pat4)
re4 = reverse_arr(re4)
print_hexarr(re4)

re5.append(0x00)
re5.append(0x00)
re5.append(0x00)
re5.append(0x00)

for i in range(0, len(re4) - 1):
    tmp =i % 4
    re5[tmp] += re4[i+1]
    re5[tmp] = (re5[tmp] & 0xff)

#re5 = reversed(re5)
#print_hexarr(re5)
a = 0x00
for i in range(0, len(re5)):
    tmp = 16**(i*2)
    #print hex(re5[i]*tmp)
    a += re5[i]*tmp   
print hex(a)

final = []
div = 0xa
remain = 0x0
while a != 0:
    remain = a % div
    final.append(((remain & 0xf) + 0x30) & 0xf)
    a = a / div

final = reversed(final)
result = ''.join(str(x) for x in final)
print result
