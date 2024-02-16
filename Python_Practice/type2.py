from typing import Optional


class Section:
    def __init__(self, upper: Optional[int] = None, lower: Optional[int] = None, length: Optional[float] = None):
        self.upper: Optional[int] = upper
        self.lower: Optional[int] = lower
        self.length: Optional[float] = length



class PipeSection(Section):
    def __init__(self, diameter: Optional[float] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.diameter: Optional[float] = diameter

    def get_volume(self) -> float:
        # Volume of cylinder formula: π * r^2 * h
        return self.length * (self.diameter / 2) ** 2 * 3.14159


class RectangularSection(Section):
    def __init__(self, width: Optional[float] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width: Optional[float] = width

    def get_volume(self) -> float:
        return self.length * self.width


def get_price(section: Section, price_per_volume: float = 10.) -> float:
    return section.get_volume() * price_per_volume


# Example usage:
pipe_section = PipeSection(upper=1, lower=2, length=5, diameter=2)
rectangular_section = RectangularSection(upper=3, lower=4, length=6, width=3)

pipe_volume = pipe_section.get_volume()
rectangular_volume = rectangular_section.get_volume()

pipe_price = get_price(pipe_section)
rectangular_price = get_price(rectangular_section)

print("Pipe Volume:", pipe_volume)
print("Pipe Price:", pipe_price)
print("Rectangular Volume:", rectangular_volume)
print("Rectangular Price:", rectangular_price)
