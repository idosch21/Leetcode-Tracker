class Solution:
    def compress(self, chars: List[str]) -> int:

        if not chars:
            return []
        write = 0
        count = 0
        
        for read in range(len(chars)):
            
            count += 1
            if read == len(chars) - 1 or chars[read] != chars[read+1]:
                #we need to write
                chars[write] = chars[read]
                write += 1
                if count > 1:
                    for number in str(count):
                        chars[write] = number
                        write += 1
                count = 0
        return write