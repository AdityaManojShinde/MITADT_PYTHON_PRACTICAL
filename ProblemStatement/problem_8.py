# Problem Statement 8: Write a program to manage a club membership system. The program 
# should allow the user to add members to a Sports Club and an Art Club, and list the members 
# who are part of both clubs and those who are part of only one club. Also, list the members 
# across both clubs. 

class Club:
    def __init__(self):
        self.sports_club = set()
        self.art_club = set()

    def add_member(self, name, club="sports"):
        if club == "sports":
            self.sports_club.add(name)
        elif club == "art":
            self.art_club.add(name)

    def list_members(self):
        print("\nMembers in Sports Club: ", self.sports_club)
        print("\nMembers in Art Club: ", self.art_club)
    def list_common_members(self):
        print("\nMembers in both clubs: ", self.sports_club & self.art_club)
    def list_unique_members(self):
        print("\nMembers in only Sports Club: ", self.sports_club - self.art_club)
        print("\nMembers in only Art Club: ", self.art_club - self.sports_club)
    def list_all_members(self):
        print("\nAll members: ", self.sports_club | self.art_club)

club = Club()
club.add_member("John", "sports")
club.add_member("Mike", "sports")
club.add_member("John", "art")
club.list_all_members()
club.list_members()
club.list_common_members()
club.list_unique_members()

    