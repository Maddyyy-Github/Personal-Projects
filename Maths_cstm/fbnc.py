
	
			
def list_f(n_fn):
	i=0
	f=1
	sum=i+f
	l_f=[0]
	while len(l_f)<n_fn:
		l_f.append(f)
		i=f
		f=sum
		sum=i+f
										
	n_count=1
	for number in l_f:
		print(f"{n_count}. {number}")
		n_count+=1
											
									
def final_f(n_fn):
	i=0
	f=1
	sum=i+f
	l_f=[0]
	while len(l_f)<n_fn:
		l_f.append(f)
		i=f
		f=sum
		sum=i+f
	return l_f[-1]
		
		
