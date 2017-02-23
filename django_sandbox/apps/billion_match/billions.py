from random import randint
from os import path

# http://stackoverflow.com/questions/42239179/fastest-way-to-find-lines-of-a-text-file-from-another-larger-text-file-in-bash

haystack_filename = 'haystack.tmp'
if not path.exists(haystack_filename):
    with open('%s' % haystack_filename, 'w') as f:
        for i in range(0, 1000000000):
            name = 'foo' if randint(0,1) else 'bar'
            num = randint(1,100)
            f.write('date|%s%d|number\n' % (name, num))
    print('Bam billion!')

needle_filename = 'needles.tmp'
if not path.exists(needle_filename):
    with open(needle_filename, 'w') as f:
        for i in range(0, 15000):
            name = 'foo' if randint(0,1) else 'bar'
            num = randint(1,20)
            f.write('%s%d\n' % (name, num))
    print('Bam mini billion!')