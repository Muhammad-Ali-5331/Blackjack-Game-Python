# 🃏 Blackjack Game

This project is a command-line implementation of the classic Blackjack card game. It allows users to play against a dealer, simulating the core mechanics of Blackjack, including dealing cards, calculating scores, handling user input, and determining win/loss conditions. The game provides a simple and interactive way to experience Blackjack directly from the terminal.

## 🚀 Features

- **Interactive Gameplay:** Engage in a command-line Blackjack experience, making decisions to "hit" or "stand."
- **Card Dealing Simulation:** Randomly deals cards from a virtual deck, ensuring fair and unpredictable gameplay.
- **Score Calculation:** Automatically calculates the total value of the user's and dealer's hands, considering the special rules for Aces.
- **Win/Loss Determination:** Accurately determines the winner based on Blackjack rules, including handling busts (exceeding 21).
- **ASCII Art Integration:** Features a visually appealing Blackjack logo using ASCII art for an enhanced user experience.
- **Game Loop:** Play multiple rounds of Blackjack without restarting the application.

## 🛠️ Tech Stack

- **Language:** Python
- **Random Module:** Used for card shuffling and dealing simulation.
- **arts.blackjack_logo:** ASCII art for the game's logo.

## 📦 Installation

### Prerequisites

- Python 3.6 or higher

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  (Optional) Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install any dependencies (if applicable - create a `requirements.txt` if needed):

    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

1.  Run the `main.py` file:

    ```bash
    python main.py
    ```

2.  Follow the on-screen prompts to play the game. You'll be asked to start a new game, and then prompted to "hit" or "stand" during your turn.

## 📂 Project Structure

```
blackjack_game/
├── main.py
├── arts/
│   └── blackjack_logo.py  # (Optional: If the logo is in a separate file)
├── README.md
└── ...
```

## 📸 Screenshots

<p align="center">
  <img src="https://raw.githubusercontent.com/Muhammad-Ali-5331/Blackjack-Game-Python/main/Screenshot2.png" alt="Blackjack Game Screenshot 2" width="49%">
  <img src="https://raw.githubusercontent.com/Muhammad-Ali-5331/Blackjack-Game-Python/main/Screenshot1.png" alt="Blackjack Game Screenshot 1" width="49%">
</p>

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests with bug fixes, improvements, or new features.

## 📝 License

This project is licensed under the [MIT License](https://github.com/Muhammad-Ali-5331/Blackjack-Game-Python/blob/main/LICENSE) - see the `LICENSE` file for details.

## 📬 Contact

If you have any questions or suggestions, feel free to reach out:

Muhammad Ali - malitariq5324@gmail.com

## 💖 Thanks Message

Thank you for checking out this Blackjack game! We hope you enjoy playing it and find it a useful example of a command-line application.
