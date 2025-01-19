# CSC790 Information Retrieval

Below is a high-level outline of features and interaction modes I might include in an advanced IR application—one that aims to follow the major topics from the *Introduction to Information Retrieval* (Manning, Raghavan, and Schütze) textbook. This will help guide my UI/UX design and overall architecture. I’ll focus on conceptual “modes” or “states” that map nicely to stacked widgets or tabs, and how they might be arranged in a typical three-panel (left/right/center) layout with PyQt6.

---

## 1. Document Acquisition / Data Management Mode

### **Purpose & Topics**
- Demonstrate how documents are collected, imported, and managed in an IR system.
- Covers crawling, file ingestion, metadata extraction, database (MySQL) population, etc.

### **Possible UI Elements**
- **Left/Side Panel**: 
  - **Data Source Configuration**: 
    - Options to select data source types (local file system, web crawler, API endpoints, etc.).
    - Fields to specify paths or URLs.
    - Start/Stop buttons for crawling or import processes.
  - **Logs / Status**: Display real-time logs or a progress bar indicating ongoing ingestion processes.

- **Central Panel**:
  - **Document Listings**:
    - A table/list showing ingested documents (filename, title, date, source URL, etc.).
    - Additional metadata columns (author, file size, etc.).
  - **Detail / Preview Area** (possibly a sub-split or a stacked widget child):
    - A mini-preview of a selected document or extracted metadata (show first lines, highlight important fields, etc.).
    - If relevant, allow quick edits or tagging/categorizing.

- **Right/Side Panel**:
  - **Controls / Pipeline Options**: 
    - Checkboxes or combo boxes to enable/disable certain steps (e.g., “Ignore duplicates,” “Extract images,” “Ignore binary files,” etc.).
    - Scheduling settings (e.g., specify times or intervals for crawls).
  - **Database Settings** (for demonstration):
    - Quick config for MySQL parameters or alternative DBs.
    - Buttons to “Flush DB,” “Export DB,” or “Import Settings.”

---

## 2. Preprocessing & Text Normalization Mode

### **Purpose & Topics**
- Let users set up and demonstrate typical IR preprocessing pipelines: tokenization, case normalization, stopword removal, stemming/lemmatization, language detection, etc.
- Illustrates the difference each step can make to the final token stream or index.

### **Possible UI Elements**
- **Left/Side Panel**:
  - **Preprocessing Pipeline Configuration**:
    - Drag-and-drop or checkbox list for operations: 
      1. Tokenization method (whitespace, regex-based, etc.)
      2. Case-folding
      3. Stopword removal
      4. Stemming vs. lemmatization
      5. Handling punctuation, numbers, etc.
    - Buttons to apply the pipeline to sample data or entire dataset.
  - **Language Settings** (if multilingual corpus):
    - Choose NLTK or spaCy pipelines, etc.

- **Central Panel**:
  - **Before/After Comparison**:
    - A two-column view that shows raw text on the left and processed text tokens on the right.
    - Possibly color-coded or highlighted transformations (e.g., show removed stopwords in red, final tokens in green).

- **Right/Side Panel**:
  - **Statistics**:
    - Count of tokens before/after.
    - Vocabulary size.
    - Distribution plots (e.g., top words by frequency).
  - **Logs / Explanations**:
    - Any warnings, errors, or debug statements regarding preprocessing (e.g., “Language not detected,” “Encountered malformed text,” etc.).

---

## 3. Index Creation & Management Mode

### **Purpose & Topics**
- Show how to build different types of indexes (inverted index, positional index, etc.).
- Demonstrate weighting schemes (TF-IDF, BM25, etc.).
- Possibly incorporate compression, skipping, or other advanced indexing features.

### **Possible UI Elements**
- **Left/Side Panel**:
  - **Index Configuration**:
    - Choose index structure (basic inverted index, positional index, n-gram index, etc.).
    - Select weighting schemes (TF, TF-IDF, BM25, etc.).
    - Toggle compression or advanced features (delta encoding, skip pointers, etc.).
  - **Index Build Controls**:
    - Buttons: “Build Index,” “Update Index,” “Clear Index.”
    - Status/progress bar during index construction.

- **Central Panel**:
  - **Index Explorer**:
    - A hierarchical or table-based display of index terms.
    - For each term, show postings list (document IDs, term frequencies, positions).
    - Optionally a separate tab for term statistics (df, idf, etc.).
  - **Visualization** (optional):
    - Graph or chart to illustrate distribution of indexing terms, postings lengths, etc.

- **Right/Side Panel**:
  - **Index Summary & Statistics**:
    - Number of unique terms, total tokens indexed.
    - Average postings list length, largest postings list term, etc.
  - **Index Snapshots**:
    - If you want to demonstrate the evolution of an index over time or partial indexing, provide a snapshot list or checkpoint mechanism.

---

## 4. Basic & Advanced Search Mode

### **Purpose & Topics**
- Demonstrate Boolean retrieval, vector space retrieval (TF-IDF, cosine similarity), BM25, query expansion, relevance feedback, etc.
- Compare search modes and display different ranking algorithms side-by-side if desired.

### **Possible UI Elements**
- **Left/Side Panel**:
  - **Query Input & Controls**:
    - A text field or multi-line input for queries.
    - Toggle among different retrieval models (Boolean, Vector Space, Probabilistic/BM25, etc.).
    - Additional toggles for:
      - Wildcard / fuzzy search
      - Synonym expansion
      - Relevance feedback (pseudo or user-driven)
  - **Search History**:
    - A list of past queries for quick recall and comparison.

- **Central Panel**:
  - **Search Results**:
    - Display list of matching documents (title, snippet/highlighted text, score).
    - Possibly a multi-tab approach to show how each retrieval model ranks results differently.
    - On selecting a document, open a detail view (or a sub-pane) with more text highlights.

