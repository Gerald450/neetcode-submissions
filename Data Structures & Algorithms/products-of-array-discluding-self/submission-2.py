class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        input: array of nums
        output: array of products except nums[curr_i]

        edge case: negative nums, empty

        plan:
            create two arr, post products, pre products
            postarr{
                multiply all nums after curr_i and save at curr_i
                will go reverse
            }
            prearr{
                multiply all nums before curr_i and save at curr_i
            }

            otparr{
                multiply both arr
            }

            return otparr


        [48, 24, 6, 1]
        [1, ,1 ,1 ,1]
        '''
        postarr = [1] * len(nums)
        prearr = [1] * len(nums)
        otparr = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            postarr[i] = postarr[i + 1] * nums[i + 1]

        for i in range(1, len(nums)):
            prearr[i] = nums[i - 1] * prearr[i - 1]

        for i in range(len(otparr)):
            otparr[i] = prearr[i] * postarr[i]
        print(prearr, postarr, otparr)

        return otparr


    '''
        post = [1, 1, 1, 1]
        pre = [1, 1, 1, 1]
        otp = [1, 1, 1, 1]

        i -> 1, 4
        pre[1] = nums[0] * pre[0]
        1 * 1 = 1
        pre = [1, 1, 1, 1]

        1 -> 2, 4
        pre[2] = nums[1] * pre[1]
        2 * 1 = 2
        pre = [1, 1, 2, 1]

        1 -> 3, 4
        pre[3] = nums[2] * pre[2]
        4 * 2 = 8
        pre = [1, 1, 2, 8]




        i -> 2, -1
        post[2] = nums[3] * post[3]
        6 * 1 = 6
        post = [1, 1, 6, 1]

        i -> 1, -1
        post[1] = nums[2] * post[2]
        4 * 6 = 24
        post = [1, 24, 6, 1]

        i -> 0, -1
        post[0] = nums[1] * post[1]
        2 * 24 = 48
        post = [48, 24, 6, 1]

    '''




    