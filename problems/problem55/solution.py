def groupAnagrams(strs):
    
    ana_map = {}
    for word in strs:
        gp_key = "".join(sorted(word))
        if gp_key in ana_map:
            ana_map[gp_key].append(word)
        else:
            ana_map[gp_key] = [word]
        

    ana_gp = [anagram for anagram in ana_map.values()] 
    return ana_gp
    
def groupAnagrams(strs):
    result = defaultdict(list)
    
    for word in strs:
        result[tuple(sorted(word))].append(word)
        
    return result.values()