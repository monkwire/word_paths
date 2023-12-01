import unittest
from src.main import find_path, find_path_efficient


class FindWordPathTests(unittest.TestCase):

    def test_find_path(self):
        word_bank = ["bite", "bike", "book", "bike", "hike", "like", "lice", "vice" , "mice", "lice", "dice", "rice", "look", "nook", "cook", "hook", "hock", "hick"]
        assert(find_path("bike", "lice", word_bank) == ["bike", "like", "lice"])
        assert(find_path("bike", "bike", word_bank) == ["bike"])
        assert(find_path("bike", "car", word_bank) == [])

    def test_find_path_efficient(self):

        word_bank = ["bite", "bike", "book", "bike", "hike", "like", "lice", "vice" , "mice", "lice", "dice", "rice", "look", "nook", "cook", "hook", "hock", "hick"]
        assert(find_path_efficient("bike", "lice", word_bank) == ["bike", "like", "lice"])
        assert(find_path_efficient("bike", "bike", word_bank) == ["bike"])
        assert(find_path_efficient("bike", "car", word_bank) == [])


