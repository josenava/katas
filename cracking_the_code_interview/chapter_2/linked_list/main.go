package main

import "fmt"

type Node struct {
    next *Node
    data int8
}

func (n Node) Show() {
    fmt.Printf("->%d", n.data)
}

type List struct {
    head *Node
}

type LinkedList interface {
    AddElement(i int8)
    RemoveElement(i int8)
    Show()
}

func (l *List) AddElement(i int8) {
    node := Node{nil, i}
    node.next = l.head
    l.head = &node
}

func (l *List) RemoveElement(i int8) {
    for l.head.data == i {
        l.head = l.head.next
    }
    runner := l.head
    laux := l.head
    for runner != nil {
       if runner.data == i {
           laux.next = runner.next
           runner = runner.next
       } else {
           laux = runner
           runner = runner.next
       }
    }
}

func (l List) Show() {
    for l.head != nil {
        l.head.Show()
        l.head = l.head.next
    }
}

func main() {
    l := List{}
    l.AddElement(7)
    l.AddElement(15)
    l.AddElement(7)
    l.AddElement(102)
    l.AddElement(7)
    l.RemoveElement(7)
    l.Show()
}
