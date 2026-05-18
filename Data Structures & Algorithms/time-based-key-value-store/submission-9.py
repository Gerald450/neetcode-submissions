class TimeMap:

    '''
    input: set(key, val and timestamp)
    output: get(key, timestamp_prev <= timestamp)

    edge: duplicate timestamps, going down stamps

    plan:
    alice: {1: happy, 3:sad}
    find num == timestamp or just below
    traverse in timestamp dict
    if find higher return prev
    {key:{}}


    hint: key: [(timestamp, value)]
    store sorted
    do binary

    optimized plan:
    set: insertion sort
    get: do binary search, return l

    '''
    from collections import defaultdict
    def __init__(self):
        self.hashmap = defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        
        self.hashmap[key].append((timestamp, value))
        

    
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashmap:
            #binary search
            l, r = 0, len(self.hashmap[key]) - 1
            output = ''
            while l <= r:
                mid = (l + r) // 2
                num, val = self.hashmap[key][mid]

                if num > timestamp:
                    r = mid - 1
                elif num < timestamp:
                    output = val
                    l = mid + 1
                else:
                    return self.hashmap[key][mid][1]

            return output

        else:
            return ''


        '''
        [10, 11, 13]
        l = 10, r = 10


        [1, 4]
        get 5
        l = 1, r = 4,  m = 1

        l = 4, r = 4, m = 1
        '''
        






        
