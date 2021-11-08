package remove_dup

import "github.com/josenava/katas/cracking_the_code_interview/chapter_2/linked_list"


func RemoveDups(l linked_list.List) linked_list.List {
    visited := make(map[int8]bool)
    nodupList := linked_list.List{}

    for l.Head != nil {
        if !visited[l.Head.Data] {
            visited[l.Head.Data] = true
            nodupList.AddElement(l.Head.Data)
        }
        l.Head = l.Head.Next
    }
    return nodupList
}
