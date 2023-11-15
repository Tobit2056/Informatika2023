%%manim -v WARNING -qm OlympicRings
​
from manim import *
​
class OlympicRings(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Barvy pro olympijské kruhy
        colors = [BLACK, BLUE, RED, YELLOW, GREEN]
        radius = 1  # Společný poloměr pro všechny kruhy
        width = 20
        start_angles = [0, 45, 90, 135, 180]  # Začáteční úhel oblouku v stupních
        end_angle = 360  # Koncový úhel oblouku v stupních
​
        # Vytvoření olympijských kruhů s pomocí Arc
        arcs = [Arc(radius=radius, start_angle=start_angle * DEGREES, angle=end_angle * DEGREES, color=color, stroke_width=width) for start_angle, color in zip(start_angles, colors)]
​
        # Nastavení pozic pro kruhy
        positions = [(0, 0, 0), (-2.5, 0, 0), (2.5, 0, 0), (-1.25, -1, 0), (1.25, -1, 0)]
​
        # Animace pro vytvoření a zobrazení olympijských kruhů
        for arc, position in zip(arcs, positions):
            arc.move_to(position)
            self.play(Create(arc))
​
        self.wait(1)  # Počkejte jednu sekundu na konci animace
