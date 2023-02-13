def loan_repayment_calculator(loan_amount, loan_term, interest_rate, repayment_frequency):
    # Interest rate per repayment period
    interest_rate_per_repayment = interest_rate / (12 / repayment_frequency)
    # Total interest to be paid over the loan term
    total_interest = 0
    # Total amount to be repaid over the loan term
    total_repayment = 0
    # Repayment period amount
    repayment_amount = loan_amount * (interest_rate_per_repayment / (1 - (1 + interest_rate_per_repayment) ** -loan_term))
    # Table of loan repayments over the loan term
    repayment_table = []

    # Loop through each repayment period
    for i in range(1, loan_term + 1):
        # Interest for the current period
        interest = loan_amount * interest_rate_per_repayment
        # Principal for the current period
        principal = repayment_amount - interest
        # Update total interest and total repayment
        total_interest += interest
        total_repayment += repayment_amount
        # Update remaining balance
        loan_amount -= principal
        # Append the current period information to the repayment table
        repayment_table.append({
            'Period': i,
            'Principal': principal,
            'Interest': interest,
            'Repayment': repayment_amount,
            'Balance': loan_amount
        })

    # Return the results
    return {
        'Total Interest': total_interest,
        'Total Repayment': total_repayment,
        'Repayment Table': repayment_table
    }

# print(loan_repayment_calculator(5000, 2, 1.4, 12))
