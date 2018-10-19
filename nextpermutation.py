T = int(input())
for i in range(T):
    s = list(input())
    flag = 0
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            flag = 1
            break

    if flag == 0:
        print('no answer')
    else:
        max_i = 999  # choose some arbitrary high value
        for i in range(1, len(s)):
            if s[i - 1] < s[i]: max_i = i - 1
        if max_i == 999:
            print('no answer')
        else:
            max_j = 0
            for j in range(max_i + 1, len(s)):
                if s[j] > s[max_i]: max_j = j

            # swap
            temp = s[max_i]
            s[max_i] = s[max_j]
            s[max_j] = temp
            s = ''.join(s)
            print(s[:max_i + 1] + s[(max_i + 1):][::-1])