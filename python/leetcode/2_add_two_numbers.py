# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
        
#         # l1.reverse()
#         # l1_reverse = int("".join(str(element) for element in l1))
        
#         # l2.reverse()
#         # l2_reverse = int("".join(str(element) for element in l2))

#         # print(l1_reverse)

#         # l_sum = l1_reverse + l2_reverse

#         # relult_list = str(l_sum).split()

#         # relult_list.reverse()
        
#         sum=0
#         i=0
#         count_err = 0

#         while count_err < 2:
#             count_err = 0
#             factor = int("1"+"0"*i)
#             # print(s)
#             # print(l1[(i+1)*-1])
#             # print(l2[(i+1)*-1])
            
#             factor_l1 = 0
#             factor_l2 = 0


#             try:
#                 factor_l1 = l1[(i+1)*-1]
#             except:
#                 count_err+=1

#             try:
#                 factor_l2 = l2[(i+1)*-1]
#             except:
#                 count_err+=1

#             sum += (factor_l1+factor_l2)*factor

#             print(count_err)
#             print("*"*10)
            
#             i+=1

#         print(str(sum)[::-1])

#         relult_list=(str(sum)[::-1]).split()

#         return relult_list
        
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        currrent_val_l1 = l1
        currrent_val_l2 = l2
                
        sum=0
        i=0
        count_err = 0

        while count_err < 2:
            count_err = 0
            factor = int("1"+"0"*i)
            
            factor_l1 = 0
            factor_l2 = 0

            if (currrent_val_l1):
                factor_l1 = currrent_val_l1.val
                currrent_val_l1=currrent_val_l1.next
            else:
                count_err+=1

            if (currrent_val_l2):
                factor_l2 = currrent_val_l2.val
                currrent_val_l2=currrent_val_l2.next
            else:
                count_err+=1

            sum += (factor_l1+factor_l2)*factor
            
            i+=1
        
        result_str = str(sum)

        prev_node = None

        for ch in result_str:
            prev_node = ListNode(int(ch), prev_node)

        return prev_node
        
l1 = None

for el in [2,4,3]:
    l1 = ListNode(el,l1)

l2 = None

for el in [5,6,4]:
    l2 = ListNode(el,l2)

main_solution = Solution()

def list_node2list(node:ListNode):
    current_node = node
    result_list=[]
    while current_node:
        result_list.append(current_node.val)
        current_node=current_node.next
    return result_list

# print([x for x in main_solution.addTwoNumbers(l1,l2)])
print(list_node2list(main_solution.addTwoNumbers(l1,l2)))