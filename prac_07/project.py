class Project:
    """Represent a project object"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a project from the given values"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        return self.priority < other.priority
