UCS_adj_list = {
    'A': [['B', 7], ['C', 3], False],
    'B': [['E', 6], ['C', 2],  False],
    'C': [['D', 9], ['B', 2],  False],
    'D': [['H', 13], ['C', 9], ['E', 3], False],
    'E': [['B', 6], ['D', 3], ['F', 2], ['G', 1],  False],
    'F': [['E', 2], False],
    'G': [['E', 1], False],
    'H': [['D', 13], False]
}
current_node = 'A'
goal = input('Enter Goal:')
result = "A"
traversal_path_cost = 0
while goal is not current_node:
    temp = UCS_adj_list[current_node]
    least_cost = temp[0][1]
    least_cost_node = temp[0][0]
    if len(temp) > 2:
        for index in range(1, len(temp)-1):
            if least_cost > temp[index][1] and not UCS_adj_list[temp[index][0]][-1]:
                least_cost = temp[index][1]
                least_cost_node = temp[index][0]
    traversal_path_cost += least_cost
    temp[-1] = True
    current_node = least_cost_node
    result += "+" + current_node
print(result + "\nTotal Cost = ", traversal_path_cost)
