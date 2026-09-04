import math

OZ_TO_MIL = 1.378
MIL_TO_MM = 0.0254


def trace_width_mm(current_a: float, copper_oz: float = 1.0, temp_rise_c: float = 10.0) -> float:
    """Estimate external-layer trace width using the IPC-2221 equation."""
    if current_a <= 0 or copper_oz <= 0 or temp_rise_c <= 0:
        raise ValueError("Current, copper thickness, and temperature rise must be positive")
    area_mil2 = (current_a / (0.048 * temp_rise_c**0.44)) ** (1 / 0.725)
    return area_mil2 / (copper_oz * OZ_TO_MIL) * MIL_TO_MM


def via_barrel_area_mm2(drill_mm: float, plating_um: float = 25.0) -> float:
    """Return the approximate copper cross-section around a plated via barrel."""
    if drill_mm <= 0 or plating_um <= 0:
        raise ValueError("Drill diameter and plating thickness must be positive")
    plating_mm = plating_um / 1000
    outer_radius = drill_mm / 2 + plating_mm
    inner_radius = drill_mm / 2
    return math.pi * (outer_radius**2 - inner_radius**2)
