from dataclasses import dataclass
from datetime import datetime


@dataclass
class Entry:
    ts: datetime
    food: str
    sugar_g: float
    water_litre: float
    insulin_units: float
    time_eaten: datetime | None = None
    adjusted_sugar_g: float = 0.0
