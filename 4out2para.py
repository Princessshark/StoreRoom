#is_Live = True
#is_Payment = True

if is_Live and is_Payment:
	print("positive green")
elif is_Live and not(is_Payment):
	print("unpaid orange ")
elif not(is_Live) and is_Payment:
	print("check orange")
else:
	print("negative red")
