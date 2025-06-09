class Solution:
    def decodeString(self, s: str) -> str:
        
        # 
        def rec(idx):
            dec = []
            n = []
            while idx < len(s) and s[idx] != ']':
                if s[idx].isalpha():
                    dec.append(s[idx])
                    idx += 1
                elif s[idx].isdigit():
                    n.append(s[idx])
                    idx += 1
                elif s[idx] == '[':
                    idx, subdec = rec(idx + 1)
                    dec += [subdec] * int(''.join(n))
                    n = []
            return idx + 1, ''.join(dec)
        
        _, ans = rec(0)
        return ans