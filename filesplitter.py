import sys, getopt
import os

__author__ = "Alemhar Salihuddin"
__pyversion__ = "3"
__version__ = "1.0.1"
__email__ = "alemhar@gmail.com"


header_options = {'y': True, 'n': False, 'none': 'none'}


def usage():
    print('USAGE: >>> python filesplitter.py -i <input-file> -r <row-per-file> --header [y|n|none]')


def main(argv):
    inputfile = ''
    row_count_limit = 0
    header_exist = True
    add_header = True # Add header by default

    try:
        opts,args = getopt.getopt(argv,"hi:r:a:",["ifile=","row=","header="])
    except getopt.GetoptError:
        usage() 
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage() 
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-r", "--row"):
            row_count_limit = int(arg)
        elif opt in ("-a", "--header"):
                header_option = header_options.get(arg, False)
                if header_option == 'none':
                    add_header = False
                    header_exist = False
                else:
                    add_header = header_option

    if not inputfile or row_count_limit == 0:
        usage() 
        sys.exit(2)

    with open(inputfile,'r') as source_file:
        outputfile = os.path.splitext(inputfile)[0]
        counter = 1
        row_counts = row_count_limit # Initialize row counts as row limit to create the first file
        first_line = True
        column_header = ''
        for line in source_file:
            if first_line and header_exist:
                column_header = line
                first_line = False
                continue
            if row_count_limit <= row_counts: # creating files
                output_file = open(outputfile + '_' + str(counter) + '.csv','w')
                if add_header:
                    output_file.write(column_header) 
                output_file.write(line) 
                row_counts = 1
                counter += 1
            else:          
                output_file.write(line) 
                row_counts += 1      


if __name__ == "__main__":
   main(sys.argv[1:])

