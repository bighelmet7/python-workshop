#!/usr/bin/python

class User(object):

    def __init__(self, id, name, age, pic_profile=None):
        self.id = id
        self.name = name
        self.age = age
        self.pic_url = pic_profile
        self.friends = []

    def display_more_info(self, *args, **kwargs):
        print("Args info: ", args, "Kwargs info: ", kwargs)

    def __repr__(self):
        return '<ID %s> Name: %s - Age: %s' % (self.id, self.name, self.age)

def main():
    annie = User(id=0, name='Annie', age=22)
    jhon = User(id=1, name='Jhon', age=28, pic_profile="https://pic.inst.es/1")
    print(annie)
    print(jhon)
    annie.friends.append(jhon)
    annie.display_more_info(
        "Status of today...",
        "Status of 2 seconds ago",
        history=["London", "Denmark", "Poland"],
        blocked=["Danna"]
    )

if __name__ == '__main__':
    main()