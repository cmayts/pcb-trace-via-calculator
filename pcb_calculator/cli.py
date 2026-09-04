import argparse

from .calculations import trace_width_mm, via_barrel_area_mm2


def main():
    parser = argparse.ArgumentParser(description="Estimate PCB trace width and via barrel geometry")
    commands = parser.add_subparsers(dest="command", required=True)
    trace = commands.add_parser("trace", help="Estimate external trace width")
    trace.add_argument("--current", type=float, required=True)
    trace.add_argument("--copper-oz", type=float, default=1.0)
    trace.add_argument("--temp-rise", type=float, default=10.0)
    via = commands.add_parser("via", help="Calculate plated via copper area")
    via.add_argument("--drill-mm", type=float, required=True)
    via.add_argument("--plating-um", type=float, default=25.0)
    args = parser.parse_args()
    try:
        if args.command == "trace":
            width = trace_width_mm(args.current, args.copper_oz, args.temp_rise)
            print(f"Required width: {width:.3f} mm ({width / 0.0254:.2f} mil)")
        else:
            area = via_barrel_area_mm2(args.drill_mm, args.plating_um)
            print(f"Via barrel copper area: {area:.5f} mm²")
    except ValueError as error:
        parser.error(str(error))
