import models
import stores

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


member_store = stores.MemberStore()
member_store.add(member1.name)
member_store.add(member2.name)
print "+"*15+"This will print all members !!"+"+"*15
print member_store.get_all()
print "+"*15+"This will print all posts !!"+"+"*15
post_stor=stores.PostStore()
post_stor.add(post1.post_title)
post_stor.add(post2.post_title)
post_stor.add(post3.post_title)
print post_stor.get_all()