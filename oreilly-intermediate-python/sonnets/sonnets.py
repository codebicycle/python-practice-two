import time

my_words = [elt.strip() for elt in open("sonnet_words.txt", "r").readlines()]
word_list = [elt.strip() for elt in open("sowpods.txt", "r").readlines()]
word_set = set(word_list)

counter = 0

start_time = time.perf_counter()
for word in my_words:
    if word not in word_list:
        print(word)
        counter += 1
elapsed_time = time.perf_counter() - start_time

print("Total new words: %d" % counter)
print("List, elapsed time: %.2fs" % elapsed_time)

print()
counter = 0

start_time = time.perf_counter()
for word in my_words:
    if word not in word_set:
        print(word)
        counter += 1
elapsed_time = time.perf_counter() - start_time


print("Total new words: %d" % counter)
print("Set, elapsed time: %.2fs" % elapsed_time)
