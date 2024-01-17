def plusMinus(arr):
    # Write your code here
    l = len(arr)
    pos = 0.0
    neg = 0.0
    zer = 0.0

    for num in arr:
        if num > 0:
                pos += 1
        elif num < 0:
                neg += 1
        else:
              zer += 1

    print(f"{pos/l:.6f}\n{neg/l:.6f}\n{zer/l:.6f}")