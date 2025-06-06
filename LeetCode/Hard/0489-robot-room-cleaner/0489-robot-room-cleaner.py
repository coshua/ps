# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        dirs = 0
        r = c = 0
        dlst = [[-1, 0], [0, 1], [1,0], [0,-1]]
        v = set() # (r, c)

        def dfs(r, c, d):
            robot.clean()
            back_r, back_c = r + dlst[(d+2)%4][0], c + dlst[(d+2)%4][1]
            for_r, for_c = r + dlst[d][0], c + dlst[d][1]
            left_r, left_c = r + dlst[(d-1) % 4][0], c + dlst[(d-1)%4][1]
            right_r, right_c = r + dlst[(d+1) % 4][0], c + dlst[(d+1) % 4][1]
            if (for_r,for_c) not in v and robot.move():
                v.add((for_r,for_c))
                dfs(for_r, for_c, d)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnRight()
                robot.turnRight()
            if (left_r, left_c) not in v:
                robot.turnLeft()
                v.add((left_r,left_c))
                moved = robot.move()
                if moved:
                    dfs(left_r,left_c,(d-1)%4)
                robot.turnRight()
                if moved:
                    robot.turnRight()
                    robot.move()
                    robot.turnLeft()
            if (right_r, right_c) not in v:
                robot.turnRight()
                v.add((right_r,right_c))
                moved = robot.move()
                if moved:
                    dfs(right_r,right_c,(d+1)%4)
                robot.turnLeft()
                if moved:
                    robot.turnLeft()
                    robot.move()
                    robot.turnRight()
            if (back_r, back_c) not in v:
                v.add((back_r,back_c))
                robot.turnRight()
                robot.turnRight()
                moved = robot.move()
                if moved:
                    dfs(back_r, back_c, (d+2)%4)
                robot.turnRight()
                robot.turnRight()
                if moved:
                    robot.move()
        v.add((0, 0))
        dfs(0,0,0)
            
            
