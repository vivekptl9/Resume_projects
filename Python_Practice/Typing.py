from typing import List, Dict, Optional


class Section:
    """
    General Section object
    Attributes:
        upper: identifies the upper section (corresponds to the lower-attribute of the upper neighbour)
        lower: identifies the lower section (corresponds to the upper-attribute of the lower neighbour)
    """

    def __init__(self, upper: int = None, lower: int = None, length: float = None):
        self.upper: Optional[int] = upper
        self.lower: Optional[int] = lower
        self.length: Optional[float] = length
    def __str__(self):
        return f"Section(upper={self.upper}, lower={self.lower}, length={self.length})"
    def __repr__(self):
        return f'({self.upper},{self.lower},{self.length})'

    

def find_neighbours(sections: List[Section]) -> Dict[Section, List[Section]]:
    """
    Find neighbouring sections
    The result of the function is supposed to simplify the access to the next object(s).
    Usecase: objects = find_neighbours(sections)
    for section in sections:
        close_objects = objects[section]
    Args:
        sections: list of section
    Returns:
        Dict with Section object as key and a list of sections next to the section
    """
    # neighbours = {}
    # for section in sections:
    #     key = str(section)
    #     value = []
    #     for s in sections:
    #         if s.upper == section.lower or s.lower == section.upper:
    #             value.append(s)
    #             # print(f"Section: {section.upper} - {section.lower}, Neighbor: {s.upper} - {s.lower}")
    #     neighbours[key] = value
    #     # print(f"Key: {key}, Value: {value}")
    neighbours = {}
    for section in sections:
        key = str(section)
        value = []
        for s in sections:
            if s.upper == section.lower or s.lower == section.upper:
                value.append(str(s))
                neighbours[key] = value   
            # print(f"key{section} ---- value: {s}")
        # print(neighbours)
    return neighbours



def get_test_data(total=1000) -> List[Section]:
    sections = []
    for idx in range(total):
        sections.append(Section(upper=None if idx == 0 else idx, lower=idx))
        sections.append(Section(upper=None if idx == 0 else idx +
                        2 * total, lower=idx + 2 * total + 1))
        sections.append(Section(upper=None if idx == 0 else idx +
                        4 * total, lower=idx + 4 * total + 1))
    return sections


# Example usage:
test_sections = get_test_data(5)
neighbours = find_neighbours(test_sections)
for section in test_sections:
    print(f"Neighbours of section {str(section)}: {neighbours.get(str(section))}")
