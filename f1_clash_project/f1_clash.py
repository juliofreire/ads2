"""F1 clash analysis"""
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

# Defining the cards of each piece on setup-car

breaks = [['wildcore', 36, 23, 33, 22, 0.59, 0, 0, 0, 0, 0],
          ['suspense',20, 32, 23, 21, 0.37, 0, 0, 0, 0, 0],
          ['the warden', 26, 28, 27, 25, 0.43, 0, 0, 0, 0, 0],
          ['onyx', 26, 23, 25, 50, 0.49, 0, 0, 0, 0, 0],
          ['axiom', 14, 34, 18, 15, 0.67, 0, 0, 0, 0, 0],
          ['crisis sl', 27, 16, 18, 19, 0.51, 0, 0, 0, 0, 0],
          ['essence', 14, 13, 12, 25, 0.76, 0, 0, 0, 0, 0],
          ['starter', 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]

gearboxes = [['voyage', 23, 28, 22, 27, 0, 0, 0, 0, 0, 0],
             ['vector', 24, 38, 22, 36, 0.55, 0, 0, 0, 0, 0],
             ['kick shift', 18, 19, 29, 19, 0.45, 0, 0, 0, 0, 0],
             ['verdict', 33, 18, 20, 30, 0.63, 0, 0, 0, 0, 0],
             ['spectrum', 20, 25, 21, 23, 0.53, 0, 0, 0, 0, 0],
             ['swiftcharge', 14, 23, 22, 16, 0.71, 0, 0, 0, 0, 0],
             ['switch-r-00', 12, 13, 11, 14, 0.47, 0, 0, 0, 0, 0],
             ['starter', 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]

rearwings = [['typhon', 50, 27, 26, 23, 0.53, 0, 0, 0, 0, 0],
             ['transcendence', 24, 22, 36, 37, 0.53, 0, 0, 0, 0, 0],
             ['freeflare', 21, 33, 20, 22, 0.37, 0, 0, 0, 0, 0],
             ['the patron', 23, 21, 19, 37, 0.61, 0, 0, 0, 0, 0],
             ['the wasp', 16, 24, 23, 14, 0.69, 0, 0, 0, 0, 0],
             ['the matador', 19, 16, 18, 17, 0.72, 0, 0, 0, 0, 0],
             ['phantom-x', 26, 15, 12, 11, 0.76, 0, 0, 0, 0, 0],
             ['starter', 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]

frontwings = [['virtue', 23, 50, 27, 24, 0.49, 0, 0, 0, 0, 0],
              ['thunderclap', 35, 23, 21, 33, 0.55, 0, 0, 0, 0, 0],
              ['trailblazer', 21, 23, 42, 20, 0.57, 0, 0, 0, 0, 0],
              ['zeno', 25, 23, 22, 26, 0.53, 0, 0, 0, 0, 0],
              ['the vagabond', 31, 20, 23, 21, 0.35, 0, 0, 0, 0, 0],
              ['feral punch', 13, 15, 22, 21, 0.73, 0, 0, 0, 0, 0],
              ['the scout', 13, 27, 15, 14, 0.73, 0, 0, 0, 0, 0],
              ['starter', 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]

suspensions = [['sigma', 32, 28, 30, 29, 0.39, 0, 0, 0, 0, 0],
               ['presence', 23, 26, 24, 22, 0.2, 0, 0, 0, 0, 0],
               ['horizon', 22, 36, 24, 37, 0.53, 0, 0, 0, 0, 0],
               ['radiance', 25, 17, 26, 19, 0.65, 0, 0, 0, 0, 0],
               ['icon v3', 17, 13, 16, 23, 0.54, 0, 0, 0, 0, 0],
               ['rodeo', 23, 22, 15, 14, 0.69, 0, 0, 0, 0, 0],
               ['the equator', 20, 19, 18, 21, 0.61, 0, 0, 0, 0, 0],
               ['starter', 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]

engines = [['cloudroar', 26, 24, 50, 27, 0.55, 0, 0, 0, 0, 0],
           ['avalanche', 34, 22, 25, 21, 0.35, 0, 0, 0, 0, 0],
           ['the rover', 27, 25, 28, 24, 0.53, 0, 0, 0, 0, 0],
           ['twinburst', 16, 29, 18, 17, 0.51, 0, 0, 0, 0, 0],
           ['enigma', 16, 13, 23, 25, 0.69, 0, 0, 0, 0, 0],
           ['nova', 31, 13, 15, 16, 0.71, 0, 0, 0, 0, 0],
           ['brute force', 21, 19, 36, 18, 0.63, 0, 0, 0, 0, 0],
           ['starter', 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]

setup_car = [breaks, gearboxes, rearwings, frontwings, suspensions, engines]

# Defining another item in game: bottles

bottles = [['tsar', 0, 15, 0, 0, 0, 0, 10, 0, 25, 0],
           ['frost', 0, 0, 0, 10, 0, 0, 0, 15, 25, 0],
           ['tulip', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           ['dragon', 0, 0, 15, 0, 0, 20, 0, 0, 15, 0],
           ['kawaii', 0, 20, 0, 0, 15, 0, 0, 15, 0, 0],
           ['pretzel', 0, 0, 15, 0, 10, 0, 0, 0, 25, 0],
           ['vice', 10, 0, 15, 25, 0, 0, 0, 0, 0, 0],
           ['schooner', 0, 0, 0, 25, 15, 0, 10, 0, 0, 0],
           ['djinn', 0, 15, 0, 20, 0, 0, 15, 0, 0, 0],
           ['oud', 0, 10, 0, 0, 25, 15, 0, 0, 0, 0],
           ['eternal flame', 0, 0, 0, 15, 0, 25, 0, 0, 10, 0],
           ['eagle', 0, 0, 0, 15, 15, 0, 0, 0, 20, 0],
           ['iron force', 0, 0, 20, 20, 0, 0, 0, 0, 10, 0],
           ['lumberjack', 0, 0, 0, 25, 0, 0, 15, 0, 10, 0],
           ['cranberry', 0, 0, 0, 10, 0, 20, 20, 0, 0, 0],
           ['butterfly', 0, 0, 25, 0, 5, 0, 0, 0, 20, 0],
           ['tune-in', 10, 15, 0, 0, 25, 0, 0, 0, 0, 0],
           ['self-control', 0, 0, 5, 5, 0, 0, 0, 0, 5, 0],
           ['warrior', 10, 0, 0, 0, 0, 5, 5, 0, 0, 0],
           ['ballast', 0, 10, 0, 0, 10, 0, 0, 5, 0, 0],
           ['instinct', 0, 0, 15, 5, 0, 0, 0, 10, 0, 0],
           ['downforce', 0, 5, 0, 0, 0, 0, 15, 0, 15, 0],
           ['hex', 15, 0, 0, 0, 5, 20, 0, 0, 0, 0],
           ['eggception', 0, 0, 10, 0, 25, 0, 15, 0, 0, 0],
           ['rooster', 0, 0, 10, 0, 0, 20, 0, 20, 0, 0],
           ['cuppa', 0, 20, 0, 0, 0, 10, 0, 20, 0, 0],
           ['street shark', 15, 0, 0, 0, 0, 10, 0, 25, 0, 0],
           ['herald', 0, 15, 0, 0, 0, 10, 0, 25, 0, 0],
           ['prince', 0, 20, 0, 0, 0, 0, 10, 20, 0, 0],
           ['unstoppable', 15, 0, 10, 0, 0, 25, 0, 0, 0, 0],
           ['dead fast', 25, 0, 20, 0, 0, 0, 0, 0, 5, 0],
           ['gladiator', 0, 0, 10, 0, 0, 0, 25, 15, 0, 0],
           ['taurus', 20, 0, 25, 0, 0, 5, 0, 0, 0, 0],
           ['merlion', 15, 25, 0, 0, 10, 0, 0, 0, 0, 0],
           ['samba', 5, 0, 25, 0, 20, 0, 0, 0, 0, 0],
           ['caveira', 25, 0, 10, 0, 0, 15, 0, 0, 0, 0],
           ['fogos', 20, 0, 0, 0, 0, 15, 0, 15, 0, 0],
           ['movember', 0, 25, 0, 0, 0, 0, 15, 0, 10, 0],
           ['palmeira', 0, 0, 0, 0, 0, 0, 20, 10, 20, 0],
           ['nazar', 0, 0, 0, 15, 0, 0, 0, 20, 15, 0],
           ['aderencia', 0, 25, 0, 15, 0, 0, 0, 10, 0, 0],
           ['arco-iris', 20, 0, 0, 0, 0, 0, 25, 5, 0, 0],
           ['eclipse', 25, 0, 0, 0, 10, 15, 0, 0, 0, 0],
           ['rena', 0, 10, 0, 0, 20, 0, 20, 0, 0, 0],
           ]


#glue
#piece = [spd, corner, PU, reliability, avg pst, overtaking, def, racestart, tyre, qualifying]
#teamscore = spd + corner + pu + realiability + 50*avg pst
#setup = [breaks, gearboxes, rearwings, frontwings, suspensions, engines]

"""
    TASK 1:
            Througout the observation of cards, plot a histogram which show the behavior of 
            possibles setups by combinating all pieces of cards. There are 6 differents pieces
            of car and each piece has 8 differents cards, so the all possibles combinations
            is 8^6 ~= 262k.
            Choose a cuttoff empirically to analysis the next task.
                   
"""

def team_score_calc(status):
    """
    This function just calculates the team score for one item.
    Args:
        - A list with all status of one item
    Returns:
        - The result of the ready team score using the formula
    provided by f1 clash: teamscore = spd + corner + pu + realiability + 50*avg pst
    """
    return status[1] + status[2] + status[3] + status[4] + 50*status[5]

# Calculating the teamscore for each card

for piece in setup_car:
    for item in piece:
        item.append(team_score_calc(item))

# Storing the name of combination in a specific order and team score for each combination
all_team_score = []
all_names_combination = []
all_names_ts = []
for i in range(len(setup_car[0])):
    for j in range(len(setup_car[1])):
        for k in range(len(setup_car[2])):
            for l in range(len(setup_car[3])):
                for m in range(len(setup_car[4])):
                    for n in range(len(setup_car[5])):
                        combination_ts = [setup_car[0][i][-1], setup_car[1][j][-1],
                                            setup_car[2][k][-1], setup_car[3][l][-1],
                                            setup_car[4][m][-1], setup_car[5][n][-1]]

                        combination_names = (setup_car[0][i][0] + '+' + setup_car[1][j][0] + '+'
                                            + setup_car[2][k][0] + '+' + setup_car[3][l][0] + '+'
                                            + setup_car[4][m][0] + '+' + setup_car[5][n][0])
                        # Calculates the sum of team score
                        all_names_combination.append(combination_names)
                        all_team_score.append(sum(combination_ts))
                        all_names_ts.append([combination_names, sum(combination_ts)])

# Plot histogram with a mark in CUTOFF in 880
CUTOFF = 880

plt.hist(all_team_score, bins=40, edgecolor='k')
plt.axvline(CUTOFF, color='red', linestyle='dashed', linewidth=2, label='880 Team Score Cutoff')
plt.xlabel('Team Scores')
plt.ylabel('Frequency')
plt.title('Histogram of Team Score')
plt.show()

# Split the new sample to work beyond the cutoff
names_ts_upperCUTOFF = []
for setup in all_names_ts:
    if setup[1] > CUTOFF:
        names_ts_upperCUTOFF.append(setup)

# Checking the value of how many setups is better than 880 ts
print(len(names_ts_upperCUTOFF))



#glue
#piece = [spd, corner, PU, reliability, avg pst, overtaking, def, racestart, tyre, qualifying]
#teamscore = spd + corner + pu + realiability + 50*avg pst
#setup = [breaks, gearboxes, rearwings, frontwings, suspensions, engines]

"""
    TASK 2:
            Plot a graph that each node represent a possible setup and cards that belongs to a
            setup in graph, there is a edge between nodes of setups and cards if a setup contains
            that card.
"""

G = nx.Graph()

piece_count = {}
for idx, setup in enumerate(names_ts_upperCUTOFF):
    G.add_node(f'Setup {idx}', color = 'lightcoral', size = 6*setup[1])
    name = setup[0].split('+')
    edges_to_add = []
    for piece in name:
        piece_count[piece] = piece_count.get(piece, 0) + 1
        G.add_node(piece, color='lightblue', size=200*piece_count[piece])
        edges_to_add.append((f'Setup {idx}', piece))
    G.add_edges_from(edges_to_add)

print(piece_count)
# Extract information of colors and size from each node
node_colors = [node[1]['color'] for node in G.nodes(data=True)]
node_sizes = [node[1]['size'] for node in G.nodes(data=True)]

pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color=node_colors, font_size=12,
         font_color='black', font_weight='bold')

plt.show()

# Generate a PDF graph
degree_values = list(piece_count.values())
hist, bin_edges = np.histogram(degree_values, bins=10, density=True)
bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
pdf = hist / hist.sum()

# Plot pdf
plt.plot(bin_centers, pdf, linestyle='solid', color='lightblue')
plt.xlabel('Degree of Pieces')
plt.ylabel('Density')
plt.title('PDF of Node Degrees for Pieces')
plt.show()

# Get labels and values of dict
keys = list(piece_count.keys())
values = list(piece_count.values())

# Generate a bar plot
plt.figure(figsize=(12, 6))
plt.bar(keys, values, color='lightblue')
plt.xlabel('Pieces')
plt.ylabel('Count')
plt.title('Node Degrees for Pieces')
plt.xticks(rotation=90)

# Labeling with keys
for i, v in enumerate(values):
    plt.text(i, v, str(v), ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Calculate PDF
pdf_values = np.array(values) / sum(values)

# Plot PDF
plt.figure(figsize=(12, 6))
plt.plot(keys, pdf_values, marker='o', linestyle='-')
plt.xlabel('Pieces')
plt.ylabel('Probability Density')
plt.title('Probability Density Function (PDF) for Node Degrees of Pieces')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()


""" 
    TASK 3:
            Plot a bipartite graph which show the attributes and bottles. The edges are becoming
            when a bottle provided a specific status and the weight is the value of attribute.

"""


bottles_wo_names = []
for bottle in bottles:
    bottles_wo_names.append(bottle[1::])

bottles_wo_names = np.array(bottles_wo_names)
size_node_attributes = np.sum(bottles_wo_names, axis=0)

B = nx.DiGraph()

attributes = ['Speed', 'Cornering', 'PU', 'Reliability', 'Avg PST', 'Overtaking',
               'Defending', 'Race Start', 'Tyre Manage', 'Qualifying']


# Add nodes to the first bipartition (attributes)
B.add_nodes_from(attributes, bipartite=0)

# Add nodes to the second partition (bottles)
bottle_names = [bottle[0] for bottle in bottles]
B.add_nodes_from(bottle_names, bipartite=1)

# Add directional edges to second partition from the first one
for bottle in bottles:
    bottle_name = bottle[0]
    for i, attribute in enumerate(bottle[1:]):
        if attribute != 0:
            B.add_edge(attributes[i], bottle_name, weight=attribute)

# Separate nodes in its respectively bipartition
top_nodes = {node for node, data in B.nodes(data=True) if data['bipartite'] == 0}
bottom_nodes = set(B) - top_nodes

plt.figure(figsize=(12, 8))

pos = nx.bipartite_layout(B, top_nodes, scale=3)

# Extract weight of edges
edge_weights = [B[u][v]['weight'] for u, v in B.edges()]
print(edge_weights)

# Extract the labels
edge_labels = {(u, v): d['weight'] for u, v, d in B.edges(data=True)}

# Creat a dict that specify each size of attributes nodes
node_sizes = {node: size_node_attributes[i] for i, node in enumerate(attributes)}

# Create the graph with the setup above
nx.draw_networkx_nodes(B, pos, nodelist=top_nodes, node_color='lightblue',
                        node_size=[node_sizes[node] for node in top_nodes])
nx.draw_networkx_nodes(B, pos, nodelist=bottom_nodes, node_color='lightcoral', node_size=100)
nx.draw_networkx_edges(B, pos, width=1, edge_color='gray', arrows=True)
nx.draw_networkx_edge_labels(B, pos, edge_labels=edge_labels, font_size=8)
nx.draw_networkx_labels(B, pos)

plt.show()


#glue
#piece = [spd, corner, PU, reliability, avg pst, overtaking, def, racestart, tyre, qualifying]
#teamscore = spd + corner + pu + realiability + 50*avg pst
#setup = [breaks, gearboxes, rearwings, frontwings, suspensions, engines]


""" 
    TASK 4:
            Suggest the best setup possible considering the setup is
            formed by parts + drivers + bottles.
"""

drivers = [['verstappen', 0, 0, 0, 0, 0, 97, 86, 89, 94, 99],
           ['leclerc', 0, 0, 0, 0, 0, 93, 99, 87, 89, 97],
           ['alonso', 0, 0, 0, 0, 0, 99, 92, 97, 88, 89],
           ['hamilton', 0, 0, 0, 0, 0, 81, 86, 94, 90, 89],
           ['norris', 0, 0, 0, 0, 0, 99, 95, 99, 99, 99],
           ['russel', 0, 0, 0, 0, 0, 95, 90, 83, 86, 91],
           ['perez', 0, 0, 0, 0, 0, 85, 96, 91, 84, 89],
           ['sainz', 0, 0, 0, 0, 0, 84, 85, 90, 91, 95],
           ['stroll', 0, 0, 0, 0, 0, 92, 83, 94, 89, 87],
           ['gasly', 0, 0, 0, 0, 0, 88, 93, 85, 96, 83]
]

# Combinating all possible of drivers duo
all_drivers_combination = []
for idx, driver_1 in enumerate(drivers):
    for idx, driver_2 in enumerate(drivers[idx+1:]):
        combined_drivers = [driver_1[0] + "+" + driver_2[0]]
        sum_attributes = [a + b for a, b in zip(driver_1[1:], driver_2[1:])]
        team_score_drivers = [sum(sum_attributes)]
        combined_drivers.extend(team_score_drivers)
        all_drivers_combination.append(combined_drivers)

print(all_drivers_combination)

# Picking the best duo
MAX_SUM = 0

for d1d2 in all_drivers_combination:
    if d1d2[1] >= MAX_SUM:
        MAX_SUM = d1d2[1]

best_drivers = []
for d1d2 in all_drivers_combination:
    if d1d2[1] == MAX_SUM:
        best_drivers.append(d1d2)

print(best_drivers)

# Showing the best duo
for idx,_ in enumerate(best_drivers):
    best_duo = best_drivers[idx][0].split('+')
    print(f"{best_duo}:")
    for driver in drivers:
        if driver[0] == best_duo[0] or driver[0] == best_duo[1]:
            print(driver)

# Picking the best setup_car
max_ts = max(all_team_score)
best_setups = []
for one_setup in all_names_ts:
    if one_setup[1] == max_ts:
        best_setups.append(one_setup)
print(best_setups)

# Picking the best card
best_pieces = best_setups[0][0].split('+')
print(best_pieces)
for idx, pieces in enumerate(setup_car):
    for card in pieces:
        if best_pieces[idx] == card[0]:
            print(">>>",card)

# Picking the best bottle

max_bottles = []
sum_bottles = []

for bottle in bottles:
    SUM_1 = 0
    SUM_2 = 0
    for idx in range(5):
        SUM_1 += bottle[idx+1]
        SUM_2 += bottle[idx+6]
    # SUM_1 += 50*bottle[5]
    sum_bottles.append([bottle[0], SUM_1, SUM_2])

MAX_SUM_1 = 0
MAX_SUM_2 = 0

for bottle in sum_bottles:
    if bottle[1] >= MAX_SUM_1:
        MAX_SUM_1 = bottle[1]

    if bottle[2] >= MAX_SUM_2:
        MAX_SUM_2 = bottle[2]

best_bottles = []

for bottle in sum_bottles:
    if bottle[1] == MAX_SUM_1:
        best_bottles.append([bottle, 0])
    if bottle[2] == MAX_SUM_2:
        best_bottles.append([bottle, 1])

print(best_bottles)

for one_of_best_bottle in best_bottles:
    for bottle in bottles:
        if one_of_best_bottle[0][0] == bottle[0]:
            if one_of_best_bottle[1] == 0:
                print(f"This bottle: {bottle} is good to enhace your car setup.")
            else:
                print(f"This bottle: {bottle} is good to enhace your drivers.")
