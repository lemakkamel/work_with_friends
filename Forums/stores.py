# This is class for stor members
class MemberStore():
    members=[]
    def __init__(self):
        pass

    def add(self,member):
        self.members.append(member.name)

    def get_all(self):
         return self.members


# This is class for stor Posts
class PostStore:
    posts = []
    def __init__(self):
        pass

    def add(self, post):
        self.posts.append(post.post_title)

    def get_all(self):
        return self.posts