class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        
        beg, end, res = 0, len(products) - 1, []

        for idx, char in enumerate(searchWord):
            while beg <= end and (len(products[beg]) <= idx or products[beg][idx] != char):
                beg += 1
                
            while beg <= end and (len(products[end]) <= idx or products[end][idx] != char):
                end -= 1
                
            res.append(products[beg:min(end+1, beg+3)])

        return res
    
    
        