import hashlib
import random
import string
import json

def generate_nodes(email):
    hashed_email = hashlib.sha256(email.encode()).hexdigest()
    random.seed(int(hashed_email, 16))

    # Generate number of nodes 
    num_nodes = random.randint(5, 10)

    # Generate unique node names
    nodes = [''.join(random.choices(string.ascii_uppercase, k=2)) for _ in range(num_nodes)]

    return nodes

def generate_edges(nodes):
    # Generate edges with random costs
    edges = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if random.random() < 0.5:  
                edges.append({"from": nodes[i], "to": nodes[j], "cost": round(random.uniform(1, 10), 2)})
    
    return edges
def generate_student_data(email):
    nodes = generate_nodes(email)
    edges = generate_edges(nodes)
    return nodes, edges


email = "asish2k32gmail.com"

# Generate student data
nodes, edges = generate_student_data(email)

# Output the generated data
print("Nodes:", nodes)
print("Edges:", json.dumps(edges, indent=4))
