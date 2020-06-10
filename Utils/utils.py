from numpy.random import random, randint
from numpy import argmax, array, eye
from matplotlib import pyplot as plt
from numpy import arange, array


def epsilon_greedy(q_values, epsilon):
    """
    Epsilon greedy behaviout policy. Greedy policy with prob epsilon, random with prob 1-epsilon
    :param q_values: Action state values (value of taking an action given state
    :param epsilon: Calibration parameter
    :return: Chosen action
    """
    if epsilon < random():
        return argmax(q_values)
    else:
        return randint(array(q_values).shape[-1])


def target_policy(q, a):
    """
    Policy that we want the agent to follow (Greedy) if q->q* this is optimal policy
    :param q: q values
    :param a: Actions
    :return: Chosen action
    """
    return eye(len(q))[argmax(q)]


def behaviour_policy(q):
    """
    Behaviour policy: Epsilon greeedy with epsilon 0.1
    :param q: q values
    :return: Chosen action
    """
    return epsilon_greedy(q, 0.1)


def greedy_behaviour_policy(q):
    """
    Behaviour policy: Epsilon greeedy with epsilon 0.1
    :param q: q values
    :return: Chosen action
    """
    return epsilon_greedy(q, 0)


def heatmap(q_values):
    # sns.heatmap(q_values,  annot=True)
    plt.imshow(q_values, cmap='hot', interpolation='nearest')
    plt.show()


def plot_history(healthy):
# def plot_history(healthy, silent, sick, recovered, dead):
    fig = plt.figure()
    ax = fig.gca()
    ax.bar(arange(len(healthy)), healthy, 1, align='center', label='sick')
    # ax.bar(arange(len(silent)), silent, 1, bottom=array(healthy), align='center', label='silent')
    # ax.bar(arange(len(sick)), sick, 1, bottom=array(healthy)+array(silent), align='center', label='sick', color='#009900')
    # ax.bar(arange(len(recovered)), recovered, 1, bottom=array(healthy)+array(silent)+array(sick), align='center', label='recovered', color='#d94a26')
    # ax.bar(arange(len(dead)), dead, 1, bottom=array(healthy)+array(silent)+array(sick)+array(recovered), align='center', label='dead', color='#000000')

    ax.legend(loc='best')
    ax.set_title('Disease Dynamics by Group')
    ax.set_ylabel('Number of People')
    ax.set_xlabel('Days passed')
    fig.show()
