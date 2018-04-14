# This is class for stor members
class MemberStore():
    members=[]
    last_id = 1
    def __init__(self):
        pass

    def add(self,member):
        member.id=MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id+=1

    def get_all(self):
         return self.members

# This function give us member using its ID
    def get_by_id(self, id):
        all_members = self.get_all()
        for i in all_members:
            if i.id==id:
                return i

# This function used to check if the member exist in list of members
    def entity_exists(self, member):

        result = True

        if member not in self.members:
            result = False

        return result

# This function used to delete member using its ID
    def delete(self, id):
        for i in self.members:
            if i.id==id:
                self.members.remove(i)


# This is class for stor Posts
class PostStore:
    posts = []
    def __init__(self):
        pass

    def add(self, post):
        self.posts.append(post.post_title)

    def get_all(self):
        return self.posts