dna = list("acgtaact")

nucleotides = {}
for character in dna:
    if character not in nucleotides:
        nucleotides[character] = 0
    nucleotides[character] += 1

for key in nucleotides:
    print('Frequency of {} is {}'.format(key, nucleotides[key]))
