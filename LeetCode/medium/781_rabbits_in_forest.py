class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        answers.sort()
        nums_total = 0
        nums_cur_color = 0
        prev_color = -1
        for i in range(len(answers)):
            if answers[i] == prev_color:
                if nums_cur_color == answers[i] + 1:
                    nums_total += answers[i] + 1
                    nums_cur_color = 0
                nums_cur_color += 1
            if answers[i] != prev_color:
                nums_total += prev_color + 1
                prev_color = answers[i]
                nums_cur_color = 1
        nums_total += answers[-1] + 1

        return nums_total