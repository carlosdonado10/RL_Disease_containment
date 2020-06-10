import numpy as np


class GeneralQ(object):

    def __init__(self, number_of_states, number_of_actions, initial_state, target_policy, behaviour_policy, from_file, double, step_size=0.1):
        self._q = np.zeros((number_of_states, number_of_actions))
        if double:
            self._q2 = np.zeros((number_of_states, number_of_actions))

        self._s = initial_state
        self._number_of_actions = number_of_actions
        self._step_size = step_size
        self._behaviour_policy = behaviour_policy
        self._target_policy = target_policy
        self._double = double
        self._last_action = 0
        if from_file:
            self.load_from_file()

    @property
    def q_values(self):
        if self._double:
            return (self._q + self._q2)/2
        else:
            return self._q

    def step(self, r, g, s):
        # a = self._behaviour_policy(self.q_values[s])
        a = np.random.randint(0,2)

        if self._double:
            if np.random.random() > 0.5:
                self._q[self._s][self._last_action] += self._step_size * (r + g * np.dot(self._q2[s], self._target_policy(self._q[s], a)) - self._q[self._s][self._last_action])
            else:
                self._q2[self._s][self._last_action] += self._step_size * (r + g * np.dot(self._q[s], self._target_policy(self._q2[s], a)) - self._q2[self._s][self._last_action])
        else:
            self._q[self._s][self._last_action] += self._step_size * (r + g * np.dot(self._q[s], self._target_policy(self._q[s], a)) - self._q[self._s][self._last_action])

        self._s = s
        self._last_action = a
        return a

    def load_from_file(self):
        self._q = np.load('./Data/q_values_checkpoint.npy')
        if self._double:
            self._q2 = np.load('./Data/q_values_2_checkpoint.npy')

    def save_to_file(self):
        np.save('./Data/q_values_checkpoint.npy', self._q)
        if self._double:
            np.save('./Data/q_values_2_checkpoint.npy', self._q2)
