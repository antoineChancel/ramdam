# Ram.dam case study

Instructions : https://hello-ramdam.notion.site/Case-Study-Founding-AI-ML-Engineer-14cd54f28d1c80df9905c3c934f1e4bc

## Exercise 1 : Campaign Clusterization

### Data description

Dataset contains 706 campaigns in total

Columns (4)
- Campaign id : a unique identifier of a campaign (uuid)
- Product name : product name
  - no missing
  - contains duplicated products (388 unique values)
  - most represented products
    | product name | eff |
    |---|---|
    | Joko                              |35|
    | Mojo                              |20|
    | Yubo: Make friends in your way    |15|
    | Weward                            |11|
    | Ramdam Creator App                |11|
    | SwipeWipe                         | 9|
    | Wizz                              | 9|
    | WeWard                            | 8|
    | BeReal                            | 8|
    | Yubo: Make friends your way       | 8|
    | The Oregon Trail: Boom Town       | 8|
  - a product name can be
    - brand : "Yubo"
    - brand with motto : "Yubo: Find Your Online Besties"
    - vague product : "Assurance auto malus"
    -> Data input is an issue for quality please add form fields (brand, product category)
- Short description
  Contains product description or directly a brief
  - 4 data points with void or useless content Yubo, Octo, Ramdam test campaign, TextMe (probably user tests)
  - average length : 148 chars
  - 538 unique descriptions (some company may repeat the same short descriptions accross campaigns). Mojo copy pasted 11 times the description.
- Long description
  Vague or very detailed brief on the envisionned video
  - average length 500 chars
  - mention target consumers (australia, worldwide, ...)
  Can contain :
    - a tiktok/youtube link as a ref
    - a detailed brief with the objectives of the campaign
    - just the context of the industry -> want free ideas
    - very detailed video structure with bullet points
    - a hook and/or a script
    - focus on a particular feature

Languages found: English, French, German, Spanish, Portugese, Polish, Japanese (WeWard)

### Methodology

Axe our clustering on short description for this interview.

1. Data cleaning
  - Duplicate
2. Tokenization and embedding with different models of all data points
  - google-bert/bert-base-multilingual-cased (mean pooling on last hidden layer)
  - FacebookAI/xlm-mlm-100-1280 (too heavy to run on computer)
  - sentence-transformers/distiluse-base-multilingual-cased-v1
3. Kmeans / hierarchical clustering
  - elbow plot does not depict a relevant elbow
  - 20 clusters to grasp data complexity
  - Export cluster 20 vectors

### API

Framework async with FastAPI with one route `/cluster`.

To locally launch the application
```zsh
fastapi dev api.py
```

Note : no deployment of the solution

Clusters identifiers have been manually created from common topics found in the clusters. Their mapping is documented in the `clsuters.json` file.

Lifecycle of the solution -> collect feedback (like, dislike, no feedback) in order to improve the clustering.
- Retrain kmeans algorithm to improve the accuracy of the algorithm based on fresh data.

More ideas
- Investigate on misclustered data point
- Explore new embedding models as clustering is highly sensitive
- Labelize the data into meaningful categories and train a classification algorithm (easier to analyse and monitor)

## Exercise 2 : Optimal Pricing Strategy

Question & Thoughts
- What strategy would you propose?

I would like to have further insights on the evidences that lead to:
  - higher prices for finance campaign
  - is the number of applicants is a good target ?
I also lack the number of campaign we are talking.
My initial assumption would be to let the market (campaigner and creators) to trade to the best price (auction)
Collecting the fair prices according to campaingers expectations and creators traits can lead to meaningful pricing algorithm.

- How would you measure success (KPIs)?

Market is free, the objective as a broker is to have as many transation as we can. Charges fixed.

- How would you structure the process internally, including collaboration with teams?

Not sure to understand this question, to be brainstorm during the presentation

- Cold Start Solutions? Dynamic Clustering for Price Tiers?

No algorithm at the moment, passive collection of data and monitoring of transactions

- Implement a Scalable Rules Engine? (Develop a rules engine informed by AI that can adapt over time based on client feedback and new data?)

Regression tree based machine learning for price prediction to create buckets

