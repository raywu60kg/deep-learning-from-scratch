class Operation:
    def get_output(self):
        raise NotImplementedError

    def get_gradient(self):
        raise NotImplementedError

    def update_parameters(self):
        raise NotImplementedError
