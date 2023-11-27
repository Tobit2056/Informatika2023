%%manim -v WARNING -qm OlympicRings

from manim import *

class OlympicRings(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Barvy pro olympijské kruhy
        colors = [BLACK, BLACK, BLUE, RED, YELLOW, YELLOW, GREEN, GREEN]
        radius = 1  # Společný poloměr pro všechny kruhy
        width = 20

        # Vytvoření olympijských kruhů s pomocí Arc
        arcs = []
        angles = [295, 190, 295, 192, 115, 15, 115, 15]  # Angles for each ring
        end_angle = [235, 85 ,340 ,340 ,235 , 80, 235, 80 ]
        for i in range(len(colors)):
            arc = Arc(radius=radius, start_angle=angles[i] * DEGREES, angle=end_angle[i] * DEGREES, color=colors[i], stroke_width=width)
            arcs.append(arc)

        # Nastavení pozic pro kruhy
        positions = [(0, 0, 0), (-0.45, -0.615, 0), (-2.5, 0, 0), (2.5, 0, 0), (-1.25, -1, 0), (-0.8, -0.38, 0), (1.25, -1, 0), (1.7, -0.38, 0)]

        # Animace pro vytvoření a zobrazení olympijských kruhů
        for i in range(len(arcs)):
            arcs[i].move_to(positions[i])
            self.play(Create(arcs[i]))

        self.wait(1)  # Počkejte jednu sekundu na konci animace
