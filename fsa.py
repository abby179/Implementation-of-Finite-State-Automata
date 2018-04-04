class FSA:
    def __init__(self, states, alphabet, init, accept, transitions):
        self.states = states
        self.alphabet = alphabet
        self.init = init
        self.accept = accept
        self.transitions = transitions
        self.word_dict = {}
        for st1, symbol, st2 in self.transitions:
            self.word_dict[(st1, st2)] = symbol
        self.dict = {}
        for v in self.states:
            self.dict[v] = []
        for t in self.transitions:
            self.dict[t[0]].append(t[2])

    def accepts(self, word):
        start = self.init
        find = False
        for i in word:
            for st1, symbol, st2 in self.transitions:
                if symbol == i and st1 == start:
                    start = st2
                    find = True
                    break
        if start not in self.accept:
            find = False
        return find

    def generate(self, n):
        words = []
        routes = [[self.init]]
        while routes:
            routesPrev = routes
            routes = []
            steps_ext = self.extend_steps(routesPrev)
            for step in steps_ext:
                if len(step) > n:
                    break
                elif step[-1] in self.accept:
                    word = ''
                    for i in range(len(step)-1):
                        word += self.word_dict[(step[i], step[i+1])]
                    words.append(word)
                routes.append(step)
        return words

    def extend_steps(self, steps):
        ext_steps = []
        for step in steps:
            for v in self.dict[step[-1]]:
                ext_steps.append(self.extend(step, v))
        return ext_steps

    def extend(self, step, v):
        step = step + [v]
        new_step = step
        return new_step
