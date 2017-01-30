import collections
import heapq


class Huffman:
    def __init__(self, initial):
        if not initial:
            raise ValueError('Hufman expected a non empty string.')

        self.initial = initial
        frequency = collections.Counter(initial)

        priority_queue = []
        for char in frequency:
            priority_queue.append(Node(None, None, frequency[char], char))
        heapq.heapify(priority_queue)

        # Special case only one symbol
        if len(priority_queue) == 1:
            current = priority_queue[0]
            self.root = Node(current, None, 1)
            self.mapping = {char: '0'}
            return

        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            new_frequency = left.frequency + right.frequency
            new_node = Node(left, right, new_frequency)
            heapq.heappush(priority_queue, new_node)

        self.root = priority_queue[0]
        self.mapping = {}
        for char, code in self.root.encoding(''):
            self.mapping[char] = code

    def encode(self, message):
        code = []
        for char in message:
            if char not in self.mapping:
                raise ValueError("'{}' is not encoded.".format(char))
            code.append(self.mapping[char])

        return ''.join(code)

    def decode(self, code):
        message = []
        node = self.root
        for bit in code:
            node = node.left if bit == '0' else node.right
            if node.symbol:
                message.append(node.symbol)
                node = self.root

        return ''.join(message)

    def __repr__(self):
        return self.mapping


class Node:
    def __init__(self, left, right, frequency, symbol=None):
        self.left = left
        self.right = right
        self.symbol = symbol
        self.frequency = frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __str__(self):
        return "'{}':{}".format(self.symbol, self.frequency)

    def __repr__(self):
        return self.__str__()

    def encoding(self, code):
        if not self.left and not self.right:
            yield self.symbol, code
        else:
            for values in self.left.encoding(code + '0'):
                yield values
            for values in self.right.encoding(code + '1'):
                yield values


def main():
    message = 'A man, a plan, a canal, Panama.'
    print(message)

    # Build encoding
    huffman = Huffman(message)

    encoded = huffman.encode(message)
    print(encoded)

    decoded = huffman.decode(encoded)
    print(decoded)


if __name__ == '__main__':
    main()
