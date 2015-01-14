#!/usr/bin/env python

import random, unittest
from subsequence_helpers import empty_seq, full_seq, subseqForTest

class TestMaxSubsequence(unittest.TestCase):

    def setUp(self):
        self.sub_seq = subseqForTest(full_seq)

    def tearDown(self):
        self.sub_seq = None

    def test_seqNotEmpty(self):
        self.assertNotEqual(sum(self.sub_seq), sum(empty_seq))

    def test_subSeqInFullSeq(self):
        self.full_seq = ' '.join(map(str, full_seq))
        self.sub_seq = ' '.join(map(str, self.sub_seq))
        self.assertTrue(self.full_seq.count(self.sub_seq) > 0)


suite = unittest.TestLoader().loadTestsFromTestCase(TestMaxSubsequence)
unittest.TextTestRunner(verbosity=2).run(suite)