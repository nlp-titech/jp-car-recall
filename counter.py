import os
import argparse
from pathlib import Path
from collections import defaultdict
import pandas as pd
from tabulate import tabulate

def calculate_ann(path):
    lst = [ p for p in  Path(path).rglob('*.ann') if os.stat(p).st_size > 0]
    txt_len_lst = []
    for p in lst:
        txt = p.with_suffix('.txt')
        with txt.open() as f:
            text = ''.join(f.read().split())
            txt_len_lst.append(len(text))
    ent_num = defaultdict(int)
    rel_num = defaultdict(int)
    for path in lst:
        with open(path, 'r') as f:
            for line in f.readlines():
                ann = line.split()
                if ann[0][0] == 'T':
                    ent_num[ann[1]] += 1
                elif ann[0][0] == 'R':
                    rel_num[ann[1]] += 1
    return txt_len_lst, len(lst), ent_num, rel_num

def generate_pd(ent_num, rel_num):
    tb_ent = [[key, ent_num[key]] for key in ent_num]
    tb_rel = [[key, rel_num[key]] for key in rel_num]
    header_ent = ['entity', '#']
    header_rel = ['relation', '#']
    return tb_ent, header_ent, tb_rel, header_rel

def output_table(txt_len_lst, doc_num, tb_ent, header_ent, tb_rel, header_rel):
    
    print(f'Number of documents: {doc_num}\nAverage document length: {sum(txt_len_lst)/len(txt_len_lst):.2f}\n')
    print(f'Entity stats')
    print(tabulate(tb_ent, header_ent, tablefmt='github'))
    print(f'\nRelation stats')
    print(tabulate(tb_rel, header_rel, tablefmt='github'))
    

def run(dir_path):
    txt_len_lst, doc_num, ent_num, rel_num = calculate_ann(dir_path)
    tb_ent, header_ent, tb_rel, header_rel = generate_pd(ent_num, rel_num)
    output_table(txt_len_lst, doc_num, tb_ent, header_ent, tb_rel, header_rel)
    
if __name__ == "__main__":
    """
    Usage:
        python counter.py dir_path
    Example:
        python counter.py part_relationship
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_path', type=str)
    args = parser.parse_args()
    run(args.dir_path)