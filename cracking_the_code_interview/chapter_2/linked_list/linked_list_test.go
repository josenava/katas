package linked_list

import "testing"

func TestAddElement(t *testing.T) {
	list := List{}
	list.AddElement(4)

	if list.Head.Data != 4 {
		t.Errorf("%d, was not expected", list.Head.Data)
	}
}

func TestRemoveElement(t *testing.T) {
	list := List{}
	list.AddElement(1)
	list.AddElement(2)
	list.AddElement(3)
	list.RemoveElement(2)

	if list.Head.Next.Data == 2 {
		t.Errorf("%d element not expected" , list.Head.Next.Data)
	}
}
