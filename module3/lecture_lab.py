foods: list[str] = []

foods.insert(0, "pizza")
foods.append("steak")
foods.insert(1, "lasagna")
foods.append("cake")
foods.insert(2, "burger")

print(*foods, sep=", ")
foods.sort()
print(*foods, sep=", ")

for food in foods:
    print(f"I really like to eat {food}")