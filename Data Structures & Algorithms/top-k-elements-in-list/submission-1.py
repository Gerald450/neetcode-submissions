class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dictionary to hold the freq
        nums_d = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            nums_d[num] = 1 + nums_d.get(num, 0)

        for key, value in nums_d.items():
            bucket[value].append(key)
           

        otp = []
        for i in bucket[::-1]:
            if len(otp) == k:
                break

            if not i:
                continue
            for y in i:
                otp.append(y)


        print(nums_d)
        print(bucket)
        return otp
            
        

        

        
                
