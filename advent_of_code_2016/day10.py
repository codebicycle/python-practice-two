"""
--- Day 10: Balance Bots ---

You come upon a factory in which many robots are zooming around handing small microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has two microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).

Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.

For example, consider the following instructions:

value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2

    Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
    Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
    Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
    Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.

In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip, and output bin 2 contains a value-3 microchip. In this configuration, bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.

Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips?

"""
import re

GET = re.compile(r'value (\d+).+?(bot \d+)')
GIVE = re.compile(r'(bot \d+).+?((?:output|bot) \d+).+?((?:output|bot) \d+)')


class Bot:
    bots = {}

    def __init__(self, bot_id):
        self.values = []
        self.bot_id = bot_id
        self.bots[bot_id] = self

    @classmethod
    def append_to(cls, bot_id, value):
        receiver = cls.get_or_create_bot(bot_id)
        receiver.values.append(value)

    @classmethod
    def get(cls, bot_id):
        target = cls.bots[bot_id]
        return target

    def is_valid(self):
        return len(self.values) >= 2

    @property
    def low(self):
        return min(self.values)

    @property
    def high(self):
        return max(self.values)

    def give(self, value, bot_id):
        Bot.append_to(bot_id, value)
        self.values.remove(value)

    def give_low(self, bot_id):
        self.give(self.low, bot_id)

    def give_high(self, bot_id):
        self.give(self.low, bot_id)

    @classmethod
    def get_or_create_bot(cls, bot_id):
        if bot_id in cls.bots:
            return cls.bots[bot_id]

        cls.bots[bot_id] = Bot(bot_id)
        return cls.bots[bot_id]


def traverse(lines):
    to_be_removed = []
    for idx, line in enumerate(lines):
        match = GET.match(line)
        if match:
            value = int(match.group(1))
            bot_id = match.group(2)

            Bot.append_to(bot_id, value)
            to_be_removed.append(idx)
            continue

        match = GIVE.match(line)
        if match:
            sender_id = match.group(1)
            low_id = match.group(2)
            high_id = match.group(3)

            sender = Bot.get_or_create_bot(sender_id)
            if not sender.is_valid():
                continue

            if sender.low == 17 and sender.high == 61:
                bot_number = int(sender_id[4:])
                print(bot_number)

            sender.give_low(low_id)
            sender.give_high(high_id)
            to_be_removed.append(idx)

    to_be_removed.sort(reverse=True)
    for idx in to_be_removed:
        lines.pop(idx)


def main():
    with open('input10.txt', 'r') as f:
        lines = f.readlines()

    while lines:
        traverse(lines)


if __name__ == '__main__':
    main()
