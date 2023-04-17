# python3

def read_input():
    input_type = input().strip().upper()

    if input_type == 'I':
        text = input().rstrip()
        pattern = input().rstrip()
        return text, pattern
    elif input_type == 'F':
        file_path = input().strip()
        with open(file_path, 'r') as file:
            contents = file.read().rstrip()
            text, pattern = contents.split('\n')
            return text, pattern
    else:
        print("Invalid input type.")
        return None, None

def print_occurrences(output):
    if not output:
        print("No occurrences found.")
    else:
        print(' '.join(str(pos) for pos in output))

def rabin_karp_algorithm(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    prime = 101
    mod = int(1e9 + 7)

    if p_len > t_len:
        return []

    pattern_hash = 0
    text_hash = 0
    power = 1

    for i in range(p_len):
        pattern_hash = (pattern_hash * prime + ord(pattern[i])) % mod
        text_hash = (text_hash * prime + ord(text[i])) % mod
        if i < p_len - 1:
            power = (power * prime) % mod

    positions = []

    for i in range(t_len - p_len + 1):
        if pattern_hash == text_hash:
            if text[i:i + p_len] == pattern:
                positions.append(i)

        if i < t_len - p_len:
            text_hash = (text_hash - (ord(text[i]) * power)) % mod
            text_hash = (text_hash * prime + ord(text[i + p_len])) % mod

    return positions

def get_occurrences(pattern, text):
    if pattern is None or text is None:
        return []

    occurrences = rabin_karp_algorithm(pattern, text)
    if not occurrences:
        return []
    else:
        return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
