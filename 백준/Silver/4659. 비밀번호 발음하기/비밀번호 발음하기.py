import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == "end":
        break

    is_v = False
    v_seq = 0
    c_seq = 0
    prev = ''
    is_pass = True
    
    for c in s:
        if prev == c and c not in 'eo':
            is_pass = False
            break

        if c in 'aeiou':
            is_v = True
            v_seq += 1
            c_seq = 0
        else:
            c_seq += 1
            v_seq = 0
        if v_seq == 3 or c_seq == 3:
            is_pass = False
            break

        prev = c
    if not is_v:
        is_pass = False

    if is_pass:
        print("<" + s + ">", "is acceptable.")
    else:
        print("<" + s + ">", "is not acceptable.")