package linked_list

import (
	"fmt"
	"strings"
)

type Node struct {
    next *Node
    data int8
}

func (n Node) Show() {
    fmt.Printf("->%d", n.data)
}

func (n Node) asString() string {
	return fmt.Sprintf("%d", n.data)
}

type List struct {
    head *Node
}

type LinkedList interface {
    AddElement(i int8)
    RemoveElement(i int8)
    RemoveAllOcurrencesOfElement(i int8)
	asString() string
    Show()
}

func (l *List) AddElement(i int8) {
    node := Node{nil, i}
    node.next = l.head
    l.head = &node
}

func (l *List) RemoveElement(i int8) {
    runner := l.head
    aux := l.head

    for runner.next != nil {
        if runner.data == i {
            aux.next = runner.next
            break
        }
        aux = runner
        runner = runner.next
    }
}

func (l *List) RemoveAllOcurrencesOfElement(i int8) {
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

func (l List) asString() string {
	var listStr strings.Builder
	for l.head != nil {
		listStr.WriteString(fmt.Sprintf("%s->", l.head.asString()))
	}
	listStr.WriteString("nil")

	return listStr.String()
}

func (l List) Show() {
	fmt.Print(l.asString())
}

// func main() {
//     l := List{}
//     l.AddElement(7)
//     l.AddElement(15)
//     l.AddElement(7)
//     l.AddElement(102)
//     l.AddElement(7)
//     l.RemoveAllOcurrencesOfElement(7)
//     l.Show()
// }
