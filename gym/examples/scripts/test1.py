import gym
env = gym.make('CartPole-v0')
# env = gym.make('MountainCar-v0')
# env = gym.make('MsPacman-v0')

# print(env.action_space)
# print(env.observation_space)
# print(env.reward_space)
print(env.observation_space.high)
print(env.observation_space.low)

for i_episode in range(5):
    observation = env.reset()
    reward_episode = 0
    for t in range(300):
        env.render()
        # print(observation)
        action = env.action_space.sample()
        # action = t % 2
        # action = 0
        observation, reward, done, info = env.step(action)
        # print(action, reward, observation, info)
        reward_episode += reward
        if done:
            print("Episode finished after {} timesteps. Reward: {}"
                .format(t+1, reward_episode))
            print("Observation: {}".format(observation))
            break
