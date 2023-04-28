class Route:
    def __init__(self, name, component):
        self.name = name
        self.component = component


def new_route(name, component):
    return Route(name, component)

