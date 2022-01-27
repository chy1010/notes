import random

class WORDLE:
    
    def __init__(self):
        with open('misc/wordle/core.txt', mode='r') as fp:
            core_words = fp.read().splitlines()
        with open('misc/wordle/extend.txt', mode='r') as fp:
            extend_words = fp.read().splitlines()
        
        all_words = core_words + extend_words
        self.core_words = core_words
        self.extend_words = extend_words
        self.all_words = all_words
        
        self.answer = None
        self.remain_chars = dict()
        self.match = None
        self.candidate_chars = set()
        self.ng_position = set()
        
    def clear(self):
        self.answer = None
        self.match = ['-'] * 5
        self.candidate_chars = set()
        self.ng_position = set()
        self.remain_chars = dict()
        for i in range(97, 123):
            self.remain_chars[chr(i)] = chr(i)
        
    def start(self):
        self.clear()
        self.question()
        self.ask()
    
    def wrong_position(self, c, i):
        self.candidate_chars.add(c)
        self.ng_position.add((c,i))
        
    def question(self):
        self.answer = random.choice(self.core_words)
        
    def check_position(self, word):
        for i, s in enumerate(word):
            if s not in self.remain_chars:
                return False
            if (s,i) in self.ng_position:
                return False
        return True
    
    @property    
    def possible_answer(self):
        word_list = {word: (sum([int(s==t)for s, t in zip(word, self.match)]), len(set(word)),
                            sum([int(s in self.candidate_chars) for s in word]))
                     for word in self.core_words if self.check_position(word)}
        word_list = sorted(word_list.items(), key = lambda k: k[1], reverse=True)
        return word_list
        
    def ask(self):
        j = 0
        while True:
            guess = input(f'{j+1}) make a guess? ')
            if guess not in self.all_words or len(guess) != 5:
                print('\r')
                continue
            for i, chars in enumerate(zip(guess, self.answer)):
                c, d = chars
                if c == d:
                    self.match[i] = c
                    print(f'*{c}*', end=' ')
                elif c in self.answer:
                    self.wrong_position(c,i)
                    print(f'-{c}-', end=' ')
                else:
                    if c in self.remain_chars:
                        self.remain_chars.pop(c)
                    print(f'x{c}x', end=' ')
            print('')
            remain = ''.join(list(self.remain_chars.values()))
            print(f'remain characters: {remain}')
            print(f'{"".join(self.match)}: candidate chars: {self.candidate_chars}')
            print(f'candidates: {self.possible_answer[:5]}')
            if guess == self.answer:
                print('Done!')
                break
            
            j += 1
        
            if j >= 6:
                print('Fail.')
                print(f'answer: {self.answer}')
                break
        
        
        
if __name__ == '__main__':
    
    wordle = WORDLE()
    wordle.start()
    