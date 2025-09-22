#Pet Rock Simulator

print("Welcome to the Pet Rock Simulator, your job is to take care of your pet over the in game days.")
print("Good Luck!")

def main():
    name = input("What will you name your pet rock? ")

    happiness = 5
    health = 5
    max_stat = 10
    min_stat = 0

    print(f"\nMeet your new pet rock, {name}!")

    while True:

        print(f"\n--- Your Pet Rock, {name} ---")
        print(f"Happiness: {happiness}/{max_stat}")
        print(f"Health:    {health}/{max_stat}")

        if happiness <= min_stat:
            print(f"\n{name} became too sad and rolled away. GAME OVER.")
            break
        if health <= min_stat:
            print(f"\n{name} cracked from poor health. GAME OVER.")
            break

        print("\nWhat do you want to do?")
        print("1. Feed the rock")
        print("2. Play with the rock")
        print("3. Do nothing")
        choice = input("Your choice: ")

        if choice == "1":
            health += 2
            happiness -= 1
            print(f"You fed {name}. (+2 Health, -1 Happiness)")

        elif choice == "2":
            happiness += 2
            health -= 1
            print(f"You played with {name}. (+2 Happiness, -1 Health)")

        elif choice == "3":
            print("You do nothing...")

        else:
            print("The Rock is in shock. (Invalid choice)")

        health -= 1
        happiness -= 1

        health = max(min_stat, min(health, max_stat))
        happiness = max(min_stat, min(happiness, max_stat))

if __name__ == "__main__":
    main()