%%manim -v WARNING -qm OlympicRings

from manim import *

class OlympicRings(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Barvy pro olympijské kruhy
        width = 20
        colors = [BLACK, BLUE, RED, YELLOW, GREEN]
        radius = 1  # Společný poloměr pro všechny kruhy

        # Vytvoření olympijských kruhů s stejným poloměrem
        rings = [Circle(radius=radius, color=color, stroke_width=width) for color in colors]

        # Nastavení pozic pro kruhy
        positions = [(0, 0, 0), (-2.5, 0, 0), (2.5, 0, 0), (-1.25, -1, 0), (1.25, -1, 0)]

        # Animace pro vytvoření a zobrazení olympijských kruhů
        for ring, position in zip(rings, positions):
            ring.move_to(position)
            self.play(Create(ring))


        self.wait(1)  # Počkejte jednu sekundu na konci animace
