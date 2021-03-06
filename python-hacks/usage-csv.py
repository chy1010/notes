from csv import Sniffer
import csv

def main():
    with open('data/simple-num-seq.txt') as fp:

        fp.seek(0, 2)
        # check if the document is empty
        if fp.tell():

            fp.seek(0)
            dialect = Sniffer().sniff(fp.readline(), delimiters=None)
            fp.seek(0)

            # deal with the extra space that initiates in front of every elememts
            # (behind the comma ',' or at the begining of document)
            dialect.skipinitialspace = True

            reader = csv.reader(fp, dialect)
            for row in reader:
                print(row)
                
if __name__ == '__main__':
    main()