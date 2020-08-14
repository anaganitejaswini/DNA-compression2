import numpy

x=open("test.fa")
inp = x.read().strip()
x.close()
inp=inp+"!"
inp_len = len(inp)
print(inp)
# Calculating frequency
freq = {}
for c in inp:
    if c in freq:
        freq[c] += 1/inp_len
    else:
        freq[c] = 1/inp_len
 
#freq ={key: freq[key] for key in sorted(freq.keys())}
#print(inp_len)
print(freq)

#assigning ranges to the alphabet
ranges={}
low=0
high = 1
for i in freq.items():
	alp=0
	bet=0
	alp=low
	bet=low+i[1]
	low=bet
	ranges[i[0]]=[alp,bet]
print(ranges)

ranges2=ranges.copy()

def encode(input_string,dicti):
	for j in input_string:
		lo = 0
		hi = 1
		lo = lo[
		
		

encoded=encode(inp)
