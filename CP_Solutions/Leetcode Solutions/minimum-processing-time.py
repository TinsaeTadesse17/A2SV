class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        j,li=0,[]
        processorTime.sort()
        tasks.sort(reverse=True)
        for i in range(len(processorTime)):
            li.append(processorTime[i]+tasks[j])
            j+=4
        return max(li)