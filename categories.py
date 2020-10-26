# Use | (or) to add description strings to a category
cat = {
    # Auto
    'CAR TINTING|CAR CARE|CAR WASH' : 'Auto'
    ,'SERVICE STAT|GAS STATION' : 'Auto:Fuel'
    ,'B F & M INSURANCE' : 'Auto:Insurance'
    ,'T.C.D.' : 'Auto:License'
    ,'CAR PAYMENT' : 'Auto:Loan'
    ,'BERMUDA MOTORS|WORLD DISTRIBUTORS LTD HAMILTON|EXECUTIVE AUTO DETAILI' : 'Auto:Maintenance'
    ,'CORPORATION OF HAMILTO|EASYPARK MOBILE' : 'Auto:Parking'
    ,'HITCH.BM' : 'Auto:Taxi'
    
    # Baby
    ,'DIAPERS|MEDICAL HOUSE LIMITED' : 'Baby:Diapers'
    ,'DR. TROTT & DR. MORANT' : 'Baby:OBGYN'
    ,'OCEAN ROCK WELLNESS' : 'Baby:Pediatrician'

    # Banking
    ,'FEE' : 'Banking:Fees'
    ,'INTEREST' : 'Banking:Interest'

    # C - D
    ,'ATM' : 'Cash'
    ,'BANDCAMP' : 'Dizzle'

    # Food
    ,'BURROWS LIGHTBOURN|SPIRITS|THE BIRDCAGE WARWICK|WINE' : 'Food:Alcohol'
    ,'BELCO CAFETERIA' : 'Food:BELCo'
    ,'BAKERY|BUZZ|DANGELINI|GLAZE|HAMILTON PASTRY SH' : 'Food:Coffee'

    ,' BAR| BISTRO|BULLI.SOCIAL|CAFE |CASABLANCA| DINNER|DEVIL\'S ISLE PEMBROKE|HOUSE OF INDIA|HARRYS|KITCHEN|MISAKI|PICKLED ONION AND BREW|PUB| RESTAUR| RUBY MURRYS|SARGASSO SEA|SPECIALITY INN LTD. SMITHS|SWIZZLE INN|TAKE FIVE LTD|THE LOREN|THE REEFS|VILLAGE PANTRY' : 'Food:Dining'
    
    ,'BOUQUET GARNI|DROP IT DELIVERY|GROCERIES|LINDOS FAMILY FOODS|MARKET|MODERN MART|SHOPPING CENTRE|SUPERMART' : 'Food:Groceries'

    # Household
    ,'GORHAM\'S' : 'Household'
    ,'ANYELA DE OUTERBRIDGE' : 'Household:Cleaning'
    ,'BERMUDA ENGINEERING COMPANY LIMITED' : 'Household:Solar Panels'
    ,'FREISENBRUCH MEYER' : 'Insurance:House'
    ,'HSBC BANK OF BERMUDA-PIPER GARDENS' : 'Maintenance Fee'

    # Medical
    ,'KERIN ORAL CARE' : 'Medical:Dentist'
    ,'SOMERS MEDICAL SERVICE' : 'Medical:Doctor'
    ,'PHARMACY|PHOENIX CENTRE|WOODBOURNE CHEMIST' : 'Medical:Prescriptions'
    ,'VISION' : 'Medical:Vision'

    # Mortgage
    ,'MTG INT PYMT' : 'Mortgage:Interest'
    ,'MTG PRIN PYMT' : 'Mortgage:Principle'
    
    # P - R
    ,'PET' : 'Pet'
    ,' Rent' : 'Rent'

    # Salary
    ,'DUPREE G G|ELECT PYMNT DUPREE|ELECT PYMNT BERMUDA ELECTRIC LIG EDI|MISCHA G FUBLER|MONTHLY CONTRIBUTION|FROM:  MISCHA' : 'Salary:Net'

    # Shopping
    ,'SEA VENTURE OVERSEAS SHIPPING' : 'Shopping:Shipping'

    # Tax
    ,'FCPT ' : 'Tax'
    ,'BDA GOV-HM CUSTOMS-KSK' : 'Tax:Duty'
    
    ,' DEPOT|SIG POS TRANS (\d+) TEACHERSPAYTEACHERS' : 'Teaching' # If purchase in foreign currency need to include prefix
    ,'HAIR STUDIO' : 'Toiletries:Hair Care'

    # Utilities
    ,'BELCO Bill|BELCO Payment|UM2' : 'Utilities:Electricity'
    ,'SIG POS TRANS (\d+) DIGICEL DING' : 'Utilities:Mobile Phone'
}