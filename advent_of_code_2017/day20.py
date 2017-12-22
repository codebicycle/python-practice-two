"""
--- Day 20: Particle Swarm ---
Suddenly, the GPU contacts you, asking for help. Someone has asked it to simulate too many particles, and it won't be able to finish them all in time to render the next frame at this rate.

It transmits to you a buffer (your puzzle input) listing each particle in order (starting with particle 0, then particle 1, particle 2, and so on). For each particle, it provides the X, Y, and Z coordinates for the particle's position (p), velocity (v), and acceleration (a), each in the format <X,Y,Z>.

Each tick, all particles are updated simultaneously. A particle's properties are updated in the following order:

Increase the X velocity by the X acceleration.
Increase the Y velocity by the Y acceleration.
Increase the Z velocity by the Z acceleration.
Increase the X position by the X velocity.
Increase the Y position by the Y velocity.
Increase the Z position by the Z velocity.
Because of seemingly tenuous rationale involving z-buffering, the GPU would like to know which particle will stay closest to position <0,0,0> in the long term. Measure this using the Manhattan distance, which in this situation is simply the sum of the absolute values of a particle's X, Y, and Z position.

For example, suppose you are only given two particles, both of which stay entirely on the X-axis (for simplicity). Drawing the current states of particles 0 and 1 (in that order) with an adjacent a number line and diagram of current X positions (marked in parenthesis), the following would take place:

p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>                         (0)(1)

p=< 4,0,0>, v=< 1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=< 2,0,0>, v=<-2,0,0>, a=<-2,0,0>                      (1)   (0)

p=< 4,0,0>, v=< 0,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=<-2,0,0>, v=<-4,0,0>, a=<-2,0,0>          (1)               (0)

p=< 3,0,0>, v=<-1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
p=<-8,0,0>, v=<-6,0,0>, a=<-2,0,0>                         (0)
At this point, particle 1 will never be closer to <0,0,0> than particle 0, and so, in the long run, particle 0 will stay closest.

Which particle will stay closest to position <0,0,0> in the long term?

"""
from collections import defaultdict
import re
from pprint import pprint


PATTERN = r'<([-,\d]+)>'


class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def position_at(self, tick):
        THREE_DIMMENSIONS = 3
        new_position = [None] * THREE_DIMMENSIONS
        for i in range(THREE_DIMMENSIONS):
            new_position[i] = self.position[i] + distance(tick, self.velocity[i], self.acceleration[i])
        return tuple(new_position)


class Swarm:
    """Particle swarm"""
    def __init__(self):
        self.particles = []

    def build(self, particle_components_list):
        for particle_components in particle_components_list:
            self.particles.append(Particle(*particle_components))

    def closest_to_origin_at(self, tick):
        positions = [particle.position_at(tick) for particle in self.particles]
        # pprint(sorted((self._distance_from_origin(position), index, position)
        #               for index, position in enumerate(positions)))
        return positions.index(min(positions, key=self._distance_from_origin))

    def _distance_from_origin(self, position):
        return sum(map(abs, position))

    def count_particles_after(self, ticks):
        particles = self.particles.copy()

        for tick in range(ticks):
            positions = {}
            collisions = defaultdict(list)
            for index, particle in enumerate(particles):
                if particle:
                    position = particle.position_at(tick)
                    if position in collisions:
                        collisions[position].append(index)
                    elif position in positions:
                        collisions[position].append(positions[position])
                        collisions[position].append(index)
                    else:
                        positions[position] = index

            for _, collision_indices in collisions.items():
                for index in collision_indices:
                    particles[index] = None

        return self._count_particles(particles)

    @staticmethod
    def _count_particles(particle_list):
        """Count """
        return sum(map(bool, particle_list))


def distance(tick, velocity, acceleration):
    return tick * (velocity + acceleration) + 1/2 * (tick - 1) * tick * acceleration

def read_input(filename):
    """List of particle components: position, velocity, acceleration.
    Each sublist contains three tuples of ints representing a particle's
    position, velocity and acceleration in X, Y, Z dimmensions.
    """
    accumulator = []
    with open(filename) as f:
        for line in f:
            matches = re.findall(PATTERN, line)
            components = [tuple(map(int, match.split(','))) for match in matches]
            accumulator.append(components)
    return accumulator

def main():
    puzzle_input = read_input('input20.txt')

    swarm = Swarm()
    swarm.build(puzzle_input)

    TICK = 10_000
    result = swarm.closest_to_origin_at(TICK)
    print('Part 1 solution:', result)


    TICK = 1_000
    result = swarm.count_particles_after(TICK)
    print('Part 2 solution:', result)


if __name__ == '__main__':
    main()
