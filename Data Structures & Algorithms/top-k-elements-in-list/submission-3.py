class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create dictionary
        #create buckets
        #put index == value

        nums_d = {}
        otp = []

        for num in nums:
            nums_d[num] = 1 + nums_d.get(num,0)
        
        bucket = [[] for _ in range(len(nums))]
        print(bucket)
        for key, value in nums_d.items():
            bucket[value - 1].append(key)
        
        print(bucket)
        
        for i in reversed(range(len(nums))):

            if len(otp) == k:
                break
            
            for numb in bucket[i]:
                otp.append(numb)
  
        return otp
            




        