# 🎮 Stack Tower Game
# Author: Rana Shivang Singh
# Description: A fun console-based game that demonstrates Stack (LIFO) behavior.
# Data Structure: Stack using list

print("🗼 Welcome to the Stack Tower Game!")
print("Rule: You can add or remove blocks, but only from the top of the tower (LIFO).")

stack = []

def show_tower():
    if not stack:
        print("🏗️  The tower is empty.")
    else:
        print("\nCurrent Tower (Top → Bottom):")
        for block in reversed(stack):
            print(f"🧱 {block}")

while True:
    print("\n=== MENU ===")
    print("1️⃣  Add Block (Push)")
    print("2️⃣  Remove Block (Pop)")
    print("3️⃣  Show Tower")
    print("4️⃣  Exit Game")
    print("=============")

    choice = input("👉 Enter your choice (1-4): ")

    if choice == "1":
        block = input("Enter block name/color: ")
        stack.append(block)
        print(f"✅ Block '{block}' added to the tower!")

    elif choice == "2":
        if stack:
            removed = stack.pop()
            print(f"🧩 Block '{removed}' removed from the tower!")
        else:
            print("⚠️  No blocks to remove!")

    elif choice == "3":
        show_tower()

    elif choice == "4":
        print("👋 Thanks for playing Stack Tower Game!")
        break

    else:
        print("❌ Invalid choice! Please select between 1–4.")

