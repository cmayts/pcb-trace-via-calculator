# PCB Trace & Via Calculator

A compact Python command-line calculator for early PCB design estimates. It calculates approximate external-layer trace width from current, copper thickness, and permitted temperature rise, and estimates plated via copper cross-sectional area.

## Usage

```bash
python -m pcb_calculator trace --current 2 --copper-oz 1 --temp-rise 10
python -m pcb_calculator via --drill-mm 0.30 --plating-um 25
```

Example trace result:

```text
Required width: 0.781 mm (30.76 mil)
```

## Method and limitations

Trace-width estimation uses the historical IPC-2221 external-conductor empirical relationship. It is useful for educational work and rough comparisons, but it is not a substitute for IPC-2152 evaluation, thermal simulation, stack-up data, copper-process tolerances, environmental conditions, voltage-clearance rules, or PCB manufacturer review.

Via output is geometric copper barrel area only. It does not claim a safe via current rating because current capacity depends strongly on plating quality, pad geometry, surrounding copper, temperature, and manufacturing process.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Privacy

The project contains no board files, customer data, credentials, component lists, or production information.

## License

MIT
