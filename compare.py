def equality(l1, l2):
	if l1 == l2:
		print("Congratulations, you won !");
		return 1
	else:
		return 0

def compare(l1, l2):

	if equality(l1, l2):
		return 1;
	else:
		# check number of colors ok (but not in good order)
		colOk = 0
		for x in l1:
			for y in l2:
				if x==y:
					colOk = colOk + 1

		# check if correct order
		order = 0
		for x in l1:
			for y in l2:
				if x==y:
					order = order + 1
					break
				else:
					break

		res = [colOk, order]
		return res