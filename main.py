# ------------------------------- Imports ------------------------------- #
import random                # Used to pick random cards from the deck
from arts import blackjack_logo   # ASCII art logo for the Blackjack game


# ------------------------------- Helper Functions ------------------------------- #
def add_card_user():
    """Add a random card to the user's deck and return updated total."""
    user.append(cards[random.randint(0, len(cards) - 1)])     # Add random card to user
    user_total = sum(user)                                    # Recalculate total
    return user_total


def add_dealer_card():
    """Add a random card to the dealer's deck and return updated total."""
    dealer.append(cards[random.randint(0, len(cards) - 1)])   # Add random card to dealer
    dealer_total = sum(dealer)                                # Recalculate total
    return dealer_total


# ------------------------------- Deck Setup ------------------------------- #
# Standard Blackjack values → Ace counts as 11, face cards count as 10
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# ------------------------------- Main Game Loop ------------------------------- #
while True:
    continue_status = input("\nDo you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()

    # Exit the game
    if continue_status == "no":
        break

    # Start a new game
    elif continue_status == "yes":

        print(f"{blackjack_logo}")    # Show Blackjack Logo

        # Reset hands for new game
        user = []
        dealer = []

        # Deal initial two cards each → start of Blackjack
        for _ in range(2):
            user.append(cards[random.randint(0, len(cards) - 1)])
            dealer.append(cards[random.randint(0, len(cards) - 1)])

        # Calculate starting totals
        user_total = sum(user)
        dealer_total = sum(dealer)

        # Show initial hands
        print(f"\nYour Cards: {user}, current score: {user_total}")
        print(f"Dealer's first card: {dealer[0]}")

        # ------------------------------- Immediate Blackjack Check ------------------------------- #
        if user_total == 21:
            print("\nYou have a Blackjack! You have Won!")
            break
        elif dealer_total == 21:
            print("\nDealer has a Blackjack! You have Lost!")
            break

        # ------------------------------- Player Turn: Hit or Stand ------------------------------- #
        while True:
            choice = input("\nType 'hit' to get another card. Type 'stand' to pass: ").lower()

            new_user_total = user_total

            # ------------------------------- Player Chooses HIT ------------------------------- #
            if choice == "hit":
                new_user_total = add_card_user()

                # Player busts (goes over 21)
                if new_user_total > 21:
                    print(f"\nYour Final Score: {new_user_total}. You have crossed! You lost!")
                    break
                else:
                    print(f"\nYour Cards: {user}, current score: {new_user_total}")
                    print(f"Dealer's first card: {dealer[0]}")

            # ------------------------------- Player Chooses STAND ------------------------------- #
            elif choice == "stand":

                new_dealer_total = dealer_total

                # Dealer draws cards until reaching 16+
                while new_dealer_total < 16:
                    new_dealer_total = add_dealer_card()

                # Dealer busts
                if new_dealer_total > 21:
                    print(
                        f"\nYour Final hand: {user}, final score: {user_total}\n"
                        f"Dealer Final hand: {dealer}, final score: {new_dealer_total}. Dealer crossed!"
                    )
                    print("\nYou Have Won!")
                    break

                # Player wins
                elif new_user_total > new_dealer_total:
                    print(
                        f"\nYour Final hand: {user}, final score: {user_total}\n"
                        f"Dealer Final hand: {dealer}, final score: {new_dealer_total}"
                    )
                    print("\nYou have Won!")
                    break

                # Dealer wins
                elif new_dealer_total > new_user_total:
                    print(
                        f"\nYour Final hand: {user}, final score: {user_total}\n"
                        f"Dealer Final hand: {dealer}, final score: {new_dealer_total}"
                    )
                    print("\nDealer Won!")
                    break

                # Draw
                elif new_user_total == new_dealer_total:
                    print(
                        f"\nYour Final hand: {user}, final score: {user_total}\n"
                        f"Dealer Final hand: {dealer}, final_score: {new_dealer_total}"
                    )
                    print("\nThis is a Draw!")
                    break

            else:
                print("\nWrong Input")
                continue

    else:
        print("\nWrong Input")
        continue


# ------------------------------- Exit Message ------------------------------- #
print("\n\t\tGood Bye, See You Next Time! ")
