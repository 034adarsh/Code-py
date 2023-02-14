def solve(puzzle):
    # Function to check if the puzzle is solved
    def is_solved(puzzle):
        send = puzzle[0] * 10 + puzzle[1]
        more = puzzle[2] * 10 + puzzle[3]
        money = puzzle[4] * 100 + puzzle[5] * 10 + puzzle[6]
        return send + more == money

    # Function to assign values to the letters
    def assign_values(puzzle, index):
        if index == len(puzzle):
            return is_solved(puzzle)
        for i in range(10):
            puzzle[index] = i
            if assign_values(puzzle, index + 1):
                return True
        return False

    puzzle = [None] * 7
    puzzle[0] = puzzle[2] = puzzle[4] = 1
    if assign_values(puzzle, 1):
        print(puzzle)
    else:
        print("No solution found")

solve("SENDMONEY")

def isSolvable(words, result):
    mp = [-1]*(26)
 
    Hash = [0]*(26)
 
    CharAtfront = [0]*(26)
 
    uniq = ""
 
    for word in range(len(words)):
        
        for i in range(len(words[word])):
           
            ch = words[word][i]
            Hash[ord(ch) - ord('A')] += pow(10, len(words[word]) - i - 1)
 
            if mp[ord(ch) - ord('A')] == -1:
                mp[ord(ch) - ord('A')] = 0
                uniq += str(ch)
 
            if i == 0 and len(words[word]) > 1:
                CharAtfront[ord(ch) - ord('A')] = 1
 
    for i in range(len(result)):
        ch = result[i]
 
        Hash[ord(ch) - ord('A')] -= pow(10, len(result) - i - 1)
 
        if mp[ord(ch) - ord('A')] == -1:
            mp[ord(ch) - ord('A')] = 0
            uniq += str(ch)
 
        if i == 0 and len(result) > 1:
            CharAtfront[ord(ch) - ord('A')] = 1
 
    mp = [-1]*(26)
 
    return True
 
arr = list(input("Enter string: ").split())
S = input("Enter second string: ")
 
if isSolvable(arr, S):
    print("Yes")
else:
    print("No")
