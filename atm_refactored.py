def withdraw(balance, request):
    print "Current balance = ",balance
    new_balance = balance - request
    if request > balance:
        print("Can't give you all this money !!")

    elif request < 0:
        print("More than zero plz!")
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
    return new_balance
balance = 500

balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)