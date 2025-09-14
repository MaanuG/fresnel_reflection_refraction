import matplotlib.pyplot as plt
import numpy as np
import math

class Equations:
    # Snell's Law
    def snells_law(self, theta1_deg, n1, n2):
        theta1_rad = math.radians(theta1_deg)
        if n1 * math.sin(theta1_rad) / n2 > 1:
            return "No transmitted wave exists. Total Internal Reflection occurs."
        theta2_rad = math.asin(n1 * math.sin(theta1_rad) / n2)
        return f"Refracted Angle: {math.degrees(theta2_rad):.2f}°"

    # Brewster's Angle
    def brewsters_angle(self, n1, n2):
        theta_B_rad = math.atan(n2 / n1)
        return math.degrees(theta_B_rad)

    # Fresnel Reflection Coefficients
    def reflection_coefficients(self, theta1_deg, n1, n2):
        theta1_rad = math.radians(theta1_deg)
        if n1 * math.sin(theta1_rad) / n2 > 1:
            return "TIR"
        theta2_rad = math.asin(n1 * math.sin(theta1_rad) / n2)
        r_s = (n1 * math.cos(theta1_rad) - n2 * math.cos(theta2_rad)) / \
              (n1 * math.cos(theta1_rad) + n2 * math.cos(theta2_rad))
        r_p = (n2 * math.cos(theta1_rad) - n1 * math.cos(theta2_rad)) / \
              (n2 * math.cos(theta1_rad) + n1 * math.cos(theta2_rad))
        return r_s, r_p

    # Fresnel Transmission Coefficients
    def transmission_coefficients(self, theta1_deg, n1, n2):
        reflection = self.reflection_coefficients(theta1_deg, n1, n2)
        if reflection == "TIR":
            return 0, 0
        r_s, r_p = reflection
        t_s = 1 - abs(r_s)**2
        t_p = 1 - abs(r_p)**2
        return t_s, t_p

    # Plot Reflectivity vs Angle with Brewster's Angle and TIR shading
    def plot_reflectivity_vs_angle(self, n1, n2, num_points=500):
        angles_deg = np.linspace(0, 90, num_points)
        R_s_list = []
        R_p_list = []

        # Critical angle for TIR
        if n1 > n2:
            theta_c_deg = math.degrees(math.asin(n2 / n1))
        else:
            theta_c_deg = None

        for theta in angles_deg:
            reflection = self.reflection_coefficients(theta, n1, n2)
            if reflection == "TIR":
                R_s_list.append(1.0)
                R_p_list.append(1.0)
            else:
                r_s, r_p = reflection
                R_s_list.append(abs(r_s)**2)
                R_p_list.append(abs(r_p)**2)

        # Brewster's angle
        theta_B_deg = math.degrees(math.atan(n2 / n1))

        plt.figure(figsize=(8, 5))
        plt.plot(angles_deg, R_s_list, label='R_s (s-pol)', color='blue')
        plt.plot(angles_deg, R_p_list, label='R_p (p-pol)', color='red')
        plt.axvline(theta_B_deg, color='green', linestyle='--', label=f"Brewster's Angle ≈ {theta_B_deg:.2f}°")
        if theta_c_deg:
            plt.axvspan(theta_c_deg, 90, color='gray', alpha=0.3, label=f"TIR Region (θ > {theta_c_deg:.2f}°)")

        plt.xlabel("Incident Angle (°)")
        plt.ylabel("Reflectivity")
        plt.title(f"Reflectivity vs Incident Angle (n1={n1}, n2={n2})")
        plt.grid(True)
        plt.legend()
        plt.show()





'''
import math
import matplotlib.pyplot as plt
import numpy as np


class Equations:
    # Snell's Law
    def snells_law(self, theta1_deg, n1, n2):
        theta1_rad = math.radians(theta1_deg)
        if n1 * math.sin(theta1_rad) / n2 > 1:
            return "No transmitted wave exists. Total Internal Reflection occurs."
        theta2_rad = math.asin(n1 * math.sin(theta1_rad) / n2)
        return f"Refracted Angle: {math.degrees(theta2_rad):.2f}°"

    # Brewster's Angle
    def brewsters_angle(self, n1, n2):
        theta_B_rad = math.atan(n2 / n1)
        return f"Brewster's Angle: {math.degrees(theta_B_rad):.2f}°"

    # Fresnel Reflection Coefficients (returns amplitude reflection coefficients)
    def reflection_coefficients(self, theta1_deg, n1, n2):
        theta1_rad = math.radians(theta1_deg)
        # Handle total internal reflection
        if n1 * math.sin(theta1_rad) / n2 > 1:
            return "Total Internal Reflection: Rs=1, Rp=1"
        theta2_rad = math.asin(n1 * math.sin(theta1_rad) / n2)
        r_s = (n1 * math.cos(theta1_rad) - n2 * math.cos(theta2_rad)) / \
              (n1 * math.cos(theta1_rad) + n2 * math.cos(theta2_rad))
        r_p = (n2 * math.cos(theta1_rad) - n1 * math.cos(theta2_rad)) / \
              (n2 * math.cos(theta1_rad) + n1 * math.cos(theta2_rad))
        return r_s, r_p

    # Fresnel Transmission Coefficients (intensity)
    def transmission_coefficients(self, theta1_deg, n1, n2):
        reflection = self.reflection_coefficients(theta1_deg, n1, n2)
        if isinstance(reflection, str):
            return reflection
        r_s, r_p = reflection
        t_s = 1 - r_s**2
        t_p = 1 - r_p**2
        return t_s, t_p

    def plot_reflectivity_vs_angle(self, n1, n2, num_points=500):
        angles_deg = np.linspace(0, 90, num_points)
        R_s_list = []
        R_p_list = []

        for theta in angles_deg:
            reflection = self.reflection_coefficients(theta, n1, n2)
            if isinstance(reflection, str):
                # Total internal reflection
                R_s_list.append(1.0)
                R_p_list.append(1.0)
            else:
                r_s, r_p = reflection
                R_s_list.append(abs(r_s)**2)
                R_p_list.append(abs(r_p)**2)

        plt.figure(figsize=(8, 5))
        plt.plot(angles_deg, R_s_list, label='R_s (s-pol)', color='blue')
        plt.plot(angles_deg, R_p_list, label='R_p (p-pol)', color='red')
        plt.xlabel("Incident Angle (°)")
        plt.ylabel("Reflectivity")
        plt.title(f"Reflectivity vs Incident Angle (n1={n1}, n2={n2})")
        plt.grid(True)
        plt.legend()
        plt.show()
'''