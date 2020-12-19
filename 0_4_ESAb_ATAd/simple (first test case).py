import sys

file_in = sys.stdin
file_out = sys.stdout

def get_line(): return file_in.readline()
def get_int(): return int(get_line())
def get_ints(): return [int(x) for x in get_line().split()]

cases,size = get_ints()

for k in range(cases):
	result = list()

	#get values
	for i in range(size):
		print(str(i+1), flush=True)
		query = get_int()
		result.append(query)

	#combine numbers into string
	result = [str(x) for x in result]
	result = ''.join(result)
	print(result, flush=True)

	#get response wheter answer is right
	response = get_line().replace('\n','')
	if response!='Y':
		raise 'wrong answer'
		sys.exit()