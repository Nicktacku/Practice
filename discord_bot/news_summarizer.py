from bs4 import BeautifulSoup
from requests import get
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

# gets the news from rappler, all credits to them


def get_news():
    URL = "https://www.rappler.com/"

    page = get(URL)
    rappler = BeautifulSoup(page.text, "html.parser")

    top_news = rappler.find(class_="post-card__title-top-stories")
    top_news_link = top_news.find("a")["href"]

    top_page = get(top_news_link)
    news = BeautifulSoup(top_page.text, "html.parser")
    title = news.find(class_="post-single__title").text
    publish_date = news.find("time").text
    body = news.find(class_="post-single__content entry-content")
    contents = body.find_all("p")

    text = "".join([content.text for content in contents])
    # Object of automatic summarization.
    auto_abstractor = AutoAbstractor()
    # Set tokenizer.
    auto_abstractor.tokenizable_doc = SimpleTokenizer()
    # Set delimiter for making a list of sentence.
    auto_abstractor.delimiter_list = [".", "\n"]
    # Object of abstracting and filtering document.
    abstractable_doc = TopNRankAbstractor()
    # Summarize document.
    result_dict = auto_abstractor.summarize(text, abstractable_doc)

    summarized_news = list(result_dict["summarize_result"])
    return (title, publish_date, "\n".join(summarized_news))
