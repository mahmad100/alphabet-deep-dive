# Alphabet (GOOGL): The Price Assumes Stronger Returns on AI Investment

**Personal hobby project. For informational and educational purposes only, not investment advice. Model outputs
are assumption-dependent. Use at your own risk.**

My deep dive on Alphabet, October 2026: a presentation, the Excel model behind it, and a Monte Carlo notebook that
draws the model's uncertain inputs 10,000 times. Prices are as of the October 16, 2026 close ($340.59). Filed
figures run through the Q2 2026 Form 10-Q; the Q3 2026 results (October 28, 2026) are not reflected.

---

## What's in here

```
alphabet-deep-dive-oct2026.pdf   The presentation, 46 slides.
alphabet-model-oct2026.xlsx      The model: evidence sheets, a five-year forecast, three-scenario DCF,
                                 reverse DCF, audits, sources and a change log.
alphabet-monte-carlo.ipynb       The Monte Carlo behind slide 30, with its outputs saved.
engine/engine.py                 A Python replica of the workbook's operating model and DCF, used by the notebook.
engine/scenarios_lib.py          Input overrides for the engine.
README.md                        This file.
```

## The view in brief

Under my assumptions, the model values Alphabet below the current price. The business is strong; the question is
what the AI build earns.

| | Value per share | Against $340.59 |
|---|---:|---:|
| Base case, DCF at the price date | $202.63 | -41% |
| Best case | $365.07 | +7% |
| Worst case | $80.57 | -76% |
| Scenarios weighted 25 / 50 / 25 | $213 | |
| Monte Carlo median (90% of draws $122 to $322) | $201 | |
| Forward multiples (P/E, EV/EBITDA) | $299 to $360 | |

- **Personal model label: Sell.** The twelve-month model value is $221: the base case at the price date, rolled
  forward a year at the 9.73% cost of equity, less dividends. That is a model-implied total return of about -35%.
  The label is my own classification, not a recommendation to trade.
- **The judgment that decides it** is the return on new capital after FY2030E, 15% in my base case. At 25% the
  base value rises by about $51; at 10% it falls by about $41. For a Hold, the base value would need to reach about
  $279.
- **Where my forecast differs from the Street:** operating income is 9% below consensus in FY2027 and 15% below in
  FY2028, on lower revenue and a lower margin.
- **Signals I would reassess on:** Cloud revenue added above 35 cents per dollar of prior-year capex, or Cloud
  margin holding above 35% as the build enters service.

The presentation sets out the evidence, the forecast against consensus, the scenarios, the risks and the full
method.

## Using the model

- Open `alphabet-model-oct2026.xlsx` in Excel and start at `00 Contents`. Blue cells are inputs, black are formulas
  on the same sheet, green are links to other sheets.
- One switch, `16 Scenarios` D6 (1 Base, 2 Best, 3 Worst), drives the visible model. Six hidden sheets hold fixed
  copies of the model for each case, so `20 DCF Valuation` values all three at once (row 29).
- The value at the price date, the twelve-month model value and the model label are on `11 Valuation` rows 85-99.
- `26 Pack Audit` and `27 Model Audit` test that the model's wiring is consistent. They do not test whether the
  assumptions are right.
- Every input that moves value is noted beside it, and `28 Sources` lists each source.

## Running the notebook

```bash
# from the top folder of this repository
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install numpy pandas matplotlib openpyxl jupyter
jupyter notebook alphabet-monte-carlo.ipynb
```

Run the cells top to bottom; a full run takes a minute or two. The notebook reads the workbook's saved values, first
checks that the engine reproduces the workbook's own results, then draws the inputs. The input distributions are
my judgments, stated in the notebook. The result describes uncertainty in the inputs around the base case, not
where the stock will trade.

## Sources

Alphabet's Form 10-K (FY2025) and Form 10-Q (Q1 and Q2 2026) and the Q2 2026 earnings call; StockAnalysis and
MarketScreener for prices, peer statistics and consensus; Damodaran for the equity risk premium and industry
betas; the U.S. Treasury and FRED for rates. The full list, with links, is on the last slide of the presentation
and on `28 Sources` in the workbook.

## Disclosures

- **Personal project.** I made this for fun and learning. "Ahmadi Research" is the name of my personal project,
  not a firm.
- **Informational use only.** Nothing here is investment, financial, legal or tax advice, or an offer or
  solicitation. It does not consider anyone's circumstances, objectives or risk tolerance.
- **Model labels and values.** Buy, Hold and Sell are personal model labels, and the twelve-month model value is a
  conditional model output. Neither is a prediction of the market price or an instruction to trade.
- **Uncertainty.** Forecasts depend on assumptions and can be wrong; outcomes can differ materially.
- **AI assistance.** Generative AI assisted with research and source gathering, filing checks, workbook construction
  and formulas, Python code (scenario engine, Monte Carlo), charts and slides, consistency checks, and drafting. I
  set the key assumptions and judgments and reviewed the work; that review is not a guarantee of accuracy. Data,
  citations, code and calculations may contain errors or omissions and should be independently verified. No
  independent audit was performed.
- **Verify before acting.** Check the information yourself and seek qualified advice before making any investment
  decision. Investments can lose value, including all of it.
- **Updates.** Views may change, and I make no commitment to update this material.
- **Interests.** I may hold or trade securities discussed, including Alphabet and peers, without notice.
- **Liability.** To the extent permitted by applicable law, I disclaim liability for reliance on this material.
  Nothing here excludes liability that cannot lawfully be excluded.

## Author

Mohammad Ahmadi
[GitHub](https://github.com/mahmad100)
