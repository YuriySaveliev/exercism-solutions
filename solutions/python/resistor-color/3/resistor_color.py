COLORS = [
        'black', 
        'brown', 
        'red', 
        'orange', 
        'yellow', 
        'green', 
        'blue', 
        'violet', 
        'grey', 
        'white'
 ]

def color_code(color: str) -> str:
    return colors().index(color)


def colors() -> list[str]:
    return COLORS
