import os, re

def is_data_seg(line):
    return re.match('^\.[a-z]{0,1}data', line)

def is_text_seg(line):
    return re.match('^\.text', line)

def is_2digit_hex(text):
    return re.match('^[0-9A-F]{2}\+?$', text)

def is_text_comment(text):
    return re.match('^_[a-z]?text$', text)

def is_data_comment(text):
    return re.match('^_[a-z]?data$', text)

def is_addr_label(text):
    return True if re.match('^sub_[0-9A-F]{6}\:?$', text) or re.match('^loc_[0-9A-F]{6}\:?$', text) or re.match('^ds\:{1}[a-zA-Z0-9]{1,}$', text) else False

def is_num_value(text):
    return True if ((text.endswith('h') and re.match('^[0-9A-F]{1,10}h$', text)) or re.match('^[0-9A-F]{1,10}$', text)) else False

def read_file(file):
    with open(file, 'r', encoding='ISO-8859-1') as f:
        struct_dict = {
            "text_arr": [],
            "file_name": file
        }
        for asm_line in f:
            asm_line = asm_line.strip()
            if is_text_seg(asm_line):
                struct_dict["text_arr"].append(asm_line)
            else:
                continue
        return struct_dict

def start_of_comment(arr):
    indices = [ i for i, token in enumerate(arr) if token.startswith(';') ]
    if len(indices) > 0:
        return indices[0]
    else:
        return None

def remove_commas(line_arr):
    newlinearr = []
    for line in line_arr:
        newline = []
        for token in line:
            if ',' in token:
                temp = token.split(',')
                temp = [ item for item in temp if item != '' ]
                for item in temp:
                    newline.append(item)
            else:
                newline.append(token)
        newlinearr.append(newline)
    return newlinearr

def cleanse_lines(line_arr, segment):
    # Split by whitespace each line in line_arr
    line_arr = [ line.split() for line in line_arr ]
    # Remove all comments from each line (array)
    line_arr = [ line[:(start_of_comment(line))] for line in line_arr ]
    # Remove the first word (".text*" or ".*data*") 
    # from each line (array), depending on whether 
    # they are data segment or text segment
    if segment == 'text':
        line_arr = [ [token for token in line if not is_text_seg(token)] for line in line_arr ]
    else:
        line_arr = [ [token for token in line if not is_data_seg(token)] for line in line_arr ]
    # Remove hexadecimal numbers (purpose is to 
    # remove the first few hex numbers which probably 
    # is the hex representation of the opcodes)
    line_arr = [ [token for token in line if not is_2digit_hex(token)] for line in line_arr ]
    # Remove all '??' from line
    line_arr = [ [token for token in line if not ('??' in token) ] for line in line_arr ]
    # Split all tokens using ','
    line_arr = remove_commas(line_arr)
    # Remove all empty line (array).
    line_arr = [ line for line in line_arr if line != [] ]
    # Remove all db, dw, dd, dq, dt, ddq and do opcodes and their operands
    # This is to help reduce the size of the dataset, and also since it 
    # only creates some variables
    line_arr = [ line for line in line_arr if line[0] != 'db' or line[0] != 'dw' or line[0] != 'dd' or line[0] != 'dq' or line[0] != 'dt' or line[0] != 'ddq' or line[0] != 'do' ]
    line_arr = [ line for line in line_arr if not (re.match('^include', line[0]) or re.match('^\.[0-9a-zA-Z]{1,}', line[0])) ]
    return line_arr

def separate_symbols(symbol, line):
    newline = []
    for i, token in enumerate(line):
        if symbol in token:
            temp_arr = token.split(symbol)
            for j in range(1, len(temp_arr), 2):
                temp_arr.insert(j, symbol)
            temp_arr = [ val for val in temp_arr if val ]
            for val in temp_arr:
                newline.append(val)
        else:
            newline.append(token)
    return newline
