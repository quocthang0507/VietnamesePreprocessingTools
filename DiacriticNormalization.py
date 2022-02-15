def old_to_new_diacritic(word: str, reversed: bool = False):
    old = ['òa', 'óa', 'ỏa', 'õa', 'ọa', 'òe', 'óe',
           'ỏe', 'õe', 'ọe', 'ùy', 'úy', 'ủy', 'ũy', 'ụy']
    new = ['oà', 'oá', 'oả', 'oã', 'oạ', 'oè', 'oé',
           'oẻ', 'oẽ', 'oẹ', 'uỳ', 'uý', 'uỷ', 'uỹ', 'uỵ']
    for i in range(0, len(new)):
        word = word.replace(
            new[i], old[i]) if reversed else word.replace(old[i], new[i])
