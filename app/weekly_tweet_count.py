import mysql.connector
import requests
import os
import json

my_conn=mysql.connector.connect(
    user = os.environ.get("DB_USER"),
    password = os.environ.get("DB_PASS"),
    db = os.environ.get("DB_NAME"),
    host = os.environ.get("DB_HOST"),
)

bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/counts/recent"

def weekly_update():
    my_cursor = my_conn.cursor()
    my_cursor.execute("SELECT Symbol FROM nasdaq_tickers")
    ticker_list = my_cursor.fetchall()

    for x in range(300, 400):
        ticker = ticker_list[x][0]
        query_params = {'query': f'{ticker} lang:en', 'granularity': 'day'}

        def bearer_oauth(r):
            """
            Method required by bearer token authentication.
            """

            r.headers["Authorization"] = f"Bearer {bearer_token}"
            r.headers["User-Agent"] = "v2RecentTweetCountsPython"
            return r

        def connect_to_endpoint(url, params):
            response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
            print(response.status_code)
            if response.status_code != 200:
                raise Exception(response.status_code, response.text)
            return response.json()

        def main():
            json_response = connect_to_endpoint(search_url, query_params)
            #print(json.dumps(json_response, indent=4, sort_keys=True))
            total_count = int(json.dumps(json_response['meta'].get('total_tweet_count')))
            rs = my_cursor.execute("UPDATE nasdaq_tickers SET count = %s WHERE Symbol = '%s'" % (total_count, ticker))
            my_conn.commit()
            print(f"{ticker} count is {total_count}.")
            print("Rows updated = ", rs.rowcount)

        if __name__ == "__main__":
            main()

weekly_update()
