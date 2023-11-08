input_file = open('input.txt')
text = input_file.readline()
input_file.close()
letters = list(filter(lambda symbol: symbol.isalpha(), set(text)))
statistic = {}
for letter in letters:
    statistic[letter] = text.count(letter)
statistic = sorted(statistic.items(), key=lambda x: x[1])
output_file = open('output.txt', 'w')
for i in range(len(statistic)):
    output_file.write(statistic[i][0] + ': ' + str(statistic[i][1]) + '\n')
output_file.close()