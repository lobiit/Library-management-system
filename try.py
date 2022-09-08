x = 'wewewe'
a = list(x)
y = len(a)
z = 0

while z != y:
    print(a[z:y])
    a.pop()



class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow