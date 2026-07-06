def intent_classification(query):
    """Simple NLP function to detect user intent"""
    # Keyword synonyms to expand chatbot understanding
    revenue_keywords = ['revenue', 'sales', 'turnover', 'earnings', 'top line']
    net_income_keywords = ['net income', 'profit', 'earnings', 'net profit', 'bottom line']
    assets_keywords = ['assets', 'property', 'wealth', 'holdings']
    
    if any(word in query for word in revenue_keywords):
        return "get_revenue"
    elif any(word in query for word in net_income_keywords):
        return "get_net_income"
    elif any(word in query for word in assets_keywords):
        return "get_assets"
    elif "exit" in query or "quit" in query:
        return "exit"
    else:
        return "unknown"

def entity_extraction(query):
    """Simple NLP function to extract entities (Company & Year)"""
    companies = ['microsoft', 'tesla', 'apple']
    years = ['2023', '2024', '2025']
    
    # Search for the mentioned company
    target_company = None
    for company in companies:
        if company in query:
            target_company = company
            break
            
    # Search for the mentioned year
    target_year = None
    for year in years:
        if year in query:
            target_year = year
            break
            
    return target_company, target_year

def advanced_chatbot(user_query):
    # Standard NLP preprocessing: clean text
    query = user_query.strip().lower()
    
    # Step 1: Detect Intent
    intent = intent_classification(query)
    
    # Step 2: Extract Entities
    company, year = entity_extraction(query)
    
    # Exit if user requests it
    if intent == "exit":
        return "Goodbye!"
    
    # Step 3: Decision Logic based on Intent & Entity
    if intent == "get_revenue" and company == "microsoft" and year == "2025":
        return "Chatbot: The total revenue for Microsoft in 2025 is $287,510 million."
    elif intent == "get_net_income" and company == "tesla" and year == "2025":
        return "Chatbot: Tesla's net income in 2025 is $3,794 million."
    elif intent == "get_assets" and company == "apple" and year == "2024":
        return "Chatbot: The total assets for Apple in 2024 is $364,980 million."
    
    # Fallback message if intent/entity combination is incomplete or missing
    else:
        return f"Chatbot: Sorry, I understood your intent as '{intent}' for '{company}' in '{year}', but that specific data combination is not in my database."

# Interactive Loop
print("=== Welcome to the NLP-Based Financial Chatbot ===")
print("Try typing with synonyms (e.g., 'profit' instead of 'net income')\n")

while True:
    user_input = input("You: ")
    response = advanced_chatbot(user_input)
    print(response)
    
    if "goodbye" in response.lower():
        break