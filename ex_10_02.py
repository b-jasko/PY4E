name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hours = list()
dictionary = dict()

for line in handle:
    if line.startswith("From "):
        line = line.split()
        line = line[5].split(':')
        hours.append(line[0])

for hour in hours:
    dictionary[hour] = dictionary.get(hour, 0) + 1

srtd = sorted([(v, k) for v, k in dictionary.items()])

for k, v in srtd:
    print(k, v)
