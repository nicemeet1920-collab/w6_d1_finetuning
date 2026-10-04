from app.knowledge import load_knowledge


dataset = load_knowledge()

print("Number of examples:", len(dataset))

print("\nFirst example:")
print(dataset[0])