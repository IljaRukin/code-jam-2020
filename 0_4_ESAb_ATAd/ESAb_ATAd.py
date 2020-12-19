import sys

file_in = sys.stdin
file_out = sys.stdout

###debug###
f = open('debug.txt','w')
###########

def get_line(): return file_in.readline()
def get_int(): return int(get_line())
def get_ints(): return [int(x) for x in get_line().split()]

def reverse(result): return [result[j] for j in reversed(range(len(result)))]
def complement(result): return [(1 if x==0 else (0 if x==1 else None)) for x in result]

cases,size = get_ints()
case = 0

#array of positions for traversal
positions = []
for l in range(size//2):
    positions.append(l)
    positions.append(size-l-1)

for k in range(cases): #loop over cases

	result = [None]*size #empty list

	n_query = 0
	pos = 0
	mode = False #start in collect mode
	while (None in result) or (mode==True):
		if n_query == 10 :
			n_query = 0
			mode = True

		if mode == False: #collect new values
			p = positions[pos]
			pos += 1
			print(p+1, flush=True); n_query+=1;
			result[p] = get_int()
			###debug###
			f.write('collect: '+str(result[p])+' at: '+str(p+1)+'\n')
			###########

		if mode == True: #determine transformation
		#note: only known values have to be transformed !
			mode = False

			trafo_pos = 0
			rev = None #0...1 detect reverse
			compl = None #1...1 detect complement
			while (trafo_pos<size) and ((rev==None) or (compl==None)):
				if result[positions[trafo_pos+1]]==None :
					#no known values left
					break
				if result[positions[trafo_pos]] == result[positions[trafo_pos+1]]:
					compl = trafo_pos
				else:
					rev = trafo_pos
				trafo_pos += 2

			if (rev == None or compl == None) and (pos%2==0):
				#retry collecting last value, if transform can't be determined completly
				pos -=1

			#test for complement
			if (compl!=None):
				p = positions[compl]
				print(p+1, flush=True); n_query+=1;
				q = get_int()
				###debug###
				f.write('trafo: '+str(q)+' at: '+str(p+1)+'\n')
				###########
				if result[p] != q:
					result = complement(result)

			#test for reverse
			if (rev!=None):
				p = positions[rev]
				print(p+1, flush=True); n_query+=1;
				q = get_int()
				###debug###
				f.write('trafo: '+str(q)+' at: '+str(p+1)+'\n')
				###########
				if result[p] != q:
					result = reverse(result)

	#convert to string and output
	result = [ ('1' if x==True else ('0' if x==False else str(x) )) for x in result]
	result = ''.join(result)
	print(result, flush=True)

	response = get_line().replace('\n','')
	if response!='Y':
		raise 'wrong answer'
		sys.exit()
	###debug###
	f.write('calculated: '+''.join(result)+' \n')
	f.write('confirmed: '+str(response)+' \n')
	###########
###debug###
f.close()
###########