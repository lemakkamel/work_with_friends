import models
import stores

member1=models.Member("Bahaa",5)
member2=models.Member("wassim",10)
member3=models.Member("kamel",20)

post1=models.Post("Python","This is an introduction to python")
post2=models.Post("Variables","A name that refers to a value.")
post3=models.Post("Assignment","A statement that assigns a value to a variable.")
print "="*35
print member1
print "="*35
print member2
print "="*35
print "="*7+"This is first post "+"="*7
print post1
print "="*7+"This is second post "+"="*7
print post2
print "="*7+"This is third post "+"="*7
print post3


member_store = stores.MemberStore()
member_store.add(member1)
member_store.add(member2)
member_store.add(member3)
print "+"*15+"This will print all members !!"+"+"*15
print member_store.get_all()
print "+"*15+"This will print all posts !!"+"+"*15
post_stor=stores.PostStore()
post_stor.add(post1)
post_stor.add(post2)
post_stor.add(post3)
print post_stor.get_all()
print "-"*40
print member_store.get_by_id(1)
print member_store.entity_exists(member1)
member_store.delete(1)
print member_store.entity_exists(member1)
