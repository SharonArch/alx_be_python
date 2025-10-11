class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Perform addition without referring to class or instance data"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Perform multiplication while showing the class attribute"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
