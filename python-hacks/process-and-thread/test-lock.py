from time import time, sleep
from threading import Thread, Lock


class Memo:
    def __init__(self):
        self.memos = dict()
        self._lock = Lock()

    def save_memo(self, memo):
        self._lock.acquire()

        try:
            self.memos[time()] = memo
            sleep(0.01)
        finally:
            self._lock.release()

    @property
    def show_memos(self):
        return self.memos


class SaveMemoThread(Thread):
    def __init__(self, memos, memo_string):
        super().__init__()
        self._memos = memos
        self._memo_string = memo_string

    def run(self):
        self._memos.save_memo(self._memo_string)


def main():
    note = Memo()
    threads = []
    for step in range(100):
        t = SaveMemoThread(note, f'step: {step}')
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(note.show_memos)


if __name__ == '__main__':
    main()