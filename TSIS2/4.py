class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mylist =[0]
        counter = 0
        for i in range(len(gain)):
            counter = counter + gain[i]
            mylist.append(counter)
        return (max(mylist))  