from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.storage = dict()
        self.order = DoublyLinkedList()
        self.size = 0
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):

        # Check and see if key is in cache
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return

        # If it is in the cache move to front and update value
        if self.size == self.limit:
            del self.storage[self.order.head.value[0]]
            self.order.remove_from_head()
            self.size += 1

        # If not add to the front of the cache
        # Defining tail as most recent and head as oldest
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1

        # if self.count >= self.limit:
        #     if key not in self.container:
        #         self.list.add_to_tail([key, value])
        #         self.container[key] = self.list.tail
        #         # needed to remove the head
        #     else:
        #         self.list.remove_from_head()
        #         self.container.pop(key)
        #         self.list.add_to_tail([key, value])
        #         self.container[key] = self.list.tail

        # elif self.count == 0:
        #     if key not in self.container:
        #         self.count += 1
        #     self.list.add_to_head([key, value])
        #     self.container[key] = self.list.tail

        # else:
        #     if key not in self.container:
        #         self.count += 1
        #     self.list.add_to_tail([key, value])
        #     self.container[key] = self.list.tail


# myList = LRUCache()
# myList.set(1, 1)
# myList.set(2, 2)
# myList.set(3, 3)
# myList.set(4, 4)
# myList.set(5, 5)
# myList.set(6, 6)
# myList.set(7, 7)
# myList.set(8, 8)
# myList.set(9, 9)
# myList.set(10, 10)
# myList.set(5, 55)

# print(myList.get(9))


# temp = myList.list.head
# while(temp):
#     print(temp.value)
#     temp = temp.next

# print(myList.container)
# print(myList.count)
