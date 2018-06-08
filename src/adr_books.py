# -*- coding: utf-8 -*-
'''
Given a flat file of book metadata, write a Library class that parses the book data and provides an API that lets you search for all books containing a word.

API:

Library
- <constructor>(input) -> returns a Library object
- search(word) -> returns all books that contain the word anywhere in the
                  title, author, or description fields. Only matches *whole* words.
E.g. Searching for "My" or "book" would match a book containing "My book", but searching for "My b" or "boo" would *not* match.
'''
import re
from sre_constants import SRE_FLAG_DOTALL


LIBRARY_DATA = """
TITLE: Hitchhiker's Guide to the Galaxy
AUTHOR: Douglas Adams
DESCRIPTION: Seconds before the Earth is demolished to make way for a galactic freeway,
Arthur Dent is plucked off the planet by his friend Ford Prefect, a researcher for the
revised edition of The Hitchhiker's Guide to the Galaxy who, for the last fifteen years,
has been posing as an out-of-work actor.

TITLE: Dune
AUTHOR: Frank Herbert
DESCRIPTION: The troubles begin when stewardship of Arrakis is transferred by the
Emperor from the Harkonnen Noble House to House Atreides. The Harkonnens don't want to
give up their privilege, though, and through sabotage and treachery they cast young
Duke Paul Atreides out into the planet's harsh environment to die. There he falls in
with the Fremen, a tribe of desert dwellers who become the basis of the army with which
he will reclaim what's rightfully his. Paul Atreides, though, is far more than just a
usurped duke. He might be the end product of a very long-term genetic experiment
designed to breed a super human; he might be a messiah. His struggle is at the center
of a nexus of powerful people and events, and the repercussions will be felt throughout
the Imperium.

TITLE: A Song Of Ice And Fire Series
AUTHOR: George R.R. Martin
DESCRIPTION: As the Seven Kingdoms face a generation-long winter, the noble Stark family
confronts the poisonous plots of the rival Lannisters, the emergence of the
White Walkers, the arrival of barbarian hordes, and other threats.

"""


def remove_non_alpha_chars(s):
    s = s.replace("\n", " ")
    s = re.sub("[^a-zA-Z0-9\s']+", "", s)
    return s.strip()


class Book:
    def __init__(self, title, author, desc):
        self.title = remove_non_alpha_chars(title)
        self.author = remove_non_alpha_chars(author)
        self.description = remove_non_alpha_chars(desc)

        words = set(self.title.split(" "))
        words = words.union(set(self.author.split(" ")))
        words = words.union(set(self.description.split(" ")))
        self.words = words


class Library:

    def __init__(self, data):

        book_text = data.split("\n\n")
        self.books = []
        for t in book_text:
            if not t:
                continue

            m = re.search('.*TITLE:(.*)AUTHOR:(.*)DESCRIPTION:(.*)', t, SRE_FLAG_DOTALL)

            title = m.group(1)
            author = m.group(2)
            description = m.group(3)
            self.books.append(Book(title, author, description))

    def search(self, word):
        results = []
        for b in self.books:
            if word in b.words:
                results.append(b)
        return results


library = Library(LIBRARY_DATA)
first_results = library.search("Arrakis")
assert first_results[0].title == "Dune"
second_results = library.search("winter")
assert second_results[0].title == "A Song Of Ice And Fire Series"
third_results = library.search("demolished")
assert third_results[0].title == "Hitchhiker's Guide to the Galaxy"
fourth_results = library.search("the")
assert len(fourth_results) == 3
assert fourth_results[1].title == "Dune"
assert fourth_results[2].title == "A Song Of Ice And Fire Series"
assert fourth_results[0].title == "Hitchhiker's Guide to the Galaxy"
print("All tests passed!")
