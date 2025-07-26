import re
from html import unescape

def extract_clean_text(html: str) -> str:
    matches = re.findall(
        r'<span[^>]*class="[^"]*dash-letter[^"]*"[^>]*>(.*?)</span>',
        html,
        re.IGNORECASE | re.DOTALL
    )

    characters = []
    for m in matches:
        if '<' in m:  # ignore spans that contain tags like <img>
            continue
        characters.append(unescape(m))

    raw_text = ''.join(characters)
    return re.sub(r'\s+', ' ', raw_text).strip()