"""
dice_sum:
    Return the combination of n dice values that output a desired sum
"""
def dice_sum(n_dice: int, desired_sum: int) -> list[int]:
    def backtrack(n: int, total: int, values: list[int]):
        if n == 0:
            if total == 0:
                print(values)
            return
        if total >= n * 1 and total <=n * 6:
            for i in range(1, 7):
                # choose
                values.append(i)
                # explore
                backtrack(n-1, total-i, values)
                # un-choose
                values.pop()

    values = []
    backtrack(n_dice, desired_sum, values)


"""
permutations:
    given a string, output all possible combinations without repeating any value
    permutations("abc") -> [["a", "b", "c"], ["a", "c", "b"], ..]
"""
def permutations(s: str) -> set[str]:
    def backtrack(s: list[str], chosen: list[str], result: set[list[str]]):
        if not s:
            word = "".join(chosen)
            if word not in result:
                result.add(word)
                print(word)
            return
        for i in range(len(s)):
            c = s.pop(i)
            chosen.append(c)

            backtrack(s, chosen, result)

            chosen.pop()
            s.insert(i, c)

    result = set()
    backtrack(list(s), [], result)

    return result


if __name__ == "__main__":
    dice_sum(3, 7)
    permutations("jose")
