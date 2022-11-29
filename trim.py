'''
trimming files based on quality score
'''

def trim_file(file_path):
    with open(file_path, "r") as fastq_file:
        header = fastq_file.readline()
        sequence = fastq_file.readline()
        sign = fastq_file.readline()
        quality_scores = fastq_file.readline()
        print(quality_scores)

trim_file("SRR2362898.fastq")