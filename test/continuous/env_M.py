"""
Author: RichardM
Date: 2023-12-14 18:07:55
LastEditors: RichardM
LastEditTime: 2023-12-14 18:41:28
Description: 

Copyright (c) 2023 by ${XJTU}, All Rights Reserved. 
"""
import gym
from gym import spaces
import numpy as np
from queue import Queue


class MyEnvironment(gym.Env):
    def __init__(self):
        super(MyEnvironment, self).__init__()

        # 定义观测空间
        self.state = np.random.rand()

        # 定义动作空间
        self.action_space = spaces.Box(low=-0.5, high=0.5, shape=(1,))

        # 记录当前回合的步数
        self.current_step = 0

        # 记录当前回合的奖励 是一个队列

        self.reward = Queue()

    def step(self, action):
        # 在这里实现环境的状态转移逻辑
        # 根据动作更新环境状态
        self.state += action + np.random.rand() * 0.2 - 0.3
        reward = (self.state - 0.5) ** 2
        # 计算奖励
        # 假设奖励在三个回合后才能体
        self.reward.put(reward)

        return self.state, self.reward.get(), done, info

    def reset(self):
        # 在每个回合开始时重置环境状态
        self.current_step = 0
        self.current_reward = 0
        for _ in range(3):
            self.current_reward.put(0)

    def render(self, mode="human"):
        # 在控制台上显示当前状态
        print("Current state:", self.state)

        # 返回初始观测
        return self.state
