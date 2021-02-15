from typing import Tuple, List
import pygame as pygame
from math import sin, cos, tan, pi


class Hypercube:
    """Class for a hypercube (self explanatory)
    """
    origin: Tuple[float, float, float, float]
    points: List[Tuple[float, float, float, float]]
    segments: list
    colour: Tuple[int, int, int]
    length: int

    def __init__(self, origin: Tuple[float, float, float, float]) -> None:
        """Initialize a new cube"""
        self.origin = origin
        self.points = [
            (1.0, 1.0, 1.0, 1.0),
            (1.0, 1.0, -1.0, 1.0),
            (-1.0, 1.0, -1.0, 1.0),
            (-1.0, 1.0, 1.0, 1.0),
            (1.0, -1.0, 1.0, 1.0),
            (1.0, -1.0, -1.0, 1.0),
            (-1.0, -1.0, -1.0, 1.0),
            (-1.0, -1.0, 1.0, 1.0),
            (1.0, 1.0, 1.0, -1.0),
            (1.0, 1.0, -1.0, -1.0),
            (-1.0, 1.0, -1.0, -1.0),
            (-1.0, 1.0, 1.0, -1.0),
            (1.0, -1.0, 1.0, -1.0),
            (1.0, -1.0, -1.0, -1.0),
            (-1.0, -1.0, -1.0, -1.0),
            (-1.0, -1.0, 1.0, -1.0),
        ]
        self.segments = [
            [self.points[0], self.points[1]],
            [self.points[1], self.points[2]],
            [self.points[2], self.points[3]],
            [self.points[3], self.points[0]],
            [self.points[4], self.points[5]],
            [self.points[5], self.points[6]],
            [self.points[6], self.points[7]],
            [self.points[7], self.points[4]],
            [self.points[0], self.points[4]],
            [self.points[1], self.points[5]],
            [self.points[2], self.points[6]],
            [self.points[3], self.points[7]],
            [self.points[8], self.points[9]],
            [self.points[9], self.points[10]],
            [self.points[10], self.points[11]],
            [self.points[11], self.points[8]],
            [self.points[12], self.points[13]],
            [self.points[13], self.points[14]],
            [self.points[14], self.points[15]],
            [self.points[15], self.points[12]],
            [self.points[8], self.points[12]],
            [self.points[9], self.points[13]],
            [self.points[10], self.points[14]],
            [self.points[11], self.points[15]],
            [self.points[0], self.points[8]],
            [self.points[1], self.points[9]],
            [self.points[2], self.points[10]],
            [self.points[3], self.points[11]],
            [self.points[4], self.points[12]],
            [self.points[5], self.points[13]],
            [self.points[6], self.points[14]],
            [self.points[7], self.points[15]]
        ]
        self.colour = (0, 0, 0)
        self.length = 40
        self.multiply_points()

    def multiply_points(self) -> None:
        """Multiply the points to the initial length
        """
        for i in range(0, len(self.points)):
            x = self.points[i][0]
            y = self.points[i][1]
            z = self.points[i][2]
            w = self.points[i][3]

            self.points[i] = (
                x * self.length,
                y * self.length,
                z * self.length,
                w * self.length
            )

    def draw_segments(self, screen: pygame.Surface) -> None:
        """Draw the line segments for the cube
        """
        for segment in self.segments:
            col = int(min(segment[0][2], segment[1][2]) + 80)
            col = max(col, 0)
            col = min(col, 255)
            colour = (col, col, col)
            pygame.draw.line(screen, colour, self.to_world(segment[0]), self.to_world(segment[1]), 3)

    def draw_points(self, screen: pygame.Surface) -> None:
        """Draw the points for the cube
        """
        for point in self.points:
            col = int(point[2] + 80)
            col = max(col, 0)
            col = min(col, 255)
            colour = (col, col, col)
            pygame.draw.circle(screen, colour, self.to_world(point), 10)

    def update_segments(self) -> None:
        """Update segments to match the points
        """
        self.segments = [
            [self.points[0], self.points[1]],
            [self.points[1], self.points[2]],
            [self.points[2], self.points[3]],
            [self.points[3], self.points[0]],
            [self.points[4], self.points[5]],
            [self.points[5], self.points[6]],
            [self.points[6], self.points[7]],
            [self.points[7], self.points[4]],
            [self.points[0], self.points[4]],
            [self.points[1], self.points[5]],
            [self.points[2], self.points[6]],
            [self.points[3], self.points[7]],
            [self.points[8], self.points[9]],
            [self.points[9], self.points[10]],
            [self.points[10], self.points[11]],
            [self.points[11], self.points[8]],
            [self.points[12], self.points[13]],
            [self.points[13], self.points[14]],
            [self.points[14], self.points[15]],
            [self.points[15], self.points[12]],
            [self.points[8], self.points[12]],
            [self.points[9], self.points[13]],
            [self.points[10], self.points[14]],
            [self.points[11], self.points[15]],
            [self.points[0], self.points[8]],
            [self.points[1], self.points[9]],
            [self.points[2], self.points[10]],
            [self.points[3], self.points[11]],
            [self.points[4], self.points[12]],
            [self.points[5], self.points[13]],
            [self.points[6], self.points[14]],
            [self.points[7], self.points[15]]
        ]

    def to_world(self, point: Tuple[float, float, float, float]) -> Tuple[float, float]:
        """Return 2d point given a 3d point
        """
        # new_point = (point[0] + self.origin[0], point[1] + self.origin[1])

        mult_z = -(point[2] - 100) / 50
        mult_w = -(point[3] - 100) / 50

        new_point = (point[0] * mult_z * mult_w / 2 + self.origin[0], point[1] * mult_z * mult_w / 2 + self.origin[1])
        return new_point

    def rotate_around_yz(self, theta: float):
        """Rotate the cube about the z-axis"""
        for i in range(0, len(self.points)):
            x = self.points[i][0]
            y = self.points[i][1]
            z = self.points[i][2]
            w = self.points[i][3]

            self.points[i] = (
                x,
                y * cos(theta) - z * sin(theta),
                y * sin(theta) + z * cos(theta),
                w
            )

        self.update_segments()

    def rotate_around_xz(self, theta: float):
        """Rotate the cube about the z-axis"""
        for i in range(0, len(self.points)):
            x = self.points[i][0]
            y = self.points[i][1]
            z = self.points[i][2]
            w = self.points[i][3]

            self.points[i] = (
                x * cos(theta) + z * sin(theta),
                y,
                -x * sin(theta) + z * cos(theta),
                w
            )

        self.update_segments()

    def rotate_around_xy(self, theta: float):
        """Rotate the cube about the z-axis"""
        for i in range(0, len(self.points)):
            x = self.points[i][0]
            y = self.points[i][1]
            z = self.points[i][2]
            w = self.points[i][3]

            self.points[i] = (
                x * cos(theta) - y * sin(theta),
                x * sin(theta) + y * cos(theta),
                z,
                w
            )

        self.update_segments()

    def rotate_around_xw(self, theta: float):
        """Rotate the cube about the z-axis"""
        for i in range(0, len(self.points)):
            x = self.points[i][0]
            y = self.points[i][1]
            z = self.points[i][2]
            w = self.points[i][3]

            self.points[i] = (
                x * cos(theta) + w * sin(theta),
                y,
                z,
                x * -sin(theta) + w * cos(theta)
            )

        self.update_segments()

    def rotate_around_yw(self, theta: float):
        """Rotate the cube about the z-axis"""
        for i in range(0, len(self.points)):
            x = self.points[i][0]
            y = self.points[i][1]
            z = self.points[i][2]
            w = self.points[i][3]

            self.points[i] = (
                x,
                y * cos(theta) - w * sin(theta),
                z,
                y * sin(theta) + w * cos(theta)
            )

        self.update_segments()

    def rotate_around_zw(self, theta: float):
        """Rotate the cube about the z-axis"""
        for i in range(0, len(self.points)):
            x = self.points[i][0]
            y = self.points[i][1]
            z = self.points[i][2]
            w = self.points[i][3]

            self.points[i] = (
                x,
                y,
                z * cos(theta) - w * sin(theta),
                z * sin(theta) + w * cos(theta)
            )

        self.update_segments()


def initialize_screen(screen_size: tuple[int, int]) -> pygame.Surface:
    """Initialize pygame and the display window.

    allowed is a list of pygame event types that should be listened for while pygame is running.
    """
    pygame.display.init()
    pygame.font.init()
    screen = pygame.display.set_mode(screen_size)
    screen.fill((0, 0, 0))
    pygame.display.flip()

    return screen


def run_sim() -> None:
    """Run simulation of 3d cube
    """
    run = True
    screen_width = 800
    screen_height = 800
    screen = initialize_screen((screen_width, screen_height))

    hypercube = Hypercube((400, 400, 0, 0))

    theta = pi / 3000

    while run:
        screen.fill((255, 255, 255))

        hypercube.draw_points(screen)
        hypercube.draw_segments(screen)

        hypercube.rotate_around_xz(theta)
        hypercube.rotate_around_yw(theta)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.display.quit()


if __name__ == "__main__":
    run_sim()
