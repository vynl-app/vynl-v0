import party,os
#try:
x=party.Party("hey","195.196.1.1")
song="xxx5"
song2="yyy5"
song3="fff5"
song4="qqqqq"
x.addSong(song,"exampleimage","name","channelman")
x.addSong(song2,"exampleimage","name2","channelwhat")
x.addSong(song3,"exampleimage","name3","channelwho")
x.addSong(song4,"exampleimage","name4","itstaytay")
for i in xrange(20):
	x.upVote(song,"199")
for i in xrange(11):
	x.downVote(song,"167")
for i in xrange(13):
	x.upVote(song2,"189")
for i in xrange(20):
	x.downVote(song3,"155")
for i in xrange(30):
	x.downVote(song4,"155")
for i in xrange(50):
	x.upVote(song4,"155")

print x.getOrdered("155")
y=party.Party("hey")
print y.getDJ()
print y.getOrdered("167")
x.end()
#except:
#	os.system("rm uniques.db;rm hey.db")
