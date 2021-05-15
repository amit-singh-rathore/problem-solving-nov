class Solution:
    def isNumber(self, s: str) -> bool:

        valid_patterns = ('xd','x.d','xd.','xd.d','xsd','xsd.','xsd.d',
                'xded','x.ded','xd.ed','xd.ded','xsded','xsd.ed','xsd.ded', 
                'xdesd','x.desd','xd.esd','xd.desd','xsdesd','xsd.esd','xsd.desd',
               'xs.d','xs.ed','xs.esd','xs.ded','xs.desd')
    
        patttern = 'x'
        for ch in s:
            if ch == '+' or ch == '-': patttern += 's'
            elif ch == 'e' or ch == 'E': patttern += 'e'
            elif ch.isdigit():
                if patttern[-1] != 'd': patttern += 'd'
            elif ch == '.': patttern += '.'
            else: return False
            
        return patttern in valid_patterns