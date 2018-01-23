import gym

def get_action(env, observation):
    action = env.action_space.sample()
    # action = t % 2
    # action = 0

    return action

def main():
    env = gym.make('CartPole-v0')
    # env = gym.make('MountainCar-v0')
    # env = gym.make('MsPacman-v0')

    # print(env.action_space)
    # print(env.observation_space)
    # print(env.reward_space)
    print(env.observation_space.high)
    print(env.observation_space.low)

    reward_average = 0
    for i_episode in range(10):
        observation = env.reset()
        # print(observation)

        reward_episode = 0
        for t in range(200):
            env.render()

            action = get_action(env, observation)
            observation, reward, done, info = env.step(action)
            # print(action, reward, observation, info)

            reward_episode += reward
            if done:
                print("Episode finished after {} timesteps. Reward: {}"
                    .format(t+1, reward_episode))
                print("Observation: {}".format(observation))
                break

        reward_average = (reward_average * i_episode + reward_episode) / (i_episode + 1)

    print("Average reward: {}".format(reward_average))

if __name__ == "__main__":
    main()
