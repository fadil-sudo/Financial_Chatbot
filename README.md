Advanced Financial Chatbot Prototype (NLP-Based) - Documentation

1. How the Chatbot Works
------------------------
This enhanced chatbot utilizes foundational Natural Language Processing (NLP) concepts—specifically **Intent Classification** and **Entity Extraction**—to handle user queries dynamically. Instead of relying on rigid keyword matching, the system processes text through a three-stage pipeline:

1. **Preprocessing:** The user's input is stripped of leading/trailing whitespaces and converted entirely to lowercase to ensure case-insensitivity.
2. **Intent Classification (`intent_classification`):** The system analyzes the query against predefined lists of synonyms (keywords). For example, if a user types "profit", "laba", or "net profit", the chatbot successfully classifies the user's intent as `get_net_income`.
3. **Entity Extraction (`entity_extraction`):** The chatbot scans the input to extract key parameters required to answer the query: the target company (`microsoft`, `tesla`, or `apple`) and the fiscal year (`2023`, `2024`, or `2025`).

Once both the **Intent** and **Entities** are successfully mapped, the chatbot triggers its decision logic to deliver the exact financial figure retrieved from the verified 10-K filings.

2. Predefined Queries It Can Answer
----------------------------------
Thanks to the flexible synonym-mapping framework, the chatbot can understand varied natural language phrasing for the following financial metrics:

- **Total Revenue:** Understands phrases including *revenue, sales, turnover, earnings, top line*. (e.g., *"What are Microsoft's sales for 2025?"*)
- **Net Income:** Understands phrases including *net income, profit, laba, net profit, bottom line*. (e.g., *"How much profit did Tesla make in 2025?"*)
- **Total Assets:** Understands phrases including *assets, property, wealth, holdings*. (e.g., *"Show me Apple's total holdings in 2024."*)
- **Session Control:** Gracefully terminates the command-line interaction loop when the user types `"exit"` or `"quit"`.

3. Chatbot Limitations
----------------------
Despite its structural upgrade toward professional AI engineering patterns, this prototype still operates within specific guardrails:

- **Dictionary-Bound NLP:** The intent classification relies on explicit synonym arrays. If a user inputs a term entirely missing from the keyword dictionary, the bot will fail to classify the intent (unlike an LLM or semantic search vector embedding model).
- **Static Hardcoded Scope:** The chatbot does not query a live file or an external database dynamically; the data combination answers remain hardcoded inside the logic block based on the Task 1 analysis.
- **No Out-of-Scope Fallback:** It cannot process unstructured analytical prompts, generate text summaries, or answer questions regarding other fiscal years or companies outside the current dataset. Unmatched intent/entity combinations will prompt a default fallback messaging.

Update note: I applied the requested updates to the code. This README now contains the documentation you provided. If you also want the previous GitHub push instructions preserved, tell me and I will add them to a "Getting Started" section.

