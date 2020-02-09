package remove_dup

import (
	"testing"
	"github.com/josenava/katas/cracking_the_code_interview/chapter_2/linked_list"
)


func TestRemoveDups(t *testing.T) {
	l := linked_list.List{}
	l.AddElement(1)
	l.AddElement(2)
	l.AddElement(3)
	l.AddElement(3)
	l.AddElement(2)
	l.AddElement(1)
	l.AddElement(4)
	// originalList := l.AsString()
	// t.Log("original list", originalList)
    expectedList := "1->2->3->4->nil"

	list := RemoveDups(l)
	if list.AsString() != expectedList {
		t.Errorf("lists do not match %s != %s", l.AsString(), expectedList)
	}
}
