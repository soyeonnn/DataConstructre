from heapify_code import *


class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙

    def insert(self, data):
        """삽입 메소드"""
        self.heap.append(data)  # 힙의 마지막에 데이터 추가
        reverse_heapify(self.heap, len(self.heap)-1)  # 삽입된 노드(추가된 데이터)의 위치를 재배치

    def extract_max(self):
        """최우선순위 데이터 추출 메소드"""

        # root 노드와 마지막 노드의 위치를 바꾼다.
        swap(self.heap, 1, len(self.heap)-1)

        # 마지막 위치로 간 원래 root 노드의 데이터를 별도 변수에 저장하고, 노드는 힙에서 지운다.
        extract_num = self.heap.pop()

        # 새로운 root 노드를 대상으로 heapify 해서 망가진 힙 속성을 복원
        heapify(self.heap, 1, len(self.heap))

        return extract_num

    def __str__(self):
        return str(self.heap)


# 출력 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())