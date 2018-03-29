import models

member1=models.Member("Bahaa",5)
member2=models.Member("wassim",10)

post1=models.Post("Python","This is an introduction to python")
post2=models.Post("Variables","A name that refers to a value.")
post3=models.Post("Assignment","A statement that assigns a value to a variable.")
print "="*35
print "This is Name of member One ",member1.name
print "This is Age of member One ",member1.age
print "="*35
print "This is Name of member Two ",member2.name
print "This is Age of member Two ",member2.age
print "="*35
print "="*7+"This is first post "+"="*7
print post1.post_title
print post1.post_content
print "="*7+"This is second post "+"="*7
print post2.post_title
print post2.post_content
print "="*7+"This is third post "+"="*7
print post3.post_title
print post3.post_content