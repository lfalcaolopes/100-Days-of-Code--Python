from news import News
from stock import Stock
from twilio.rest import Client

# twilio_SID = "https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1"
# twilio_token = "https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1"
phone = +17853673661

news = News()
stock = Stock()

if stock.enough_variation():
    news_info = news.get_news()

    client = Client(twilio_SID, twilio_token)

    for index in range(len(news_info)):
        text = f"""
    {stock.code}: {stock.symbol}{stock.percentage_variation}%
    Headline: {news_info[index]["title"]}  
    Brief: {news_info[index]["description"]}\n
    """

        print(text)

        # message = client.messages.create(
        #     body=text,
        #     from_='whatsapp:+14155238886',
        #     to='whatsapp:+557791814996'
        # )

    # print(message.status)
