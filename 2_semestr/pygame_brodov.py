import pygame
import random
 
x_coordinates = [random.randint(0,800) for i in range(1000)]
y_coordinates = [random.randint(0,600) for i in range(1000)]
 
pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
 
bg = [0,0,0]
earth = [0,0,150]
 
pygame.display.set_caption("Space")
clock = pygame.time.Clock()
 
y=0
y_s=1
x=0
x_s=-1
ry = 0;
dy = 0; dx = 0; dy_s = 1; dx_s = 2;
 
 
done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(bg)
 
    for i in range(1000):
        pygame.draw.circle(screen, [255,255,255],(x_coordinates[i], y_coordinates[i]),1,0)
    for i in range(500):
        k = random.randint(0,999)
        pygame.draw.circle(screen, [40,40,40],(x_coordinates[k], y_coordinates[k]),1,0)
 
    x_coordinate = random.randint(800,1600);
    y_coordinate = random.randint(600,1200);
 
    #sun
    pygame.draw.circle(screen,[255,150,0],(725,75),50)
 
    #comet
    x_coordinate = 0;
    y_coordinate = 0;
    pygame.draw.circle(screen, [200,0,0],(x_coordinate + dx, y_coordinate + dy), 10)
    dy += dy_s
    dx += dx_s
    if dy > 600:
        dy = 0;
        dx = 0;
 
    #rocket
    pygame.draw.polygon(screen,[150,150,150],[[400,600+ry],[420,600+ry],[420,520+ry],[410,500+ry],[400,520+ry]])
    pygame.draw.circle(screen,[200,100,0],(410,600+ry),15)
    ry += -1
    if 600+ry < 0:
        ry = 0;
 
    #earth
    pygame.draw.circle(screen,[0,100,100],(400,950),500)
    pygame.draw.polygon(screen,[0,200,0],[[750,600],[100,550],[400,450],[700,565]])
   
    #station
    pygame.draw.polygon(screen, [255,252,0], [[370+x,250+y],[370+x,380+y],[200+x,380+y],[200+x,250+y]])
    pygame.draw.polygon(screen, [255,252,0], [[450+x,250+y],[450+x,380+y],[620+x,380+y],[620+x,250+y]])
    pygame.draw.line(screen, [50,50,50],(200+x,295+y),(620+x,295+y),1)
    pygame.draw.line(screen, [50,50,50],(200+x,350+y),(620+x,350+y),1)
    pygame.draw.polygon(screen, [255,252,232], [[370+x,450+y],[450+x,450+y],[450+x,200+y],[370+x,200+y]])
    pygame.draw.circle(screen, [255,255,255], (410+x,180+y),60,0)
    pygame.draw.circle(screen, [50,50,50], (410+x,250+y),20,0)
    pygame.draw.circle(screen, [50,50,50], (410+x,300+y),20,0)
    pygame.draw.circle(screen, [50,50,50], (410+x,350+y),20,0)
   
 
 
    y+=y_s
    x+=x_s
    if y>50:
        y_s*=-1
        x_s*=-1
    if y<-50:
        y_s*=-1
        x_s*=-1
 
 
    pygame.display.flip()
    clock.tick(0)
 
pygame.quit()