- **Right/Side Panel**:
  - **Advanced Query Controls**:
    - Faceted search (if you have category/metadata info).
    - Filters (date ranges, author, file type).
    - Sort orders (by date, by ranking score, etc.).
  - **Interactive Relevance Feedback** (if implemented):
    - A place to mark results as relevant/irrelevant and re-run the query to see updated ranking.

---

## 5. Evaluation & Benchmarking Mode

### **Purpose & Topics**
- Show standard IR metrics (Precision, Recall, F1, MAP, nDCG, etc.).
- Let users evaluate how changes in indexing or retrieval affect system performance.

### **Possible UI Elements**
- **Left/Side Panel**:
  - **Evaluation Configuration**:
    - Import or define a set of ground truth queries and relevance judgments (TREC-style QREL).
    - Select which metrics to compute (Precision@k, Recall, MAP, nDCG).
    - Buttons to run evaluation across multiple retrieval models or index variants.

- **Central Panel**:
  - **Results Table**:
    - Rows for each query, columns for each metric and retrieval model.
    - Possibly color-coded to highlight best performance per metric.
  - **Charts / Graphs**:
    - Precision-Recall curves.
    - Bar charts for MAP or nDCG comparisons.

- **Right/Side Panel**:
  - **Statistical Analysis**:
    - Paired t-tests, confidence intervals, or other significance testing (if you want to be thorough).
  - **Logs / Summaries**:
    - Plain-text summary of results, insights, or suggestions based on the metrics.

---

## 6. Advanced Topics & Experimental Mode

Depending on how much depth you want, you could dedicate a separate “mode” or set of tabs to cover more advanced topics from *Introduction to Information Retrieval*. These might include:

- **Clustering & Classification**:
  - Implement or demonstrate k-means clustering of documents, hierarchical clustering, or text classification (Naive Bayes, SVM, etc.).
  - Visualization of clusters or classification results.

- **Latent Semantic Analysis (LSA) / Topic Modeling**:
  - Show how to build an LSA-based index or run LDA to discover topics in the corpus.
  - Visualization of topic distributions and document-topic relationships.

- **Learning to Rank**:
  - Experiment with machine learning-based ranking models (RankSVM, LambdaMART, etc.).
  - Panels to upload training data, train a model, then compare performance to classic models.

- **Neural IR / Embedding-based Retrieval**:
  - Integration with word embeddings (Word2Vec, GloVe) or BERT-like models for semantic search.
  - Compare dense vector search vs. sparse “classic” indexes.

- **Entity Linking, Knowledge Graph integration**:
  - If you want to demonstrate how entity extraction can enrich retrieval.

Each advanced module could follow the same overall layout pattern (left: configuration, center: data/results, right: stats/logs).

---

## High-Level Interaction Flow

Below is a brief idea of how a user might flow through your application:

1. **Document Acquisition**: User sets up data sources, ingests documents, and sees them in a repository list.  
2. **Preprocessing**: User configures how the text is cleaned/tokenized/stemmed. They run it on the dataset and see how it changes the tokens.  
3. **Indexing**: User selects the type of index and weighting scheme, then builds the index. They can explore terms and postings.  
4. **Searching**: User enters queries, toggles different retrieval models, sees results. Possibly interacts with feedback or expansions.  
5. **Evaluation**: User uploads relevance judgments, runs evaluations across models, sees metrics. Compares which approach works best.  
6. **Advanced Features** (optional): Clustering, classification, LSA, neural IR, etc., each in its own dedicated mode/tab.

---

## Putting It All Together in PyQt6

- **Main Window**:
  - **QSplitter** or nested splitters:
    - **Left Panel**: Typically for mode-specific controls, pipeline configurations, or data sources.
    - **Central Panel**: The primary display area (lists, results, charts, previews).
    - **Right Panel**: Secondary/auxiliary controls, logs, advanced settings, or statistics.  

- **Stacked Widgets**:
  - One approach is to have a *top-level tab bar* or a *mode selector* on the left (like a vertical list) that changes the central and right panels’ stacked widgets. For each mode, you load the relevant UI components.

- **Qt Designer**:
  - You can design each “mode” or “state” as a `.ui` file, or as a custom widget, then embed them in a QStackedWidget or QTabWidget.  
  - Reuse design patterns: each mode likely has a “configuration panel” on the left, a “results/visualization panel” in the center, and a “stats/logs panel” on the right.  

- **Backend Integration**:
  - For demonstration purposes, you can have a “core IR library” in Python that handles ingestion, preprocessing, indexing, searching, etc., and your PyQt6 front-end just calls those library methods and displays results.  
  - For MySQL or other DB integration, keep it modular so that you can swap out different DB backends or even in-memory data structures.

---

## Final Thoughts

1. **Simplicity First**: Start with the basic pipeline (acquisition → preprocessing → indexing → search → evaluation). Only after you have that stable do you add more advanced features.
2. **Transparency and Visualization**: IR concepts can be abstract. Visual aids (charts, tables, side-by-side comparisons) make it easier to demonstrate what’s happening under the hood.
3. **Comparisons**: One of the most instructive things is to let users quickly compare, e.g., “Boolean vs. TF-IDF vs. BM25.” Emphasize toggles, side-by-side results, or multi-tab displays.
4. **Extensibility**: Make sure your design is modular so you can plug in new retrieval models, indexing methods, or data sources down the line.

This feature set and mode-based layout should cover a large portion of what *Introduction to Information Retrieval* discusses, and it’ll give you ample room to demonstrate and experiment with every step of the IR pipeline. Good luck with your PyQt6 development!