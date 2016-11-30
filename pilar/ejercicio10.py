import string
import random
all_chars = list(string.ascii_lowercase)
random.shuffle(all_chars)
print "----Abecedario Ordenado----"
print string.ascii_lowercase
print "----Abecedario Desordenado----"
print ''.join(all_chars)
