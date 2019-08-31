# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 11:19:07 2018

无限网格上的机器人从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：

    -2：向左转 90 度
    -1：向右转 90 度
    1 <= x <= 9：向前移动 x 个单位长度

有一些网格方块被视作障碍物。 

第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])

如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。

返回从原点到机器人的最大欧式距离的平方。

 

示例 1：

输入: commands = [4,-1,3], obstacles = []
输出: 25
解释: 机器人将会到达 (3, 4)

示例 2：

输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
输出: 65
解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处

@author: liyang
"""

class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x, y = 0, 0              #初始坐标为（0，0）
        obs = set([])            #声明一个障碍的集合
        for ox, oy in obstacles: #加上绕过障碍物的步数
            obs.add((ox, oy))
        mxd = 0
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        curdir = 0
        for c in commands:       #命令走过的长度
            while c > 0:
                nx, ny = x + dirs[curdir][0], y + dirs[curdir][1]
                if (nx, ny) in obs:
                    c = 0
                else:
                    x, y = nx, ny
                    c -= 1
            mxd = max(mxd, x**2 + y**2)   #欧式距离的平方就是勾股定理
            if c == -2:
                curdir = (curdir + 1) % 4
            elif c == -1:
                curdir = (curdir + 3) % 4
        return mxd
a=Solution()
print(a.robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4]]))
#输入参数是指令和障碍物的坐标