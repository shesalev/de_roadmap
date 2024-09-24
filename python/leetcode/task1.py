class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <=0:
            return False

        s = str(x)

        if len(s)==1:
            return True
        
        l = 0

        if x % 2 == 0:
            l = int(len(s)/2)
        else:
            l = int((len(s)-1)/2)

        for i in range(l-1):
            print(f"{s[i]} | {s[-(i+1)]}")
            # if(s[i]!=s[-(i+1)]):
            #     return False

        # print(int(len(s)/2))
        # print(range(0,l))

        return True

ss = Solution()        

print(f"Result: {ss.isPalindrome(1231)}")
