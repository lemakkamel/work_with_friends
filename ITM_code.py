def atm_function(request):
	if request>500 or request<0:
		print "you can't"
	else:
		while request > 0:
			if request >= 100:
				request -= 100
				print "give ", 100
			if request >= 50 and request < 100:
				request -= 50
				print "give ", 50
			if request >= 10 and request < 50:
				request -= 10
				print "give ", 10
			if request >= 5 and request < 10:
				request -= 5
				print "give ", 5
			if request < 5 and request != 0:
				print "give ", request
				request = 0
atm_function(277)