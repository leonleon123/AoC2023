from re import findall

def get_number(line, match_words):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    res = findall(f"(?=([0-9]|{'|'.join(digits)}))" if match_words else '[0-9]', line)
    return int(''.join(str(digits.index(num) + 1) if num in digits else num for num in [res[0], res[-1]]))

print(*[sum(get_number(line, match_words) for line in open('01.txt').readlines()) for match_words in [False, True]], sep='\n')
