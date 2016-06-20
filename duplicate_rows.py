# -*- coding:utf-8 -*-

import codecs

file_path     = 'duplicate_rows_test.txt'
enc           = 'utf-8'
output_file   = './dupulicate_rows_output.txt'
duplicate_num = 4

output_fp = codecs.open(output_file, 'w', enc)

with codecs.open(file_path, 'r', enc) as fp:
    for line in fp:
        output_fp.write(line * duplicate_num)


