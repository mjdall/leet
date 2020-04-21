def middle_node(head):
        """
        Returns the middle of a linked list.
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            
        return slow
