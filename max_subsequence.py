#!/usr/bin/env python

from subsequence_helpers import full_seq

def max_subfull_seq(full_seq):

    maximumSum = runningSum = full_seq[0]
    i = 0
    start = 0
    finish = 0

    for j in range(1, len(full_seq)):

        if full_seq[j] > (runningSum + full_seq[j]):
            runningSum = full_seq[j]
            i = j

        else:
            runningSum += full_seq[j]

        if runningSum > maximumSum:
            maximumSum = runningSum

            if full_seq[i] != 0:
                start = i
            else:
                start = i + 1

            finish = j

    print "maximum contiguous sum = ", maximumSum
    print "index of starting element:", start
    print "index of ending element:", finish
    return maximumSum


max_subfull_seq(full_seq)