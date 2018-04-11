import string
from collections import deque



def sub(s):
	final = ""
	try:
		w, h = 2, 31;
		alpha = [[0 for x in range(w)] for y in range(h)] 

		low = 95
		high = 125

		i = low
		j = high
		n = 0
		index1 = 0
		index2 = 0
		while(index1 < 31):
			while(index2 < 31):
				alpha[index1][index2] = chr(i)
				alpha[index1][index2 + 1] = chr(j)
				i = i + 1
				j = j - 1
				index1 = index1 + 1
			index2 = index2 + 1

	except:
		pass

	final = list(final)
	for i in s:
		for k in alpha:
			if i in k[0]:
				final.append(k[1])
	return ''.join(final)


def shifting(abc):
	word = sub(abc)
	d = deque(list(word))
	d.rotate(-3)
	return ''.join(d)



# clear = #plaintexthere
# encrypted = shifting(clear)
# print encrypted
