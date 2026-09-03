class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        input: tasks[str], n: int
        output: num

        edge: tasks is empty, one task, n = 0, 1


        plan:
        make a counter to get all freqs
        get the max freq
        count how many keys have the max freq
        calculate grouped length using, (max_freq - 1) * (n + 1) + num_max_freq

        return max between len and grouped
        '''
        from collections import Counter
        count = Counter(tasks)
        max_freq = max(count.values())

        num_max_freq = sum(1 for v in count.values() if v == max_freq)

        grouped_length = (max_freq - 1) * (n + 1) + num_max_freq


        return max(len(tasks), grouped_length)
        