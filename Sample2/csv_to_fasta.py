import csv
seq_file = open('C:\Users\dell7\Documents\Tzachi\workspace\FitSeq\data\\reference_variant_full_sequences.csv','rb')
seq_csv = csv.reader(seq_file)
seq_fasta = open('C:\Users\dell7\Documents\Tzachi\workspace\FitSeq\data\\reference_variant_full_sequences.fa','wb')
seq_csv.next()
for seq in seq_csv:
#    seq_fasta.write('>' + seq[0] + ' | Gene: ' + seq[1] + ' | CDS Type: ' + seq[2] + ' | Promoter: ' + seq[3] + ' | RBS: ' + seq[4] + '\n')
    seq_fasta.write('>' + seq[0] + '\n')
    seq_fasta.write(seq[1]+ '\n')
