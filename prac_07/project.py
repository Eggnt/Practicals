class Project:
    """Represent a project object"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a project from the given values"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return (f"{self.name}, start:{self.start_date}, priority {self.priority}, "
                f"estimate: {self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100

    def update(self, updated_priority, updated_completion_percentage):
        if updated_priority != "":
            self.priority = updated_priority
        if updated_completion_percentage != "":
            self.completion_percentage = updated_completion_percentage
