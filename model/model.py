from model.evaluator import Evaluator
from model.collector import Collector


class ML:
    evaluator: Evaluator
    collector: Collector
    def __init__(self):
        self.evaluator = Evaluator()
        self.collector = Collector()
    
    