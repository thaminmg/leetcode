class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        groups = defaultdict(list)

        for index, value in enumerate(groupSizes):
            groups[value].append(index)
            if len(groups[value]) == value:
                result.append(groups.pop(value))
        return result
        