from urllib.parse import urlparse

SOURCE_CREDIBILITY = {
    # International trusted news
    "bbc.com": 0.95,
    "reuters.com": 0.97,
    "apnews.com": 0.96,
    "nytimes.com": 0.92,
    "washingtonpost.com": 0.91,
    "theguardian.com": 0.90,
    "cnn.com": 0.85,

    # Indian trusted news
    "thehindu.com": 0.90,
    "indianexpress.com": 0.88,
    "hindustantimes.com": 0.87,
    "ndtv.com": 0.86,
    "timesofindia.indiatimes.com": 0.84,

    # Tech / business
    "bloomberg.com": 0.94,
    "forbes.com": 0.85,
    "economist.com": 0.95,

    # Moderate / mixed credibility
    "news18.com": 0.75,
    "foxnews.com": 0.70,

    # Social media / blogs
    "medium.com": 0.60,
    "blogspot.com": 0.50,
    "wordpress.com": 0.50,

    # Default
    "unknown": 0.40
}


from typing import Optional

def get_source_credibility(url: Optional[str]) -> float:
    try:
        if not url:
            return SOURCE_CREDIBILITY["unknown"]

        domain = urlparse(url).netloc.replace("www.", "")
        return SOURCE_CREDIBILITY.get(domain, SOURCE_CREDIBILITY["unknown"])
    except:
        return SOURCE_CREDIBILITY["unknown"]
