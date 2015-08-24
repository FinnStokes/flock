import random
import itertools

import vector

class Flock:
    def __init__(self, size, separation_coefficient = 1.0, alignment_coefficient = 1.0, cohesion_coefficient = 1.0):
        self.agents = [Agent(self) for _ in xrange(size)]
        self.separation_coefficient = separation_coefficient * 0.04
        self.alignment_coefficient = alignment_coefficient * 0.14
        self.cohesion_coefficient = cohesion_coefficient * 0.6
        self.force = vector.Vect()

    def __str__(self):
        return "[" + ", ".join([str(a) for a in self.agents]) + "]"

    def __len__(self):
        return len(self.agents)

    def __getitem__(self, key):
        return self.agents[key]

    def update(self, dt):
        for agent in self.agents:
            agent.computeForces()
        for agent in self.agents:
            agent.update(dt)    

class Agent:
    MAX_FORCE = 3.0
    MAX_SPEED = 2.0
    
    def __init__(self, flock):
        self.pos = vector.Vect(random.random(), random.random(), random.random())
        self.vel = vector.Vect(random.random()*2-1, random.random()*2-1, random.random()*2-1)
        self.force = vector.Vect()
        self.flock = flock
        #self.neighbors = [(0,None)]*7
        self.neighbors = None

    def __str__(self):
        return str(self.pos)

    # def findNeighbors(self):
    #     for i, (dist2, agent) in enumerate(self.neighbors):
    #         if agent:
    #             dist2 = self.pos.dist2(agent.pos)
    #             if i == 0:
    #                 self.neighbors[i] = (dist2, agent)
    #             else:
    #                 for j in xrange(i-1, -1, -1):
    #                     if dist2 > self.neighbors[j][0]:
    #                         self.neighbors[j+1] = (dist2, agent)
    #                         break
    #                     else:
    #                         self.neighbors[j+1] = self.neighbors[j]
    #                     if j == 0:
    #                         self.neighbors[j] = (dist2, agent)
    #     # Determine neighbors
    #     for agent in self.flock.agents:
    #         if agent == self:
    #             continue
    #         dist2 = self.pos.dist2(agent.pos)
    #         if (self.neighbors[-1][1] and dist2 > self.neighbors[-1][0]) or agent in (n[1] for n in self.neighbors):
    #             continue
    #         reverse_enumerate = lambda l: itertools.izip(xrange(len(l)-1, -1, -1), reversed(l))
    #         for i, n in reverse_enumerate(self.neighbors):
    #             if n[1] and n[0] < dist2:
    #                 if i+1 < len(self.neighbors):
    #                     for j in xrange(len(self.neighbors) - 1, i+1, -1):
    #                         self.neighbors[j] = self.neighbors[j-1]
    #                     self.neighbors[i+1] = (dist2, agent)
    #                 break
    #             if i == 0:
    #                 for j in xrange(len(self.neighbors) - 1, i, -1):
    #                     self.neighbors[j] = self.neighbors[j-1]
    #                 self.neighbors[i] = (dist2, agent)
    #     return self.neighbors

    def findNeighbors(self):
        if self.neighbors:
            thresh = self.pos.dist2(self.neighbors[0][1].pos)
            for d, n in self.neighbors[1:]:
                d2 = self.pos.dist2(n.pos)
                if d2 > thresh:
                    thresh = d2
            calc_d2 = lambda n: ((n.pos.x - self.pos.x)**2 + (n.pos.y - self.pos.y)**2 + (n.pos.z - self.pos.z)**2, n)
            nearby_flock = (a for a in self.flock if a.pos.x - self.pos.x <= thresh and self.pos.x - a.pos.x <= thresh and a.pos.y - self.pos.y <= thresh and self.pos.y - a.pos.y <= thresh and a.pos.z - self.pos.z <= thresh and self.pos.z - a.pos.z <= thresh)
            self.neighbors = [(d2, n) for d2, n in map(calc_d2, nearby_flock) if d2 <= thresh and n != self]
            # for n in self.flock:
            #     if n == self:
            #         continue
            #     #if abs(self.pos.x - n.pos.y) > 
            #     d2 = self.pos.dist2(n.pos)
            #     if d2 <= thresh:
            #         self.neighbors += [(d2, n)]
            if len(self.neighbors) > 7:
                self.neighbors.sort()
                self.neighbors = self.neighbors[:7]
            return self.neighbors
        else:
            self.neighbors = [(self.pos.dist2(n.pos), n) for n in self.flock if n != self]
            self.neighbors.sort()
            self.neighbors = self.neighbors[:7]
            return self.neighbors

    def computeForces(self):
        neighbors = self.findNeighbors()
        
        # Apply flock-wide constant force
        self.force = self.flock.force

        for dist2, agent in neighbors:
            # Separation - avoid crowding neighbors (short range repulsion)
            self.force += (self.pos - agent.pos) * self.flock.separation_coefficient/dist2

            # Alignment - steer towards average heading of neighbors
            self.force += agent.vel.normalise() * self.flock.alignment_coefficient

            # Cohesion - steer towards average position of neighbors (long range attraction)
            self.force += (agent.pos - self.pos) * self.flock.cohesion_coefficient

        self.force.limit(self.MAX_FORCE)
            
    def update(self, dt):
        self.vel += self.force*dt
        self.vel.limit(self.MAX_SPEED)

        self.pos += self.vel*dt
