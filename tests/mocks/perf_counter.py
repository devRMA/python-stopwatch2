class MockPerfCounter:
    value: float

    def __init__(self) -> None:
        self.value = 0.0

    def increment(self, n: float) -> None:
        self.value += n

    def perf_counter(self) -> float:
        return self.value
