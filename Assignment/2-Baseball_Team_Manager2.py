# Display Header
print("=================================================================")
print("                   Baseball Team Manager")
print()
print("This program calculate the batting average for a play based on")
print("the player's official number of at bats and hits.")
print("=================================================================")

# Gather required data
name = input("Player's name: ")
num_at_bats = int(input("Official number of at bats: "))
num_hits = int(input("Number of hits: "))

# Calculate batting average
avg = num_hits / num_at_bats

# Output
print()
print(f"{name}'s batting average is: {avg:.3f}")
