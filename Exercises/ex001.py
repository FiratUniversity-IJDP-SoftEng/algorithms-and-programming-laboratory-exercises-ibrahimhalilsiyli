# Your Student ID: 240543022
# Your Name and Surname: IBRAHIM HALIL SIYLI

song = ["Twinkle, twinkle, little star,",
		"How I wonder what you are!",
		"Up above the world so high,",
		"Like a diamond in the sky."]

space = " " * len(song[0])

print( song[0],
	  '\n',space[0:6], song[1],
	  '\n',space[0:14],song[2],
	  '\n',space[0:14],song[3]+ #The '+' operator was used because no space was desired.
	  '\n'+song[0],
	  '\n',space[0:6], song[1][:-1])


#in some code envoriment,'\t'code runs or showing differenly and ıt's possible to get different outputs.
#I used a specific number of spaces for all platforms to ensure the same output is displayed, instead of the example below.

#	 ||
#	 ||
#	\  /
#	 \/

#print(song[0],
#	  '\n','\t'*2, song[1],
#	  '\n','\t'*4, song[2],
#	  '\n','\t'*4, song[3],
#	  '\n', song[0][1:],
#	  '\n','\t'*2, song[1][:-1])
