

import os, csv, argparse
from parse import parse

parser = argparse.ArgumentParser(description='take a list of movies and export them to a CSV.')
parser.add_argument('--titles', action="store_true", help="prints titles for each column in the first row of the CSV")
parser.add_argument('directory')
parser.add_argument('filename_format') #format string for parsing filenames
parser.add_argument('column_names', metavar='N', type=str, nargs='+',
                   help='the list of column names')

args = parser.parse_args()

csv_rows = []

for dirname, dirnames, filenames in os.walk(args.directory):

    for dirname in dirnames:
        #ignore hidden stuff
        if dirname[0] == '.':
            dirnames.remove(dirname)

    # print path to all filenames.
    for filename in filenames:
        try:
            parsed=parse(args.filename_format, filename)
            csv_row = [parsed[col_name] for col_name in args.column_names]
            csv_rows.append(csv_row)
        except TypeError:
            #if there is no file matching the format, move on
            pass
    #     print(os.path.join(dirname, filename))


with open('dirlisting.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    if args.titles:
        writer.writerow(args.column_names)
    for row in csv_rows:
        writer.writerow(row)
