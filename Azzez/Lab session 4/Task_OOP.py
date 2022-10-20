# creating the Artist Class
class Artist:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.songs = [] 

    #  This method adds new song to the Artist songs list
    def make_song(self, song):
        self.songs.append(song)
      
    # This method display all songs of this artist
    def all_songs(self):
        print("<<<<<<<<<<<<<<<<<<<<<<  All Songs by %s >>>>>>>>>>>>>>>>>>>>>>>>>" % (self.name))
        for song in self.songs:
            print(song)
        print("-----------------------------------------------------")

#  creating the Song class
class Song:

    def __init__(self, title: str, artist: object, duration: float) -> None:
        self.title = title
        self.artist_name = artist.name
        self.duration = duration

        # The code below links a song to an artist
        artist.make_song(self)
        

    # this method is a string representation of our song object 
    def __str__(self) -> str:
        return "%s by %s duration: %smins" % (self.title, self.artist_name, self.duration)

#  creating the Playlist class
class Playlist:

    def __init__(self, name) -> None:
        self.name = name
        self.playlist = []

    #  This method adds new song to the playlist
    def add_song(self, song):
        self.playlist.append(song)

    def display(self):      
        print("<<<<<<<<<<<<<< Playlist (%s) >>>>>>>>>>>" % (self.name))  
        for song in self.playlist:
            print(song)
        print("-----------------------------------------------------")


#  Testing aggregation 

# creating an Artist object
asake = Artist("Ololade Asake", 23)
nle_choppa = Artist("NLE Choppa", 21)

# creating songs object
sungba = Song("Sungba", asake, 3.20)
dull = Song("Dull", asake, 2.10)
Me_vs_me = Song("Me Vs Me", nle_choppa, 5.00)

# creating Playlist object
hiphop_playlist = Playlist("HipHop Playlist")
hiphop_playlist.add_song(sungba)
hiphop_playlist.add_song(dull)
hiphop_playlist.add_song(Me_vs_me)

# checking songs by artist
asake.all_songs()
nle_choppa.all_songs()
hiphop_playlist.display()




"""
 Inheritance Solution below
"""

class Person:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def get_profile_info(self):
        return "Name: %s, Phone number: %s" %(self.name, self.phone_number)

# Creating a Lecturer that inherits from Person class
class Lecturer(Person):

    def __init__(self, name, phone_number, academic_title, salary):
        self.academic_title = academic_title
        self.salary = salary
        super().__init__(name, phone_number)

    #  overriding the get_profile_info method from the parent class
    def get_profile_info(self):
        return "Name: %s, Phone number: %s, Academic title: %s, Salary: %s " %(self.name, self.phone_number, self.academic_title ,self.salary)

# creating a Lecturer object
soyinka = Lecturer("Wole Soyinka", "09045366254", "Doctor", 5_000_000)
print(soyinka.get_profile_info())