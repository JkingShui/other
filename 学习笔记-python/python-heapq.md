## python学习笔记之heapq内置模块

>heapq内置模块位于./Anaconda3/Lib/heapq.py，提供基于堆的优先排序算法
>
>堆的逻辑结构就是完全二叉树，并且二叉树中父节点的值小于等于该节点的所有子节点的值。这种实现可以使用 heap[k] <= heap[2k+1] 并且 heap[k] <= heap[2k+2] （其中 k 为索引，从 0 开始计数）的形式体现，对于堆来说，最小元素即为根元素 heap[0]。

**1. 初始化**

可以通过 list 对 heap 进行初始化，或者通过 api 中的 heapify 将已知的 list 转化为 heap 对象。

**2. heapq.py中提供的函数方法**

```python
heapq.heappush(heap, item)

heapq.heappop(heap)：返回 root 节点，即 heap 中最小的元素。

heapq.heapreplace(heap,item): python3中heappushpop的更高效版。

heapq.heappushpop(heap, item)：向 heap 中加入 item 元素，并返回 heap 中最小元素。

heapq.heapify(x)：Transform list into a heap, in-place, in O(len(x)) time

heapq.merge(*iterables, key=None, reverse=False)

heapq.nlargest(n, iterable, key=None)：返回可枚举对象中的 n 个最大值，并返回一个结果集 list，key 为对该结果集的操作。

heapq.nsmallest(n, iterable, key=None)：同上相反

heapq._heappop_max(heap): Maxheap version of a heappop 

heapq._heapreplace_max(heap,item)：Maxheap version of a heappop followed by a heappush.

heapq._heapify_max(x)：Transform list into a maxheap, in-place, in O(len(x)) time

heapq._siftdown(heap,startpos,pos)： Follow the path to the root, moving parents down until finding a place

heapq._siftup(heap,pos)：Bubble up the smaller child until hitting a leaf

heapq._siftdown_max(heap,startpos,pos)：Maxheap variant of _siftdown

heapq._siftup_max(heap,pos)：Maxheap variant of _siftup
```

**举例：**

```python
import heapq
def heapsort(iterable):
    h = []
    for i in iterable:
        heapq.heappush(h, i)
    return [heapq.heappop(h) for i in range(len(h))]

# method 1: sort to list
s = [3, 5, 1, 2, 4, 6, 0, 1]
print(heapsort(s))
'''
[0, 1, 1, 2, 3, 4, 5, 6]
'''

# method 2: use key to find price_min
portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
             {'name': 'AAPL', 'shares': 50, 'price': 543.22},
             {'name': 'FB', 'shares': 200, 'price': 21.09},
             {'name': 'HPQ', 'shares': 35, 'price': 31.75},
             {'name': 'YHOO', 'shares': 45, 'price': 16.35},
             {'name': 'ACME', 'shares': 75, 'price': 115.65}]
cheap = heapq.nsmallest(1, portfolio, key=lambda s:s['price'])
print(cheap)
'''
[{'name': 'YHOO', 'shares': 45, 'price': 16.35}]
'''

# method 3: use while to push min element
def heapilize_list(x):
    n = len(x)
    # 获取存在子节点的节点 index 列表，并对每个节点单元进行最小堆处理
    for i in reversed(range(n // 2)):
        raiseup_node(x, i)

def put_down_node(heap, startpos, pos):
    current_item = heap[pos]
    # 判断单元中最小子节点与父节点的大小
    while pos > startpos:
        parent_pos = (pos - 1) >> 1
        parent_item = heap[parent_pos]
        if current_item < parent_item:
            heap[pos] = parent_item
            pos = parent_pos
            continue
        break
    heap[pos] = current_item

def raiseup_node(heap, pos):
    heap_len = len(heap)
    start_pos = pos
    current_item = heap[pos]
    left_child_pos = pos * 2 + 1
    while left_child_pos < heap_len:
        right_child_pos = left_child_pos + 1
        # 将这个单元中的最小子节点元素与父节点元素进行位置调换
        if right_child_pos < heap_len and not heap[left_child_pos] < heap[right_child_pos]:
            left_child_pos = right_child_pos
        heap[pos] = heap[left_child_pos]
        pos = left_child_pos
        left_child_pos = pos * 2 + 1
    heap[pos] = current_item
    put_down_node(heap, start_pos, pos)

p = [4, 6, 2, 10, 1]
heapilize_list(p)
print(p)
'''
[1, 4, 2, 10, 6]
'''
```

