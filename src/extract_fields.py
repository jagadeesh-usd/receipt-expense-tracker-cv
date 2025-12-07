import re
from typing import Optional, Dict, List
from datetime import datetime
from dateutil import parser as date_parser  # dateutil is robust for many formats
import math

# Regex patterns
CURRENCY_NUM_RE = re.compile(r'([0-9]{1,3}(?:[,][0-9]{3})*(?:\.[0-9]{2})|[0-9]+(?:\.[0-9]{2}))')
AMOUNT_LABEL_RE = re.compile(
    r'(?i)\b(total|amount|grand total|grand|balance|invoice total|total amount|amount due|net amt|grandtotal)\b[:\s]*\$?\s*([0-9,]+\.\d{2})'
)
DATE_RE_LIST = [
    # common mm/dd/yyyy or dd/mm/yyyy variants
    re.compile(r'\b(0?[1-9]|1[0-2])[\/\-.](0?[1-9]|[12][0-9]|3[01])[\/\-.](\d{2,4})\b'),
    # yyyy-mm-dd
    re.compile(r'\b(20\d{2})[\/\-.](0?[1-9]|1[0-2])[\/\-.](0?[1-9]|[12][0-9]|3[01])\b'),
    # textual months: 12 Jan 2020, Jan 12, 2020
    re.compile(r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*[ \-\.]?\d{1,2}[,]?[ \-\.]?[0-9]{2,4}\b', re.I),
    re.compile(r'\b\d{1,2}[ \-\.](?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*[ \-\.]?[0-9]{2,4}\b', re.I),
]

VENDOR_HEURISTICS_BLACKLIST = [
    "total", "subtotal", "amount", "gst", "tax", "invoice", "taxable", "bill", "qty",
    "item", "change", "tender", "cash", "visa", "mastercard", "****", "www", "http"
]

def normalize_number_str(s: str) -> Optional[float]:
    """Turn common currency-like strings into float or None."""
    if not s:
        return None
    s = s.replace(',', '').strip()
    s = re.sub(r'[^0-9\.\-]', '', s)
    try:
        return float(s)
    except Exception:
        return None

def find_total_in_text(full_text: str) -> Optional[float]:
    """Try label-first then fallback numeric-last strategies."""
    text = full_text
    # 1) labeled amounts (prefer last labeled)
    matches = list(AMOUNT_LABEL_RE.finditer(text))
    if matches:
        # choose the last labeled amount
        for m in reversed(matches):
            v = m.group(2)
            num = normalize_number_str(v)
            if num is not None:
                return num

    # 2) fallback: take the last currency-format number in the document
    nums = CURRENCY_NUM_RE.findall(text)
    if nums:
        # last candidate
        val = nums[-1]
        num = normalize_number_str(val)
        if num is not None:
            return num

    return None

def find_date_in_text(full_text: str) -> Optional[str]:
    """Return date string in ISO format (YYYY-MM-DD) if possible, else raw match."""
    text = full_text
    # Try dateutil first for robust parsing on any substring
    # We'll look for candidate substrings using regex windows
    # First try the explicit regex list
    for patt in DATE_RE_LIST:
        m = patt.search(text)
        if m:
            candidate = m.group(0)
            try:
                dt = date_parser.parse(candidate, dayfirst=False, fuzzy=True)
                return dt.date().isoformat()
            except Exception:
                return candidate

    # As fallback, attempt to parse any text token that looks like a date
    tokens = re.split(r'[\\n\\r\\t\\s,]+', text)
    for tok in tokens:
        if len(tok) < 6 or len(tok) > 10:
            continue
        try:
            dt = date_parser.parse(tok, fuzzy=False, dayfirst=False)
            return dt.date().isoformat()
        except Exception:
            continue
    return None

def guess_vendor_from_lines(lines):
    """
    Heuristic: vendor is usually in the first few non-empty lines that are not numeric/labels.
    """
    if not lines:
        return None

    candidate_lines = [l.strip() for l in lines if l and l.strip()]
    top = candidate_lines[:6]

    for l in top:
        low = l.lower()

        if any(b in low for b in VENDOR_HEURISTICS_BLACKLIST):
            continue

        # skip lines that are mostly numbers or very short
        word_count = len(low.split())
        letters = sum(c.isalpha() for c in low)
        if letters < 2:
            continue
        if word_count <= 5:
            return l

    return candidate_lines[0] if candidate_lines else None

def extract_fields_from_ocr_result(ocr_result: Dict) -> Dict:
    """
    ocr_result: dict with keys 'lines' (list[str]) and 'full_text' (str) and optionally 'raw'.
    Returns: dict with vendor, date, total (float), and confidence placeholders.
    """
    full_text = ocr_result.get('full_text', '')
    lines = ocr_result.get('lines', [])
    vendor = guess_vendor_from_lines(lines)
    date = find_date_in_text(full_text)
    total = find_total_in_text(full_text)
    return {"vendor": vendor, "date": date, "total": total}