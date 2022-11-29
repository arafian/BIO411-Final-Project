'''
trimming files based on quality score
sample fastq files from: https://zenodo.org/record/3736457#.Y4VlY-zMKEs
quality score calculation: https://support.illumina.com/help/BaseSpace_OLH_009008/Content/Source/Informatics/BS/QualityScoreEncoding_swBS.htm
'''

def main():

    threshold = int(input("Please enter a quality score threshold: "))
    fastq_file_path = input("Please enter the file path of the fastq file to filter: ")
    output_file_name = fastq_file_path + "_" + str(threshold) + ".fastq"

    with open(fastq_file_path, "r") as fastq_file:
        with open(output_file_name, "w") as filtered_file:

            lines = fastq_file.readlines()
            above_threshold_count = 0
            below_threshold_count = 0
            count = 0

            for i in range(0, len(lines), 4):
                above_threshold = True
                header = lines[i]
                sequence = lines[i+1]
                sign = lines[i+2]
                quality_scores = lines[i+3]

                for k in range(len(quality_scores) - 1):
                    score = ord(quality_scores[k]) - 33
                    if score < threshold:
                        above_threshold = False
                        break

                if above_threshold:
                    filtered_file.write(header)
                    filtered_file.write(sequence)
                    filtered_file.write(sign)
                    filtered_file.write(quality_scores)
                    above_threshold_count += 1

                else:
                    below_threshold_count += 1
                count += 1

    fastq_file.close()
    filtered_file.close()

    print("{0} total sequences in {1}".format(count, fastq_file_path))
    print("{0} sequences above the threshold of {1}".format(above_threshold_count, threshold))
    print("{0} sequences below the threshold of {1}".format(below_threshold_count, threshold))

if __name__ == '__main__':
    main()