import random
import math
import time


random.seed(1) # Setting random number generator seed for repeatability

NUM_NEURONS = 10000

NERVE_SIZE = 128000 # nanometers

CONFLICT_RADIUS = 500 # nanometers


def distance(n1, n2):
	return math.sqrt((n1[0] - n2[0]) **2 + (n1[1] - n2[1]) **2)


def check_for_conflicts_slow(ns, conflict_radius):
	conflicting_idxs = {}
	count = 0
	for i in range(len(ns)):
		for j in range(i+1, len(ns)):
			if distance(ns[i], ns[j]) < conflict_radius:
				if i not in conflicting_idxs:
					conflicting_idxs[i] = True
					count += 1
				if j not in conflicting_idxs:
					conflicting_idxs[j] = True
					count += 1
	#
	global alg_0_conflict_set 
	alg_0_conflict_set = set(conflicting_idxs.keys())
	#
	return count


def check_for_conflicts(nerves, conflict_radius):
	d = math.floor( conflict_radius/math.sqrt(2) )
	cells_in_a_row = math.ceil(NERVE_SIZE/d)
	conflicting_idxs = {}
	count = 0
	grid_info = {}
	def add_conf(idx):
		nonlocal count
		nonlocal conflicting_idxs
		if idx not in conflicting_idxs:
			conflicting_idxs[ idx ] = True
			count += 1

	for i in range(len(nerves)):
		cur_nerve = nerves[i]
		x_grid = math.floor(cur_nerve[0]/d)
		y_grid = math.floor(cur_nerve[1]/d)
		if x_grid not in grid_info:
			grid_info[x_grid] = {}
		if y_grid not in grid_info[x_grid]:
			grid_info[x_grid][y_grid] = []
		# elif len(grid_info[x_grid][y_grid]) == 0: # empty only on creation
		# 	print("waaat?")	
		else:
			add_conf(i)
			if len(grid_info[x_grid][y_grid]) == 1:
				add_conf(grid_info[x_grid][y_grid][0])			
		grid_info[x_grid][y_grid].append(i)

		# Check surrounding cells that might be affected
		x_min_affected = math.floor((cur_nerve[0] - conflict_radius + 1)/d)
		x_max_affected = math.floor((cur_nerve[0] + conflict_radius - 1)/d)
		y_min_affected = math.floor((cur_nerve[1] - conflict_radius + 1)/d)
		y_max_affected = math.floor((cur_nerve[1] + conflict_radius - 1)/d)
		for x in range(max(0, x_min_affected), min(cells_in_a_row, x_max_affected + 1)): 
			for y in range(max(0, y_min_affected), min(cells_in_a_row, y_max_affected + 1)):
				if x == x_grid and y == y_grid: continue
				if x not in grid_info or y not in grid_info[x]: continue 
				# Alone neurons that required to be checked
				if len(grid_info[x][y]) == 1 and grid_info[x][y][0] not in conflicting_idxs:
					j = grid_info[x][y][0]
					if distance(cur_nerve, nerves[j]) < conflict_radius:
						add_conf(i)
						add_conf(j)
				# Checking for conflicts with neighbour cell if necessary
				elif i not in conflicting_idxs: 
					for j in grid_info[x][y]:
						if distance(cur_nerve, nerves[j]) < conflict_radius:
							add_conf(i)
							break
	#
	global alg_1_conflict_set 
	alg_1_conflict_set = set(conflicting_idxs.keys())
	#
	return count


def gen_coord ():
	# DO NOT MODIFY THIS FUNCTION
	return int(random.random() * NERVE_SIZE)

if __name__ == '__main__':
	neuron_positions = [[ gen_coord () , gen_coord ()] for i in range ( NUM_NEURONS )]

	n_conflicts = check_for_conflicts (neuron_positions, CONFLICT_RADIUS)
	print(" Neurons in conflict : {}\n".format( n_conflicts ))
	

	# t_sum = 0
	# runs_count = 1000
	# for i in range(runs_count):
	# 	neuron_positions = [[ gen_coord () , gen_coord ()] for i in range ( NUM_NEURONS )]
	# 	t0 = time.time()
	# 	check_for_conflicts (neuron_positions, CONFLICT_RADIUS)
	# 	t_sum += time.time() - t0
	# print(" Average execution time: {} ms".format( int(t_sum*1000/runs_count) ))
	# ~121ms

	# n_conflicts_slow = check_for_conflicts_slow(neuron_positions, CONFLICT_RADIUS)
	# # Cross-checking algorithms
	# diff_set = alg_0_conflict_set.symmetric_difference(alg_1_conflict_set)
	# print(f" Result difference : { len(diff_set) } Slow alg result: {n_conflicts_slow} \n")
	# #

	
