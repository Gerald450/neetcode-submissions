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
    '''
    from collections import defaultdict
    def __init__(self):
        self.hashmap = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].update({timestamp: value})
        
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashmap:
            if timestamp in self.hashmap[key]:
                return self.hashmap[key][timestamp]

            key_list = list(self.hashmap[key])
            

            l, r = min(key_list), timestamp
            output = ''
            for i in range(l, r):
                if i in self.hashmap[key]:
                    output = self.hashmap[key][i]
            
            return output
        else:
            return ''
            
          

    
    
    
    '''
    timeMap.set("alice", "happy", 1)
    {alice: {1: happy}}

    timeMap.get("alice", 1); 
    returns happy

    timeMap.get("alice", 2);
    output = 1
    {1: happy}
    output = 1
    return happy


    {key1: {10: value1}}
    '''






        
