default_selectors = {
            "author" : ['span.user-post__author-name'],
            "recommendation" : ['span.user-post__author-recomendation > em'],
            "stars" : ['span.user-post__score-count'],
            "content" : ['div.user-post__text'],
            "pros" : ["div.review-feature__col:has(> div[class*=\"positives\"]) > div.review-feature__item", True],
            "cons" : ["div.review-feature__col:has(> div[class*=\"negatives\"]) > div.review-feature__item", True],
            "purchased" : ['div.review-pz'],
            "submit_date" : ["span.user-post__published > time:nth-child(1)"],
            "purchase_date" : ["span.user-post__published > time:nth-child(2)"],
            "useful" : ["span[id^='votes-yes']"],
            "useless" : ["span[id^='votes-no']"]
        }

def extract_element(opinion, selector, attribute = None):
    try:
        if attribute:
            if isinstance(attribute, str):
                return opinion.select(selector).pop(0)[attribute].strip()
            else:
                return [x.get_text().strip() for x in opinion.select(selector)]
        else:
            return opinion.select(selector).pop(0).get_text().strip()
    except IndexError:
        return attribute