##### Reviewing the prerequsite concepts needed for Udacity Intro to Data Analysis course #####

##### If Statement

print("\n REVIEWING IF STATEMENT")

# take input at command line
s = input('--> Which do you prefer? Giraffe or hippo? ') 
#print(s)

if s.upper() == 'GIRAFFE' :
	print("Yay, giraffes are my favorite too!")
elif s.upper() == 'HIPPO' :
	print("Oh boy. I love hippos too, but do prefer giraffes.")
else :
	print ("You didn't answer my question with either 'giraffe' or 'hippo'")


##### Loops

print("\n REVIEWING LOOPS")

# loop 1
d = [1,6,3]
for i in d:
	print("loop1",i)

# loop 2
start = 1
end = 5
while start <= end:
	print ("loop2","start",start,"end",end)
	start += 1

##### Functions

print("\n REVIEWING FUNCTIONS")

def sq(num):
	num_sq = int(num) * int(num)
	#return num_sq
	print ("The square of",num,"is",num_sq)

t = input("--> What do you want the square of? ")
sq(t)