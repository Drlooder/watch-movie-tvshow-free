# Watch Movie & TV Show Free 🎬

A Python application that allows you to stream movies and TV shows listed on IMDB.com for free!

---

## 📋 Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Credits & Acknowledgments](#credits--acknowledgments)

---

## ✨ Features

- **Search & Stream Movies**: Search for any movie listed on IMDB and stream it
- **TV Show Support**: Watch TV shows with season and episode selection
- **Automatic API Key Generation**: Auto-generate OMDB API keys using temporary email addresses
- **Multiple API Key Management**: Store and manage multiple API keys with usage tracking
- **Interactive CLI Menu**: User-friendly command-line interface with stylish branding

---

## 📦 Requirements

- Python 3.7 or higher

### Python Dependencies

Install the packages listed in `requirements.txt`:

- `requests` - For making HTTP requests to APIs
- `temp-mail` - For generating temporary email addresses
- `pyfiglet` - For ASCII art text formatting

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Drlooder/watch-movie-tvshow-free.git
cd watch-movie-tvshow-free
```

### Step 2: Install Required Dependencies

#### Option A: Using requirements.txt (Recommended)

```bash
pip install -r requirements.txt
```

#### Option B: Manual Installation

Install each package individually:

```bash
pip install requests
pip install temp-mail
pip install pyfiglet
```

### Step 3: Run the Application

```bash
python main.py
```

The application will start and display an interactive menu.

---

## 💻 Usage

Once you run the application, you'll see a menu with these options:

### Main Menu Options:

1. **Watch** - Search for a movie or TV show to stream
   - Type the exact name of the movie/TV show from IMDB
   - Select your preferred season and episode (for TV shows)
   - Stream directly in your default browser

2. **Generate new API key** - Create a new OMDB API key
   - Automatically generates a temporary email
   - Creates and activates a new API key
   - Saves it for future use

3. **Select API key** - Choose from your saved API keys
   - View all available keys and their usage statistics
   - Switch between different keys

4. **Exit** - Close the application

### Example Usage:

```
[+] Made by Drlooder
[+] For more tools Github: https://github.com/Drlooder

[1] Watch
[2] Generate new API key
[3] Select API key
[4] Exit
.> 1

[+] - Type !Exit to close.
Enter Name.> The Matrix
```

---

## 👏 Credits & Acknowledgments

This project was built thanks to the contributions and services of the following:

### Special Thanks To:

- **[OMDB API](https://www.omdbapi.com/)** - Provides comprehensive movie and TV show information from IMDB
  - Used to fetch movie details, plot summaries, and TV show information
  - Essential for the core functionality of this application

- **[VidAPI](https://vidapi.ru/)** - Provides the video streaming service
  - Handles the actual streaming of movies and TV shows
  - Integrates with the player for seamless viewing experience

- **[cardisnotvalid](https://github.com/cardisnotvalid)** - Creator of the [10MinuteMail.net](https://github.com/cardisnotvalid/10MinuteMail.net) library
  - Enables temporary email generation
  - Allows automated OMDB API key creation without manual registration
  - Makes the setup process seamless and automatic

- **[Drlooder](https://github.com/Drlooder)** - Project Creator & Maintainer
  - Built and maintains this amazing streaming tool
  - Check out more tools on GitHub: https://github.com/Drlooder

---

## 🐛 Troubleshooting

### Issue: "Unactivated api"
- The API key hasn't been properly activated
- Try generating a new API key from the menu option 2

### Issue: Can't find movie/TV show
- Use the exact title as it appears on IMDB
- Check spelling and formatting

### Issue: Streaming doesn't open
- Ensure your default web browser is configured
- The application creates an `index.html` file and opens it in your browser

---

## 📄 License

This project is for educational and personal use. Please respect the terms of service of OMDB API and VidAPI.

---

**Happy Streaming! 🍿🎬**

For more projects and tools, visit: **https://github.com/Drlooder**
