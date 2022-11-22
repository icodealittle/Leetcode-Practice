'''s = s.lower()
        result = []
        # output = [data[i:i + k] for i in range(0, len(s), k)]
        for i in reversed(range(len(s))):
            if s[i] == '-':
                continue
            if len(result) % (k + 1) == k:
                result += '-'
            result += s[i].upper()
        return "".join(reversed(result))'''
