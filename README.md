# Ram.dam case study

Instructions : https://hello-ramdam.notion.site/Case-Study-Founding-AI-ML-Engineer-14cd54f28d1c80df9905c3c934f1e4bc

## Data description

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

## Methodology

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

## API

Framework async with FastAPI

```zsh
fastapi dev api.py
```
