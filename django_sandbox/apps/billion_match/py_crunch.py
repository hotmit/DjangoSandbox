from datetime import datetime

start = datetime.now()

with open('needles.tmp', 'r') as f:
    needles = f.readlines()
    needles = dict.fromkeys([n.strip() for n in needles])

counter = 0
found = 0
with open('haystack.tmp', 'r') as f:
    line = 'X'
    while line:
        line = f.readline()
        counter += 1
        parts = line.split('|')

        if counter % 1000000 == 0:
            print('      Counter: {0:,}, Found: {1:,}'.format(counter, found))

        if parts and len(parts) == 3:
            key = parts[1]
            if key in needles:
                found += 1

print('Total: {0:,}'.format(counter))
print('Matched: {0:,}'.format(found))

end = datetime.now()
duration = (end - start).total_seconds() / 60
print('Duration: %s min' % duration)

# Total: 2,000,000,001
# Matched: 300,014,400
# Duration: 75 min