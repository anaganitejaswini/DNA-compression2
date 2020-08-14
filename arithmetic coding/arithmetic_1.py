import sys
import random
import string

import decimal
from decimal import Decimal

decimal.getcontext().prec=10000

with open('test.fa') as fin, open('bacillus2.fa', 'w') as fout:
	for line in fin:
		if not line.startswith('>'):
			line = line.replace("\n","")
			fout.write(line)
		else:
			fout.write("\n")
            #fout.write(next(fin))
x=open('bacillus2.fa')
string = x.read()
print(len(string))

def encode(encode_str, N):
    count = dict.fromkeys(("A","G","C","T","N","\n"), 1)                                    # probability table
    print("count",count)
    cdf_range = dict.fromkeys(("A","G","C","T","N","\n"), 0)
    pdf = dict.fromkeys(("A","G","C","T","N","\n"), 0)

    low = 0
    high = Decimal(1)/Decimal(6)

    for key, value in sorted(cdf_range.items()):
        cdf_range[key] = [low, high]
        low = high
        high += Decimal(1)/Decimal(6)

    for key, value in sorted(pdf.items()):
        pdf[key] = Decimal(1)/Decimal(6)
	
	
    #for key, value in sorted(cdf_range.items()):
     #  print(key, value)

    # for key, value in sorted(pdf.iteritems()):
    #   print key, value

    i = 6

    lower_bound = 0                                                                     # upper bound
    upper_bound = 1                                                                     # lower bound

    u = 0

    # go thru every symbol in the string
    for sym in encode_str:
        i += 1
        u += 1
        count[sym] += 1

        curr_range = upper_bound - lower_bound                                          # current range
        upper_bound = lower_bound + (curr_range * cdf_range[sym][1])                    # upper_bound
        lower_bound = lower_bound + (curr_range * cdf_range[sym][0])                    # lower bound

        # update cdf_range after N symbols have been read
        if (u == N):
            u = 0

            for key, value in sorted(pdf.items()):
                pdf[key] = Decimal(count[key])/Decimal(i)

            low = 0
            for key, value in sorted(cdf_range.items()):
                high = pdf[key] + low
                cdf_range[key] = [low, high]
                low = high
    print(lower_bound)
    return lower_bound

def decode(encoded, strlen, every):
    decoded_str = ""

    count = dict.fromkeys(("A","G","C","T","N","\n"), 1)                                        # probability table
    cdf_range = dict.fromkeys(("A","G","C","T","N","\n"), 0)
    pdf = dict.fromkeys(("A","G","C","T","N","\n"), 0)

    low = 0
    high = Decimal(1)/Decimal(6)

    for key, value in sorted(cdf_range.items()):
        cdf_range[key] = [low, high]
        low = high
        high += Decimal(1)/Decimal(6)

    for key, value in sorted(pdf.items()):
        pdf[key] = Decimal(1)/Decimal(6)


    lower_bound = 0                                                                     # upper bound
    upper_bound = 1                                                                     # lower bound

    k = 0

    while (strlen != len(decoded_str)):
        for key, value in sorted(pdf.items()):

            curr_range = upper_bound - lower_bound                                      # current range
            upper_cand = lower_bound + (curr_range * cdf_range[key][1])                 # upper_bound
            lower_cand = lower_bound + (curr_range * cdf_range[key][0])                 # lower bound

            if (lower_cand <= encoded < upper_cand):
                k += 1
                decoded_str += key

                if (strlen == len(decoded_str)):
                    break

                upper_bound = upper_cand
                lower_bound = lower_cand

                count[key] += 1

                if (k == every):
                    k = 0
                    for key, value in sorted(pdf.items()):
                        pdf[key] = Decimal(count[key])/Decimal(6+len(decoded_str))

                    low = 0
                    for key, value in sorted(cdf_range.items()):
                        high = pdf[key] + low
                        cdf_range[key] = [low, high]
                        low = high
    print(decoded_str)
    return decoded_str

def main():
    #count = 10
    encode_str = "AGCTAA\nAAGTNA\nAGTTT"
    #encode_str=string
    strlen = len(encode_str)
    every = 10000
    encoded = encode(encode_str, every)
    decoded = decode(encoded, strlen, every)
    out=open('bacillus_decoded.fa','w')
    out.write(decoded) 		#calling decode function

if __name__ == '__main__':
    main()
    
