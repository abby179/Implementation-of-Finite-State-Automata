from fsa import FSA as FSA

fsaAA = FSA(['s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9'],
            ['a', 'n', 'o', 'p', 'r', 's', 'k'], 's0', ['s3', 's4', 's5', 's7'],
            [('s0', 'a', 's1'), ('s1', 'p', 's2'), ('s2', 'a', 's3'), ('s2', 'o', 's6'),
             ('s3', 'n', 's5'), ('s3', 's', 's4'), ('s5', 's', 's4'), ('s6', 'r', 's7'),
             ('s7', 'n', 's8'), ('s7', 's', 's4'), ('s8', 'a', 's5'), ('s1', 'n', 's9'), ('s9', 'k', 's2')])

fsaRegEx = FSA(['s0', 's1', 's2', 's3', 's4'],
               ['a', 'p', 'o', 'r'], 's0', ['s4'],
               [('s0', 'a', 's1'), ('s1', 'p', 's2'), ('s2', 'a', 's3'), ('s3', 'p', 's2'),
                ('s2', 'o', 's4'), ('s4', 'r', 's4')])

