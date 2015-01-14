#!/usr/bin/env python

import random

empty_seq = []
full_seq = [1, -2, 0, 4, 5, -2, 7, 0]

def genRandomLength(full_seq):
    full_length = len(full_seq)
    sub_length = random.randint(1, full_length)
    return sub_length

def genRandomSubseq(full_seq, sub_length):
    seq_slice = list(full_seq)
    return seq_slice[:sub_length]

def subseqForTest(full_seq):
    length = genRandomLength(full_seq)
    subseq_for_test = genRandomSubseq(full_seq, length)
    return subseq_for_test