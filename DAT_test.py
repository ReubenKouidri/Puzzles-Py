def decode(message_file):
    def triangular_sequence(n):
        return n * (n + 1) // 2

    number_word_map = {}
    with open(message_file, 'r') as file:
        for line in file:
            num, word = line.strip().split(' ')
            number_word_map[int(num)] = word

    output = []
    max_num = max(number_word_map.keys())
    i, tri_num = 1, 1
    while tri_num <= max_num:
        output.append(number_word_map[tri_num])
        i += 1
        tri_num = triangular_sequence(i)

    return ' '.join(output)


if __name__ == '__main__':
    path = "coding_qual_input.txt"
    string = decode(path)
    print(string)
