<h1>Trending Plays</h1>

Trending Plays is a web application that allows users to view the top 10 trending NASDAQ stocks on Twitter over the past 7 days. The application uses the Twitter API to track the number of tweets for each stock and displays the top 10 on the website.

This can be used as part of research when trading options or day trading.

<h2>Upcoming Features :seedling:</h2>

:heart: User will be able to click on each ticker to view more information, such as real-time stock prices and other market data

:heart: User will be able to click on each ticker to view recent news surrounding the company

<h2>Prerequisites :clipboard:</h2>

To run Trending Plays, you will need the following:

* Python 3.8 or later
* pip
* Flask
* A Twitter API bearer token (you can get one [here](href="https://developer.twitter.com/en").
* a MySQL Server (or any of your choice)
* Docker (optional)

<h2>Installing :computer:</h2>

1. Clone the repository to your local machine:

```
git clone https://github.com/karenastevens/trendingstocks.git

```

2. Navigate to the root directory of the project and create a new file named .env. Inside this file, add the following lines, replacing BEARER_TOKEN with your Twitter API bearer token and the DB variables with your database credentials where the tweet counts are being updated and held:

```
FLASK_DEBUG=true
SECRET_KEY=YOUR_RANDOMLY_GENERATED_KEY_FOR_FLASK
DB_USER=YOUR_DATABASE_USERNAME
DB_PASS=YOUR_DATABASE_PASSWORD
DB_NAME=YOUR_DATABASE_NAME
DB_HOST=YOUR_DATABASE_HOST
BEARER_TOKEN=YOUR_BEARER_TOKEN
```

3. Install the Python dependencies:

```
pip install -r requirements.txt
```

<h2>Running the application :running:</h2>

<h3>Option 1: Without Docker</h3>
