#!/bin/python
import unittest

class helloWorld:
    def __init__(self, results):
        self.results = results

    def showResults(self):
        print (self.results)


def main():
    helloWorld("Hello World").showResults()

if __name__ == '__main__':
    main()