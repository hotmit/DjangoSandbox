import os
from random import randint
from os import path

# http://stackoverflow.com/questions/42239179/fastest-way-to-find-lines-of-a-text-file-from-another-larger-text-file-in-bash

CHUNK_SIZE = 100000

count = 0
haystack_filename = 'haystack.tmp'

if path.exists(haystack_filename):
    os.remove(haystack_filename)

if not path.exists(haystack_filename):
    with open('%s' % haystack_filename, 'w') as f:
        for i in range(0, int(2000000000/CHUNK_SIZE)):
            chunk = ''
            for c in range(0, CHUNK_SIZE):
                count += 1
                name = 'foo' if randint(0, 1) else 'bar'
                num = randint(1, 100)
                chunk += 'date|%s%d|number\n' % (name, num)
                if count % 1000000 == 0:
                    print('Count: {0:,}'.format(count))
            f.write(chunk)

    print('Bam billion!')

needle_filename = 'needles.tmp'
if not path.exists(needle_filename):
    with open(needle_filename, 'w') as f:
        for i in range(0, 15000):
            name = 'foo' if randint(0, 1) else 'bar'
            num = randint(1, 15)
            f.write('%s%d\n' % (name, num))
    print('Bam mini billion!')