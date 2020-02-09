package linked_list

import "testing"

func TestAddElement(t *testing.T) {
	list := List{}
	list.AddElement(4)

	if list.head.data != 4 {
		t.Errorf("%d, was not expected", list.head.data)
	}
}

func TestRemoveElement(t *testing.T) {
	list := List{}
	list.AddElement(1)
	list.AddElement(2)
	list.AddElement(3)
	list.RemoveElement(2)

	if list.head.next.data == 2 {
		t.Errorf("%d element not expected" , list.head.next.data)
	}
}
