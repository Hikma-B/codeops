import heapq

# Graph
graph = {
    "Almaz": ["Dawit", "Tigist"],
    "Dawit": ["Hanna"],
    "Tigist": [],
    "Hanna": []
}

print("Graph:")
for person in graph:
    print(person, "->", graph[person])

# Heap
heap = []

heapq.heappush(heap, (-5000, "Big Loan"))
heapq.heappush(heap, (-200, "Small Deposit"))
heapq.heappush(heap, (-10000, "Fraud Alert"))

print("Highest Priority:", heapq.heappop(heap))