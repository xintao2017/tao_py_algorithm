#!/usr/bin/python

#A list implementation

class Node(object):

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def hasNext(self):
        if self.next is None:
            return True
        else:
            return False


class EmptyListException(Exception):
    pass

class IndexOutOfBound(Exception):
    pass


class Linkedlist(object):

    def __init__(self, head = None):
        self.head = head
        self.curr = head
        if head is not None:
            self.curr.next = None


    ## __len__()
    def __len__(self):
        counter = 0
        while self.curr.hasNext():
            self.curr = self.curr.next
            counter += 1
        return counter

    def add(self, node):
        if self.head is None:
            self.head = node
            self.curr = node
        else:
            self.curr.next = node
            self.curr = node

    ## __str__()
    def __str__(self):
        strx = ""
        node = None
        while self.curr.next is not None:
            strx += self.curr.data + ' '
        return f"[{strx}]"

    ## append ()
    def append(self, node):
        self.curr.next = node
        self.curr = node
        self.curr.next = None

    ## get()
    def get(self, index):
        if self.head is None:
            raise EmptyListException()
        if self.__len__ < index:
            raise IndexOutOfBound()
        node = self.head
        i = 0
        while node.hasNext():
            if i == index:
                return node.data
            else:
                node = node.next
                i += 1


    ## delete()
    def delete(self, index):
        if self.head is None:
            raise EmptyListException()
        if self.__len__ < index:
            raise IndexOutOfBound()
        node = self.head
        pre_node = self.head
        i = 0

        while node.hasNext():
            if i == index:
                return pre_node.next = node
            else:
                pre_node = node
                node = node.next
                i += 1

    ## pop()
    def pop(self):
        if self.__len__() < 1
            raise EmptyListException()
        else:
            h = self.head
            self.head = self.head.next
        return h
