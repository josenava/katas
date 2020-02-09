package linked_list

import (
	"fmt"
	"strings"
)

type Node struct {
	Next *Node
	Data int8
}

func (n Node) Show() {
	fmt.Printf("->%d", n.Data)
}

func (n Node) AsString() string {
	return fmt.Sprintf("%d", n.Data)
}

type List struct {
	Head *Node
}

type LinkedList interface {
	AddElement(i int8)
	RemoveElement(i int8)
	RemoveAllOcurrencesOfElement(i int8)
	AsString() string
	Show()
}

func (l *List) AddElement(i int8) {
	node := Node{nil, i}
	if l.Head != nil {
		runner := l.Head
		for runner.Next != nil {
			runner = runner.Next
		}
		runner.Next = &node
	} else {
		node.Next = l.Head
		l.Head = &node
	}
}

func (l *List) RemoveElement(i int8) {
	runner := l.Head
	aux := l.Head

	for runner.Next != nil {
		if runner.Data == i {
			aux.Next = runner.Next
			break
		}
		aux = runner
		runner = runner.Next
	}
}

func (l *List) RemoveAllOcurrencesOfElement(i int8) {
	for l.Head.Data == i {
		l.Head = l.Head.Next
	}
	runner := l.Head
	laux := l.Head
	for runner != nil {
		if runner.Data == i {
			laux.Next = runner.Next
			runner = runner.Next
		} else {
			laux = runner
			runner = runner.Next
		}
	}
}

func (l List) AsString() string {
	var listStr strings.Builder
	for l.Head != nil {
		listStr.WriteString(fmt.Sprintf("%s->", l.Head.AsString()))
		l.Head = l.Head.Next
	}
	listStr.WriteString("nil")

	return listStr.String()
}

func (l List) Show() {
	fmt.Print(l.AsString())
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
