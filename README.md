# it parses filenames into CSV files i guess

just a little quick script i wrote to quickly get an entire directory tree of movies (folders and files) into CSV format to catalog them.

uses argparse so should be somewhat documented already, other than that i put basically no effort into documenting it. 


I probably wont be maintaining this

## Usage

`python3 filter.py "/path/to/media" "[format string]" [csv] [column] [names]`

### example:

`python3 filter.py "/path/to/media" "{name} ({year}){ext}" name year`

### Notes

- the variable length list of column names at the end must match variables defined in your format string
- the format string must match the whole filename, which is why the example has `{ext}`. you dont need to use all the variables you create. anything that doesnt match will not be included
-this will parse every file in every subdirectory (except ones starting with `.`) that it can find from the directory you give it. 