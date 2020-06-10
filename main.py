from environment.environment import Environment as Env
from Utils.utils import behaviour_policy, greedy_behaviour_policy, target_policy, heatmap, plot_history
from agent.q_learning_agent import GeneralQ as Agent
from numpy import array
from numpy.random import random

if __name__ == '__main__':
    agent = Agent(1, 2, 0, target_policy, behaviour_policy, from_file=False, double=True)
    actions = []
    action = 0
    actions.append(action)
    environment = Env(population_size=1000, initial_sick=1, contagion_rate=1000, mortality_rate=0.1)

    for i in range(10000):
        reward, discount, next_state = environment.update(action)
        action = agent.step(reward, discount, next_state)
        actions.append(action)

        if not environment.ALIVE:
            environment = environment.reset(population_size=1000, initial_sick=1, contagion_rate=1, mortality_rate=0.1)

    agent.save_to_file()

    # heatmap(agent.q_values)
    # plot_history(array(environment.reward_history)*-1)
    print(agent.q_values)
    print(actions)
