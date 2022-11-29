
def main():
    res = {}
    input_file_path = input('What is the file path of the fastq :')
    output_file_name = input_file_path[:len(input_file_path) - 6] + ".fasta"
    input_file = open(input_file_path, 'r')
    output_file = open(output_file_name, 'w')
    items = input_file.readlines()
    for i in range(0, len(items), 4):
        sequence_header = items[i]
        sequence = items[i+1]
        res[sequence] = sequence_header
    for seq in res.keys():
        output_file.write(res[seq])
        output_file.write(seq)
    output_file.close()
    input_file.close()
    print("start - ", int(len(items) / 4))
    print("end - ", len(res.keys()))

if __name__ == '__main__':
    main()

