# Suggestion_bot

A simple anonymous suggestion bot for Telegram channels.

This is a minimalist anonymous bot written in Python. It has no extra features — just the basics:  
sending text messages and pictures anonymously to a Telegram channel.  
It does **not** use a database, admin IDs, or store any user data.

This bot is useful for Telegram channel admins who want a plug-and-play solution without setting up complex infrastructure.  
It was originally created for a specific use case, so it includes some hardcoded Russian phrases — feel free to replace them with your own.

## Requirements

- Python 3.9 or higher
- Telegram Bot API token

## Getting Started

### Local Launch

```bash
# Clone the repository
git clone https://github.com/KleinerMarcel/Suggestion_bot.git
cd Suggestion_bot

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the bot
python bot_hp.py

#Docker Launch

# Build Docker image
docker build -t suggestion_bot .

# Run container with your Telegram token
docker run -e BOT_TOKEN=your_token_here suggestion_bot



#Notes
The bot uses some Russian-language strings. You can easily replace them in the source file (bot_hp.py).
You can expand it with additional functionality, such as moderation, logging, or admin controls.
