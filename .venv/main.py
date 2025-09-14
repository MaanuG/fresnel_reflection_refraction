from fresnel_equations import Equations

def main():
    eq = Equations()
    print("=== Fresnel Reflection & Refraction Calculator ===")
    try:
        n1 = float(input("Enter refractive index of incident medium (n1): "))
        n2 = float(input("Enter refractive index of transmission medium (n2): "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print(f"\nBrewster's Angle: {eq.brewsters_angle(n1, n2):.2f}°\n")

    eq.plot_reflectivity_vs_angle(n1, n2)

if __name__ == "__main__":
    main()
