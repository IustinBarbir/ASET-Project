class LinearCombinationHandler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle_combination(self, combination):
        if self.next_handler:
            return self.next_handler.handle_combination(combination)
        return None

class NoiseHandler(LinearCombinationHandler):
    def handle_combination(self, combination):
        if combination.get_type() == "Noise":
            print("Applying noise reduction to the linear combination.")
        else:
            return super().handle_combination(combination)

class ErrorCorrectionHandler(LinearCombinationHandler):
    def handle_combination(self, combination):
        if combination.get_type() == "Error Correction":
            print("Applying error correction to the linear combination.")
        else:
            return super().handle_combination(combination)

class ISDHandler(LinearCombinationHandler):
    def handle_combination(self, combination):
        if combination.get_type() == "Stern's ISD Algorithm":
            print("Applying Stern's ISD algorithm to decode the linear combination.")
        else:
            return super().handle_combination(combination)

class LinearCombination:
    def __init__(self, lc_type):
        self.lc_type = lc_type

    def get_type(self):
        return self.lc_type

def main():
    # Create the chain of responsibility
    handler_chain = NoiseHandler()
    handler_chain.set_next(ErrorCorrectionHandler()).set_next(ISDHandler())

    # Simulate decoding process
    linear_combinations = [
        LinearCombination("Noise"),
        LinearCombination("Error Correction"),
        LinearCombination("Stern's ISD Algorithm"),
        LinearCombination("Unknown Type")
    ]

    for lc in linear_combinations:
        print(f"Processing linear combination of type: {lc.get_type()}")
        handler_chain.handle_combination(lc)
        print()

if __name__ == "__main__":
    main()
