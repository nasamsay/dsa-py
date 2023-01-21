from hashlib import new
from traceback import print_list


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
#print
  def print_list(self):
    cur_node = self.head
    while cur_node:
        print(cur_node.data)
        cur_node = cur_node.next
#append
  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
        last_node = last_node.next
    last_node.next = new_node
#prepend
  def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
#insert node at a given pos
  def insert(self, prev_node, data):
    if not prev_node:
        print("The previous Node doesnt exist")
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node
#deleting by key
  def delete_by_key(self, key):
    cur_node = self.head
    if cur_node and cur_node.data == key:
        self.head = cur_node.next
        cur_node = None
        return
    prev = None
    while cur_node and cur_node.data != key:
        prev = cur_node
        cur_node = cur_node.next
    if cur_node is None:
        return
    prev.next = cur_node.next
    cur_node = None
#deleting by position
  def delete_by_pos(self, pos):
    if self.head:
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
        
        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None
#length iteratively
  def len_iterative(self):
    count = 0 
    cur_node = self.head
    while cur_node:
        count += 1
        cur_node = cur_node.next
    return count
#length recursively
  def len_recursive(self, node):
    if node is None:
        return 0
    return 1 + self.len_recursive(node.next)
  #node swap
  def node_swap(self, key_1, key_2):
    if key_1 == key_2:
      return
    prev_1 = None
    curr_1 = self.head
    while curr_1 and curr_1.data != key_1:
      prev_1 = curr_1
      curr_1 = curr_1.next
    prev_2 = None 
    curr_2 = self.head 
    while curr_2 and curr_2.data != key_2:
      prev_2 = curr_2 
      curr_2 = curr_2.next
    
    if not curr_1 and not curr_2:
      return
    if prev_1:
      prev_1.next = curr_2
    else:
      self.head = curr_2
    
    if prev_2:
      prev_2.next = curr_1
    else:
      self.head = curr_1

    curr_1.next, curr_2.next = curr_2.next, curr_1.next
  #reverse iteratively
  def reverse_iterative(self):
    prev = None
    cur = self.head
    while cur:
      nxt = cur.next
      cur.next = prev
      prev = cur
      cur = nxt
    self.head = prev
  #reverse recursively
  def reverse_recursive(self):
    def _rev_recursive(cur, prev):
      if not cur:
        return prev
      nxt = cur.next
      cur.next = prev
      prev = cur
      cur = nxt
      return _rev_recursive(cur, prev)
    self.head = _rev_recursive(cur=self.head, prev = None)
  #merge two sorted lists
  def merge_sorted(self, llist):

    p = self.head
    q = llist.head
    s = None

    if not p:
      return q
    if not q:
      return p
    
    if p and q:
      if p.data <= q.data:
        s = p
        p = s.next
      else:
        s = q
        q = s.next
      new_head = s

    while p and q:
      if p.data <= q.data:
        s.next = p
        s = p
        p = s.next
      else:
        s.next = q
        s = q
        q = s.next
      if not p:
        s.next = q
      if not q:
        s.next = p

    self.head = new_head
    return self.head

llist = LinkedList()
print("The length of an empty linked list is:")
print(llist.len_recursive(llist.head))
print("\n")
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("G")
llist.append("H")
llist.prepend("E")
llist.insert(llist.head.next.next, "F")
llist.print_list()
print("------------------------------")
llist.delete_by_key("C")
llist.delete_by_pos(5)
llist.print_list()
print("\n")
print("The length of the linkedlist iteratively:")
print(llist.len_iterative())
print("\n")
print("The length of the linkedlist recursively:")
print(llist.len_recursive(llist.head))
llist.node_swap("F", "H")
llist.print_list()
print('------------')
llist.reverse_iterative()
llist.print_list()
print("-----------")
llist.reverse_recursive()
llist.print_list()
print('\n')
#merge sorted test
llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()