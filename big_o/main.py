import big_o

positive_int_gen = lambda n: big_o.datagen.integers(n, min_=0, max_=100000)
best, others = big_o.big_o(max, positive_int_gen, n_repeats=5)

print(best)
