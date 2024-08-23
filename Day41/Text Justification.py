class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        n = len(words)
        line, length, res, i = [], 0, [], 0
    
        while(i < n):

            if length + len(words[i]) + len(line) > maxWidth:
                extra_spaces = maxWidth - length
                spaces = extra_spaces // max(1,len(line) - 1)
                remainder = extra_spaces % max(1,len(line) - 1)
                if len(line) == 1:
                    s = maxWidth - len(line[0])
                    res.append(line[0] + " "*s)
                else:
                    for j in range(len(line) - 1):
                        line[j] = line[j] + " " * spaces
                        if remainder:
                            line[j] += " "
                            remainder -= 1
                    res.append("".join(line))
                line, length = [], 0
                    
            line.append(words[i])
            length += len(words[i])
            i += 1
        
        last_line = " ".join(line)
        spaces = maxWidth - len(last_line)
        last_line += " "*spaces
        res.append(last_line)

        return res
