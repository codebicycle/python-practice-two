"""
--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

    abba[mnop]qrst supports TLS (abba outside square brackets).
    abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
    aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
    ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).

How many IPs in your puzzle input support TLS?

--- Part Two ---

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

    aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
    xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
    aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
    zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).

How many IPs in your puzzle input support SSL?

"""
import re

# letter, different letter, followed by the first two in reverse order
ABBA = re.compile(r'(.)(?!\1) (.) \2\1', flags=re.X)

# above regexp somewhere inside brackets
ABBA_BRACKETS = re.compile(r'\[\w* (.)(?!\1) (.) \2\1 \w*\]', flags=re.X)

ABA = re.compile(r'(?= (.)(?!\1) (.) \1)', flags=re.X)

BRACKETS = re.compile(r'\[ \w+ \]', flags=re.X)


def valid_tls(line):
    match = ABBA_BRACKETS.search(line)
    if match:
        return False

    match = ABBA.search(line)
    if match:
        return True
    return False


def valid_ssl(line):
    brackets = BRACKETS.findall(line)
    outside = BRACKETS.split(line)

    babs = []
    for string in brackets:
        matches = ABA.findall(string)
        babs.extend(matches)

    for string in outside:
        for bab in babs:
            a = bab[1]
            b = bab[0]
            match = re.search(a+b+a, string)
            if match:
                return True
    return False


def count_valid_ips(file_handle):
    tls = 0
    ssl = 0
    for line in file_handle:
        if valid_tls(line):
            tls += 1
        if valid_ssl(line):
            ssl += 1
    return tls, ssl


def main():
    with open('input7.txt', 'r') as f:
        tls, ssl = count_valid_ips(f)

    print(tls)
    print(ssl)


if __name__ == '__main__':
    main()
