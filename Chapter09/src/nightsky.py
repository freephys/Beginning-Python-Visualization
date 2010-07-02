# create a fictitious night sky
from random import randrange as rr

execfile('star_patch.py')

# parameters for the simulated night sky image
img_size = 800
num_stars = 25

# star parameters: number of pointy edges and radius
min_num_points = 5
max_num_points = 11
min_star_radius = 2
max_star_radius = 10

# star parameter 'thinness' is on a scale of 1 to 10
min_thin = 5
max_thin = 9

# draw the night sky
figure(facecolor='k')
cur_axes = gca()

# patch stars
for i in range(num_stars):
    new_star = star(rr(min_star_radius, max_star_radius), 
        rr(0, img_size) , rr(0, img_size), 'w', \
        rr(min_num_points, max_num_points), \
        rr(min_thin, max_thin)/10.0)
    cur_axes.add_patch(new_star)

# modify axis behavior
axis([0, img_size, 0, img_size])
axis('scaled')
axis('off')

savefig('../images/nightsky', facecolor='k', edgecolor='k')