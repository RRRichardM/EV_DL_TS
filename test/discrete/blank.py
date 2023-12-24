"""
Author: RichardM
Date: 2023-12-14 20:19:59
LastEditors: RichardM
LastEditTime: 2023-12-14 20:22:23
Description: 

Copyright (c) 2023 by ${XJTU}, All Rights Reserved. 
"""
from env_M import MyEnvironment
from stable_baselines3.common.env_checker import check_env
from cartpole import CartPoleEnv

env = MyEnvironment()
# env = CartPoleEnv()
# It will check your custom environment and output additional warnings if needed
check_env(env)
