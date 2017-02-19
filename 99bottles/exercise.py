class Bottles:
    X_BOTTLES = '{count_before} {pluralise_before} of beer on the wall, {count_before} {pluralise_before} of beer.\n'
    TAKE_ONE_DOWN = 'Take {pronoun} down and pass it around, {count_after} {pluralise_after} of beer on the wall.'
    GO_TO_STORE = 'Go to the store and buy some more, 99 bottles of beer on the wall.'

    def verse(self, bottles):
        template = self._get_template(bottles)
        one_verse = self._populate_template(template, bottles)
        return one_verse

    def verses(self, start, end):
        accumulator = [self.verse(bottles)
                       for bottles in range(start, end - 1, -1)]
        return '\n\n'.join(accumulator)

    def song(self):
        return self.verses(99, 0)

    def _get_template(self, bottles):
        first_part = self.X_BOTTLES
        second_part = self.GO_TO_STORE if bottles == 0 else self.TAKE_ONE_DOWN
        return first_part + second_part

    def _populate_template(self, template, bottles):
        bottles_after = bottles - 1
        count_before = self._str_count(bottles)
        count_after = self._str_count(bottles_after)
        pluralise_before = self._pluralise('bottle', count=bottles)
        pluralise_after = self._pluralise('bottle', count=bottles_after)
        pronoun = self._pronoun(bottles)

        verse = template.format(count_before=count_before,
                                count_after=count_after,
                                pluralise_before=pluralise_before,
                                pluralise_after=pluralise_after,
                                pronoun=pronoun)

        verse = self._capitalize_first_letter(verse)

        return verse

    @staticmethod
    def _pronoun(count):
        return 'it' if count == 1 else 'one'

    @staticmethod
    def _str_count(count):
        return 'no more' if count == 0 else str(count)

    @staticmethod
    def _pluralise(noun, count):
        return noun if count == 1 else noun + 's'

    @staticmethod
    def _capitalize_first_letter(text):
        return text[0].upper() + text[1:]
