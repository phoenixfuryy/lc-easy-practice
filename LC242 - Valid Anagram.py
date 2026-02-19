class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s_list = list(s)
        # # print("true s_list is:", s_list)
        # t_list = list(t)
        # # print("true t_list is:", t_list)
        # if len(s_list) == len(t_list):
        #     for el in s_list:
        #         if(el in t_list):
        #             t_list.remove(el)
        #             if len(t_list)==0:
        #                 print("True")
        #         else:
        #             print("False") 

        s_dict = {}
        t_dict= {}
        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1
            print(s_dict[i])
            print(s_dict)
        for i in t: 
            if i not in s_dict:
                print("False")
            else:
                s_dict[i] -= 1
                       


        
s1 = Solution()
s1.isAnagram("anagram", "nagaram")