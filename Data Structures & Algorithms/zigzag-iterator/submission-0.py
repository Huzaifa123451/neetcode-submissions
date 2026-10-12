class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = deque([v for v in (deque(v1), deque(v2)) if v])
        
    def next(self) -> int:
        curr_list = self.queue.popleft()
        val = curr_list.popleft()
        if curr_list:
            self.queue.append(curr_list)
        return val

    def hasNext(self) -> bool:
        return bool(self.queue)