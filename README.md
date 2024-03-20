<h1>Project Update:</h1>
<p>
Due to the recent price adjustment to the Twitter API, maintaining the live version of Trending Plays has become financially unsustainable. The difficult decision has been made to discontinue the live service associated with this project.

Despite this setback, the repository will remain available as a showcase of the work done and a resource for those interested in the project's technical aspects.
</p>

<h1>Trending Plays</h1>

Trending Plays is a web application that allows users to view the top 10 trending NASDAQ stocks on Twitter over the past 7 days. The application uses the Twitter API to track the number of tweets for each stock and displays the top 10 on the website.

This can be used as part of research when trading options or day trading.

<h2>Prerequisites :clipboard:</h2>

To run Trending Plays, you will need the following:

* Python 3.8 or later
* pip
* Flask
* A Twitter API bearer token.
* a MySQL Server (or any of your choice)
* Docker (optional)

<h2>Creating the database table :wrench:</h2>

1. Import the `nasdaq.json` file into a new database. The latest file can be downloaded [here](https://datahub.io/core/nasdaq-listings).

```
mysql -u <username> -p <database_name> < nasdaq.json
```

2. Create a new table named `nasdaq_tickers` with the following columns:

* `symbol`: VARCHAR(10)
* `count`: INT

```
CREATE TABLE nasdaq_tickers (
    symbol VARCHAR(10)
    count INT
);
```

3. Insert the ticker symbols from the `nasdaq.json` file into the `symbol` column of the `nasdaq_tickers` table.

```
INSERT INTO nasdaq_tickers(symbol)
SELECT symbol from nasdaq;
```

4. Make sure the table is created and the symbols are added.

```
SELECT * FROM nasdaq_tickers;
```

You should now have a `nasdaq_tickers` table in your database with all the ticker symbols from the `nasdaq.json` file. The count column will be used to store the number of tweets for each symbol, which will be updated by the `weekly_tweet_count.py` script.

<h2>Installation :computer:</h2>

1. Clone the repository to your local machine:

```
git clone https://github.com/karenastevens/trendingstocks.git

```

2. Navigate to the root directory of the project and create a new file named .env. Inside this file, add the following lines, replacing BEARER_TOKEN with your Twitter API bearer token and the DB variables with your database credentials where the tweet counts are being updated and held:

```
FLASK_DEBUG=true
SECRET_KEY= randomly generated key for flask
DB_USER= database username
DB_PASS= database password
DB_NAME= database name
DB_HOST= database host
BEARER_TOKEN= your unique bearer token
```

3. Install the Python dependencies:

```
pip install -r requirements.txt
```

<h2>Running the application :running:</h2>

<h3>Option 1: Without Docker</h3>

1. Start the Flask development server:

```
export FLASK_APP=app.py
flask run
```

2. In a separate terminal windown, you can run the tweet count script to update the information in the database:

```
python3 weekly_tweet_count.py
```

The application is set to grab the lastest information from the database with each request to keep the top 10 as accurate as possible:
```
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
```

4. Open your web browser and navigate to `http://localhost:5000/` (or whichever port you chose to have it listen on)

You should now be able to view the application in your web browser. If you make any changes to the code, you will need to restart the Flask development server for the changes to take effect.

<h2>Upcoming Features :seedling:</h2>

:heart: User will be able to click on each ticker to view more information, such as real-time stock prices and other market data

:heart: User will be able to click on each ticker to view recent news surrounding the company
