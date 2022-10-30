import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 4, 5)

#Check number of room
    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)

# Check_in method
    def test_check_in_guest(self):
        self.guest = Guest("Timmy", 150)
        self.room_1 = Room(1, 4, 5)
        self.room_1.check_in_guest(self.guest)
        self.assertEqual(3, self.room_1.space)

# Check_out method
    def test_check_out_guest(self):
        self.guest = Guest("Timmy", 150)
        self.room_1 = Room(1, 4, 5)
        self.room_1.check_in_guest(self.guest)
        self.room_1.check_out_guest(self.guest)
        self.assertEqual(4, self.room_1.space)

# Add_song method
    def test_add_song(self):
        self.song = Song("Buleria")
        self.room_1 = Room(1, 4, 5)
        self.room_1.add_song(self.song)
        self.assertEqual(1, len(self.room_1.songs))
