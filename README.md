# Zillow Real Estate Data Scraper 🏡

This project scrapes real estate listing data from Zillow, cleans it, and prepares it for market price analysis.

## Features
- Automated data extraction (Requests / BeautifulSoup)
- Data cleaning and normalization (Pandas)
- Export to Excel/CSV for reporting
- Reusable code structure for scaling to any city or region

## Example Use Cases
| Use Case | Result |
|---------|--------|
| Price comparison between neighborhoods | Identify cheaper investment areas |
| Airbnb / Rental pricing analysis | Estimate nightly/monthly rates |
| Real estate flipping research | Detect undervalued properties |

## Files in This Project
| File | Purpose |
|------|---------|
| `zillow_scraper.py` | Main scraper script |
| `zillow_scraper_clean.py` | Clean & processed version |
| `zillow_data.xlsx` | Exported example dataset |

## How to Run
```bash
pip install -r requirements.txt
python zillow_scraper.py
