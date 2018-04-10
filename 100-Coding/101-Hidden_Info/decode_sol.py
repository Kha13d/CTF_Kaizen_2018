with open('dump.txt','r') as text:
	text_decode = (text.read())[:-1].decode('hex')
	text_conv = text_decode.split(',')
	for c in text_conv: print '\b'+eval(str(c)),
