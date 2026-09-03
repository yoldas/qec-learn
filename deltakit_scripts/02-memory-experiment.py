#!/usr/bin/env python
from deltakit_compile.frontend.logasm import LogAsmBuilder, RotatedPlanarPatch
from deltakit_visualise.logical_assembly_visualiser import LogicalAssemblyVisualiser

# uv add deltakit-compile
# uv add deltakit-visualise
# uv run deltakit_visualise.logical_assembly_visualiser
# open http://localhost:8000

# https://www.riverlane.com/blog/introducing-deltakit-compile-and-deltakit-visualise

def main():
    rounds = 20 # measure stabilisers 20 times - repeated error deection cycles
    builder = LogAsmBuilder()

    reg = RotatedPlanarPatch(3, 3, location=(0, 0))
    p = builder.declare_patch(reg)
    p.prepare("Z")  # prepare op.
    p.measure_stabilisers(rounds) # measure stabilisers op.
    b = p.measure("Z")  # measure op.
    builder.add_return(b)
    program = builder.build_program()
    # breakpoint()

    LogicalAssemblyVisualiser(program).visualise()

if __name__ == "__main__":
    main()

# ASGI https://uvicorn.dev/
