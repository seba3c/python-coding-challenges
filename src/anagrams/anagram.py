# -*- coding: utf-8 -*-


def has_same_elements(s1, s2):
    s1_dict = {}
    s2_dict = {}
    for s in s1:
        s1_dict[s] = s1_dict.get(s, 0) + 1
    for s in s2:
        s2_dict[s] = s2_dict.get(s, 0) + 1
    return s1_dict == s2_dict


def anagrams(word=None):

    if (not word):
        return []

    anagram_list = []

    with open("wl.txt") as f:
        words = f.readlines()
    words = list(map(lambda x: x.replace("\n", ""), words))

    for w in words:
        if has_same_elements(word, w):
            anagram_list.append(w)

    return anagram_list


if __name__ == '__main__':
    print(anagrams())
    print(anagrams("horse"))
