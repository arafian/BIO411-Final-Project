# BIO441-Final-Project
This tool utilizes the [Resistance Genome Identifier (RGI)](https://card.mcmaster.ca/analyze/rgi) tool within the Comprehensive Antibiotic Resistance Database to find expressed antibiotic resistance genes from transcriptomic data. These genes are then analyzed for differential expression using the [Rockhopper](https://cs.wellesley.edu/~btjaden/Rockhopper/) tool.

1. `Test transciptomes for CARD (click FASTA/FASTQ download)`
- [Antibiotic Resistant E. coli](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR2362898&display=metadata)
- [Reference Transcriptome E. coli](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR22250267&display=download)
- CARD is designed to take one input, but Rockhopper requires two inputs to be functional

2.`Other transcriptomes for testing`
- [1st B. anthracis transcriptome](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR028684&display=metadata)
- [2nd B anthracis transcriptome](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR028685&display=metadata)

3.`Search for transcriptomes on the Sequence Read Archive`
- [Sequence Read Archive](https://www.ncbi.nlm.nih.gov/sra) 

4. `Convert Fastq to Fasta`
- [This site explains how to do it](https://bioinformaticsworkbook.org/dataWrangling/fastaq-manipulations/converting-fastq-format-to-fasta.html#gsc.tab=0)
- Or use this code: `sed -n '1~4s/^@/>/p;2~4p' INFILE.fastq > OUTFILE.fasta`
