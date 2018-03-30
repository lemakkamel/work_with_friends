# This is class for stor members
class MemberStore():
    members=[]
    def __init__(self):
        pass

    def add(self,member_name):
        self.members.append(member_name)

    def get_all(self):
         return self.members


# This is class for stor Posts
class PostStore:
    posts = []
    def __init__(self):
        pass

    def add(self, post):
        self.posts.append(post)

    def get_all(self):
        return self.posts