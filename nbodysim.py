import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import astropy.units as u
import random

class Particle:
    # Constants:
    G = 0.01
    
    def __init__(self, mass, position, velocity):
        self.mass = mass
        # position and velocity vector attributes
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
    
    def update_position(self, dt):
        self.position = self.position + self.velocity*dt
    def update_velocity(self, dt, force):
        self.velocity = self.velocity + force / self.mass * dt
    
class NBodySimulation:
    def __init__(self, particles):
        self.particles = particles
    
    def calculate_force(self, particle1, particle2):
        r = particle2.position - particle1.position
        distance = np.linalg.norm(r)
        force_magnitude = Particle.G * particle1.mass * particle2.mass / (distance**2)
        force_direction = r / distance
        return force_magnitude * force_direction
    
    def update(self, dt):
        forces = [np.zeros(2) for _ in self.particles]
        for i,particle in enumerate(self.particles):
            for j, other_particle in enumerate(self.particles):
                if i!=j:
                    force = self.calculate_force(particle, other_particle)
                    forces[i] += force
                    forces[j] -= force
        
        for particle,force in zip(self.particles, forces):
            particle.update_velocity(force, dt)
            particle.update_position(dt)
            

p1 = Particle(1, [0,0], [0,0])
p2 = Particle(1, [1, -1], [0.05, 0.05])

particles = [p1,p2]

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
scatter = ax.scatter([], [])

def update(frame):
    NBodySimulation(particles).update(0.5)
    x = [p.position[0] for p in NBodySimulation(particles).particles]
    y = [p.position[1] for p in NBodySimulation(particles).particles]
    scatter.set_offsets(np.c_[x,y])
    return scatter,

anim = FuncAnimation(fig, update, frames=500, interval =60, blit=True)

plt.show()