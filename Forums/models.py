class Member:
    last_id = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "Member name: {}, member age: {}".format(self.name,self.age)


class Post:
    def __init__(self, post_title, post_content):
        self.post_title = post_title
        self.post_content = post_content

    def __str__(self):
        return "The title : {}\nContent: {}".format(self.post_title,self.post_content)



