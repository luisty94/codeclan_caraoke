
class Room:
    def __init__(self, number, space, rent):
        self.number = number
        self.space = space
        self.rent = rent
        self.guests = []
        self.songs = []

    def check_in_guest(self, guest):
        self.guests.append(guest)
        self.space = self.space - 1

    def check_out_guest(self, guest):
        self.guests.remove(guest)
        self.space = self.space + 1 

    def add_song(self, song):
        self.songs.append(song)

    # def room_is_full(self, space):
    #    room_empty = self.space(4)
    #    room_full = self.space(0)

