from news_summarizer import get_news


def get_response(message):
    p_message = message.lower()

    if p_message == "hello":
        return "world"
    if p_message == "news":
        news = get_news()
        return f"**Title:** {news[0]}\n**Date:** {news[1]}\n\n{news[2]}"
