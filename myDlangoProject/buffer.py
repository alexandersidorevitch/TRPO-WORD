from collections import deque


class Buffer:
    def __init__(self):
        self._history_deistveya = deque()
        self._history_otmennennih_deistveya = deque()

    def ctrl_z(self):
        if len(self._history_deistveya) >= 2:
            el = self._history_deistveya.pop()
            self._history_otmennennih_deistveya.append(el)
            return self._history_deistveya[-1]
        else:
            return None

    def shift_ctrl_z(self):
        try:
            el = self._history_otmennennih_deistveya.pop()
            self._history_deistveya.append(el)
            return el
        except:
            return None

    def append_to_history(self, el):
        self._history_deistveya.append(el)
