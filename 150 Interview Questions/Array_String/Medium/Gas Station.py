class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        total_gas = 0
        curr_gas = 0
        start_index = 0
        for i in range(n):
            total_gas += gas[i] - cost[i]
            curr_gas += gas[i] - cost[i]
            if curr_gas < 0:
                curr_gas = 0
                start_index = i + 1
        return start_index if total_gas >= 0 else -1
