#!/usr/bin/env python

from user import User


class Student(User):
    def learn(self, string):
        self.knowledge.append(string)

    knowledge = []
