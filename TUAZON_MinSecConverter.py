#promt the user to enter an integer for seconds
Integer = int(input("Enter an integer for seconds: "))

#print outcome statement
print(Integer, "seconds is", int(Integer/60), "minutes and", int(Integer%60), "seconds")