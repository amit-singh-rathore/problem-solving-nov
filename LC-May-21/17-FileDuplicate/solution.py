class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for item in paths:
            details = item.split(" ")
            pref = details[0]+'/'
            for detail in details[1:]:
                l = len(detail)
                idx = detail.find('(')
                if idx>0:
                    key = detail[idx+1:l-1]
                    mapping[key].append("".join([pref,  detail[:idx]]))

        return [value for value in mapping.values() if len(value)>1]
        