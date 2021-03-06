import pandas as pd

## Load in corporate rate codes from csv or using in-line data frame below or codes_in = pd.read_csv('./input/marriott-codes-simple.csv', index_col=False)
codes_in = pd.DataFrame({
            'company': {0: '3M', 1: 'AAA', 2: 'AARP', 3: 'Accenture', 4: 'Advance Purchase Rate',5: 'Aetna',
                        6: 'Alaska Airlines',7: 'Allstate', 8: 'American Express', 9: 'Apple', 10: 'AT&T',
                        11: 'Bank of America', 12: 'Best Available Rate', 13: 'Boeing', 14: 'Chick-Fil-A', 15: 'Chrysler',
                        16: 'Citi', 17: 'Coca-Cola', 18: 'COX', 19: 'Dell', 20: 'Deloitte', 
                        21: 'Delta', 22: 'Disney', 23: 'Exxon', 24: 'FedEx', 25: 'Ford', 
                        26: 'GAP', 27: 'General Corporate Rate', 28: 'General Electric', 29: 'GM', 30: 'Google',
                        31: 'Government Rate', 32: 'IBM', 33: 'Intel', 34: 'JCPenney', 35: 'JPMorgan',
                        36: 'Kroger', 37: 'Leisure Rate', 38: 'Local Promotion Rate', 39: 'Lockheed Martin', 
                        40: 'Look No Further Rate', 41: 'Lowes', 42: 'Microsoft', 43: 'Morgan Stanley', 44: 'Nike', 45: 'Nissan', 
                        46: 'Northrop Grumman', 47: 'Oracle', 48: 'Pepsi', 49: 'Pfizer', 50: 'Proctor & Gamble', 
                        51: 'Prudential', 52: 'Qualcomm', 53: 'Raytheon', 54: 'SAP', 55: 'Shell', 
                        56: 'Sony', 57: 'Southwest Airlines', 58: 'Sprint', 59: 'Sun Microsystems', 60: 'Texas Instruments',
                        61: 'ThyssenKrupp', 62: 'Toshiba', 63: 'Toyota', 64: 'United Airlines', 65: 'UPS',
                        66: 'Wedding Rate', 67: 'Wells Fargo'},
            'code':    {0: 'MMM', 1: 'AAA', 2: 'ARP', 3: 'ACC', 4: 'ADP', 5: 'AET', 6: 'A70', 7: 'ALL', 8: 'AMX', 9: 'APL', 10: 'ATT',
                        11: 'BOA', 12: 'BAR', 13: 'BOE', 14: 'CFA', 15: 'DCX', 16: 'CIT', 17: 'COK', 18: 'COX', 19: 'DEL', 20: 'DTC', 
                        21: 'DLA', 22: 'DIS', 23: 'XOM', 24: 'FED', 25: 'FRD', 26: 'GAP', 27: 'CRP', 28: 'GEE', 29: 'GMC', 30: 'GGL',
                        31: 'GOV', 32: 'IBM', 33: 'INL', 34: 'JCP', 35: 'JPM', 36: 'KRO', 37: 'LRR', 38: 'LPR', 39: 'XML', 40: 'LNF', 
                        41: 'LOW', 42: 'MCO', 43: 'MOS', 44: 'NKE', 45: 'NIS', 46: 'NOR', 47: 'ORA', 48: 'PEP', 49: 'PFE', 50: 'PAG', 
                        51: 'PRU', 52: 'QUA', 53: 'RAY', 54: 'SAP', 55: 'SHL', 56: 'SON', 57: 'SW8', 58: 'SPR', 59: 'SUN', 60: 'TXI',
                        61: 'TSN', 62: 'TOS', 63: 'TOY', 64: 'UAL', 65: 'UPS', 66: 'W14', 67: 'WEL'}})