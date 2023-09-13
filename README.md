# OnlyFund
Where is my money at?

**All information stored under the current repository is strictly private and not allowed to be shared beyond the authors of the repository.**


# Project Overview

1. **Alpha Signal Mining**: Discovering insider trading signals across trading data and written documents.
    - Model feed can be information across both written and numeric data (legal discolures, regular fillings, and third-party summarized data)
    - Signals are focused on **noticeable changes** of trading activities from insider.
2. **Investment Thesis Research** : Leveraging big data and LLM models, target is rationalizing signals detected from insider trading activities through all types of data could be found from the market.
    - Examples of Training Data Types: Company Capital Structure, Company Board of Directors Name List, News, Financials, Tax Fillings, Quarterly Updates, Investor Calls, Sell-side Research Reports, Recent Market Prefermance. 
3. **Trading Idea Generation**: Relying on educational materials from professional sources, a seperate trained model could better advise on how to construct a trading strategy to profit from validated thesis (strategy will be primarily focus on Equity Options to amplify returns from insider trading signals). 
    - Examples of Sources: CME group, Investopedia, Bloomberg, CFA Insititution, Capital IQ, WeChat 公众号（中金等）


Note: Executions can currently rely on paper portfolio or self recorded order book data to track performance history.



# Process

1. https://www.insider-monitor.com/resource.html -> LLM
2. Market Data -> Yahoo Finance API (Model: GAN)
3. Lasso Regression -> 
