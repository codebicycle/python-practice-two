class Bottles(object):

    def verse(self, bottles):
        bottles_after = bottles - 1
        pluralise_before = self._pluralise('bottle', count=bottles)
        pluralise_after = self._pluralise('bottle', count=bottles_after)
        pronoun = self._pronoun(bottles)
        count_before = self._str_count(bottles)
        count_after = self._str_count(bottles_after)

        first_line_template = '{count_before} {pluralise_before} of beer on the wall, {count_before} {pluralise_before} of beer.\n'
        if bottles == 0:
            second_line_template = 'Go to the store and buy some more, 99 bottles of beer on the wall.'
        else:
            second_line_template = 'Take {pronoun} down and pass it around, {count_after} {pluralise_after} of beer on the wall.'

        full_verse_template = first_line_template + second_line_template
        full_verse = full_verse_template.format(count_before=count_before,
                                                count_after=count_after,
                                                pluralise_before=pluralise_before,
                                                pluralise_after=pluralise_after,
                                                pronoun=pronoun)

        full_verse = self._capitalize_first_letter(full_verse)

        return full_verse

    def verses(self, start, end):
        accumulator = [self.verse(bottles) for bottles in range(start, end-1, -1)]
        return '\n\n'.join(accumulator)

    def song(self):
        return self.verses(99, 0)

    @staticmethod
    def _pronoun(count):
        if count == 1:
            return 'it'
        else:
            return 'one'

    @staticmethod
    def _str_count(count):
        if count == 0:
            return 'no more'
        else:
            return str(count)

    @staticmethod
    def _pluralise(noun, count):
        if count == 1:
            return noun
        else:
            return noun + 's'

    @staticmethod
    def _capitalize_first_letter(text):
        return text[0].upper() + text[1:]
