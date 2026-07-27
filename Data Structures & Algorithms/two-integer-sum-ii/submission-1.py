class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        output=[]
        while left<=right :
           # print(left)
           # print(right)
            if  numbers[left]+numbers[right]==target:
                #print([numbers[left],numbers[right]])
                output.append(left+1)
                output.append(right+1)
                return output
            elif numbers[left]+numbers[right]>target:
               # print([numbers[left],numbers[right]])
                right=right-1
            else:
                left=left+1
             #   print([numbers[left],numbers[right]])
        return output                
