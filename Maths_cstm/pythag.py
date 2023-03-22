def red(inp):
	if inp-int(inp)==0:
		inp=int(inp)
		return inp


usr_input=input("type in the triplet[Seperate values with a space]: ")
list=[]
list1=usr_input.split()
for item in list1:
	list.append(float(item))
list.sort()
try:
	b=red(float(list[0]))
	p=red(float(list[1]))
	b_2=b**2
	p_2=p**2
	b_p=b_2 + p_2
	h=red(float(list[2]))
	h_2=h**2
	print(f"{b}^2 + {p}^2")
	print(f"= {b_2} + {p_2}")
	print(f"= {b_p}")
	print("")
	print(f"{h}^2")
	print(f"= {h_2}")
	if b_p==h_2:
		print(f"{b_p} is equal to {h_2}")
		print(f"""Hence the given values are pythagorean triplets
by the converse of Pythagoras Theorem""")
	if b_p!=h_2:
				print(f"{b_p} is NOT equal to {h_2}")
				print(f"""Hence the given values are NOT pythagorean triplets
by the converse of Pythagoras Theorem""")
except ValueError:
		print("The given input is Invalid")
		
