#!/usr/bin/env python

import cmath
import math

def main():
    # Define a complex number
    z = 3 + 4j

    # Calculate the magnitude (absolute value)
    magnitude = abs(z)

    # Calculate the phase (angle in radians)
    phase = cmath.phase(z)

    print(f"Complex Number: {z}")
    print(f"Magnitude: {magnitude}")
    print(f"Phase (radians): {phase}")
    print(f"Real Part: {z.real}")
    print(f"Imaginary Part: {z.imag}")

    # Convert to polar coordinates
    polar_coordinates = cmath.polar(z)
    print(f"Polar Coordinates: {polar_coordinates}")
    r, theta = polar_coordinates
    print(f"Radius: {r}, Angle (radians): {theta}")

    # Convert back to rectangular form
    rectangular_form = cmath.rect(r, theta)
    print(f"Rectangular Form: {rectangular_form}")

    # e^(iθ) = cos(θ) + i sin(θ)
    r = 2
    theta = math.pi / 3
    z = r * cmath.exp(1j * theta)
    print("Using complex exponential:", z)

    z = math.cos(theta) + 1j * math.sin(theta)
    print("Using trigonometric form:", z)

if __name__ == "__main__":
    main()
