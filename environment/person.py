from random import random

class Status:
    healthy = 0
    silent = 1
    sick = 2
    recovered = 3
    dead = 4


class Person:
    status = Status()
    current_status = status.healthy

    def __init__(self, time_to_sick, time_to_heal):
        self.time_to_sick = time_to_sick
        self.time_to_heal = time_to_heal

    def update(self, mortality_rate, get_sick=False, locked=False):
        if get_sick and self.current_status == self.status.healthy and not locked:
            # Person gets sick if is in contact with sick person (get_sick),
            # it is a healthy person and there is no lockdown
            self.current_status = self.status.sick  # TODO: silent for silent period
            return self.current_status

        elif self.current_status == self.status.silent:
            if self.time_to_sick > 0:
                self.time_to_sick -= 1
            else:
                self.current_status = self.status.sick
                return self.current_status

        elif self.current_status == self.status.sick:
            if self.time_to_heal > 0:
                self.time_to_heal -= 1
            else:
                if random() < mortality_rate:
                    self.current_status = self.status.dead
                else:
                    self.current_status = self.status.recovered

                return self.current_status
        return None
