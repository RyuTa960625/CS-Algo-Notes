L, C = map(int, input().split())

alphabets = sorted(input().split())


def dfs(idx, codes):
    if L == idx:
        vowel_count = 0
        consonant_count = 0

        for code in codes:
            if code in "aeiou":
                consonant_count += 1
            else:
                vowel_count += 1

        if consonant_count >= 1 and vowel_count >= 2:
            print("".join(codes))

    else:
        for i in range(idx, C):
            if codes and alphabets[i] <= codes[-1]:
                continue
            dfs(idx + 1, codes + [alphabets[i]])


dfs(0, [])