def calculate_premium(formula, variables):
    try:
        # Use Python's `eval` as a basic calculation engine
        result = eval(formula, {}, variables)
        print(f"Calculated BI Premium: {result}")
        return result
    except Exception as e:
        return f"Error in calculation: {str(e)}"
