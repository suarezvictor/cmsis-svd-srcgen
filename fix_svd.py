#chargpt
import re

def transform_bit_range(line):
    line = line.replace("%s", "0") #FIXME: dimension <dim> not supported

    pattern = r'<bitRange>(\[\d+:\d+\])</bitRange>'
    bit_range_pattern = re.compile(pattern)
    match = bit_range_pattern.search(line)
    if match:
        bit_range = match.group(1)
        start_bit, end_bit = map(int, re.search(r'(\d+):(\d+)', bit_range).groups())
        line = line.replace("<bitRange>", "").replace("</bitRange>", "")
        incremented_line = line.replace(bit_range, f'<bitOffset>{end_bit}</bitOffset><bitWidth>{start_bit-end_bit+1}</bitWidth>')
        print(incremented_line, end="")
    else:
        line = line.replace("[", "")
        line = line.replace("]", "")
        print(line, end="")

def parse_and_increment(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            transform_bit_range(line)
            
# Example usage:
file_path = 'd1_unofficial.svd'  # Replace with the path to your file
parse_and_increment(file_path)
