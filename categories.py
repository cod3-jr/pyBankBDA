'''
# Use | (i.e. or regEx symbol) to add description strings to a category
'''
cat = {
    # Auto
    'CAR TINTING|CAR CARE|CAR WASH' : 'Auto'
    ,'SERVICE STAT|GAS STATION' : 'Auto:Fuel'
    ,'B F & M INSURANCE' : 'Auto:Insurance'
    ,'T.C.D.' : 'Auto:License'
    ,'CAR PAYMENT' : 'Auto:Loan'
    ,'BERMUDA MOTORS|EXECUTIVE AUTO DETAILI|ISLAND CONSTRUCTION|WORLD DISTRIBUTORS LTD HAMILTON|ZIEBART' : 'Auto:Maintenance'
    ,'CORPORATION OF HAMILTO|EASYPARK MOBILE' : 'Auto:Parking'
    ,'HITCH.BM' : 'Auto:Taxi'
    
    # Baby
    ,'NEST MATERNITY' : 'Baby'
    ,'BLUKIDS' : 'Baby:Clothes'
    ,'DANCESATIONS' : 'Baby:Dance Class'
    ,'FIRST FRIENDS NURSERY' : {-1190.0 : 'Baby:Daycare',-910.0 : 'Baby:Daycare', -0.75 : 'Banking:Fees'}
    ,'DIAPERS|MEDICAL HOUSE LIMITED' : 'Baby:Diapers'
    ,'DR. TROTT & DR. MORANT' : 'Baby:OBGYN'
    ,'OCEAN ROCK WELLNESS' : 'Baby:Pediatrician'

    # Banking
    ,'FEE' : 'Banking:Fees'
    ,'INTEREST' : 'Banking:Interest'

    # C - D
    ,'ATM' : 'Cash'
    ,'BANDCAMP' : 'Dizzle'
    ,'LNRP YEAR SUBSCRIPTION' : 'Dizzle:Services'
    ,'WIKIPEDIA': 'Donations'

    # Food
    ,'BURROWS LIGHTBOURN|SPIRITS|THE BIRDCAGE WARWICK|TWO ROCK WINE COMPANY|WINE' : 'Food:Alcohol'
    ,'TUCK SHOP' : 'Food:Bakery'
    ,'BELCO CAFETERIA' : 'Food:BELCo'
    ,'BAKERY|BUZZ|DANGELINI|GLAZE|HAMILTON PASTRY SH' : 'Food:Coffee'

    ,' BAR| BISTRO|BULLI.SOCIAL|CAFE |CASABLANCA| DINNER|DEVIL\'S ISLE PEMBROKE|GENEROSAS|HOUSE OF INDIA|HARRY\'S|KITCHEN|MISAKI|MR CHICKEN|PICKLED ONION AND BREW|PIZZA HOUSE|PUB| RESTAUR|ROBIN HOOD HAMILTON| RUBY MURRYS|SARGASSO SEA|SPECIALITY INN LTD. SMITHS|SWIZZLE INN|TAKE FIVE LTD|THE LOREN|THE REEFS|VILLAGE PANTRY' : 'Food:Dining'
    
    ,'BOUQUET GARNI|DROP IT DELIVERY|GROCERIES|LINDO\'S FAMILY FOODS|MARKET|MODERN MART|SHOPPING CENTRE|SUPERMART|WADSON\'S' : 'Food:Groceries'

    #Gifts
    ,'DAVIDROSE LTD' : 'Gifts'

    # Household
    ,'GORHAM\'S|MASTERS' : 'Household'
    ,'SEARS HOMETOWN STORE' : 'Household:Appliances'
    ,'ANYELA DE OUTERBRIDGE' : 'Household:Cleaning'
    ,'CPR CELL PHONE REPAIR' : 'Household:Electronics'
    ,'CONSPEC' : 'Household:Furniture'
    ,'BERMUDA ZOOLGOICAL|MEMBERSHIP' : 'Household:Memberships'
    ,'BERMUDA ENGINEERING COMPANY LIMITED' : 'Household:Solar Panels'
    ,'SETAPP|1PASSWORD|PARALLELS' : 'Household:Software'
    ,'FREISENBRUCH MEYER' : 'Insurance:House'
    ,'HSBC BANK OF BERMUDA-PIPER GARDENS' : 'Maintenance Fee'

    # Medical
    ,'KERIN ORAL CARE' : 'Medical:Dentist'
    ,'SOMERS MEDICAL SERVICE' : 'Medical:Doctor'
    ,'COLLECTORS HILL APOTHE|PHARMACY|PHOENIX CENTRE|WOODBOURNE CHEMIST' : 'Medical:Prescriptions'
    ,'VISION' : 'Medical:Vision'

    # Mortgage
    ,'MTG INT PYMT' : 'Mortgage:Interest'
    ,'MTG PRIN PYMT' : 'Mortgage:Principle'
    
    # P - R
    ,'PET' : 'Pet'
    ,' RENT' : 'Rent'
    ,'BOAT DAY|SPA' : 'Recreation'

    # Salary
    ,'DUPREE G G|ELECT PYMNT DUPREE|ELECT PYMNT BERMUDA ELECTRIC LIG EDI|MISCHA G FUBLER|MONTHLY CONTRIBUTION|FROM:  MISCHA' : 'Salary:Net'

    # Shopping
    ,'BERMUDA CRAFT MARK' : 'Shopping' #TODO: extend to consider card number
    ,'W. J. BOYLE & SON' : 'Shopping:Shoes'
    ,'SEA VENTURE OVERSEAS SHIPPING' : 'Shopping:Shipping'

    # Tax
    ,'FCPT ' : 'Tax'
    ,'BDA GOV-HM CUSTOMS-KSK' : 'Tax:Duty'
    ,'OFFICE OF THE TAX COMM' : 'Tax:Land'

    #Teaching
    
    ,'SPELLCITY| DEPOT|SIG POS TRANS (\d+) TEACHERSPAYTEACHERS' : 'Teaching' # If purchase in foreign currency need to include prefix
    ,'HAIR STUDIO' : 'Toiletries:Hair Care'
    ,'ACNE CLINI' : 'Toiletries:Skin Care'

    # Utilities
    ,'BELCO Bill|BELCO Payment|UM2|ASCENDANT GROUP BELCO' : 'Utilities:Electricity'
    ,'SIG POS TRANS (\d+) DIGICEL DING' : 'Utilities:Mobile Phone'
    ,'COMMUNICATIONS' : {-149.55 : 'Utilities:Internet', -169.95 : 'Utilities:Internet', -84.95 : 'Utilities:Internet:Mom', -95.00 : 'Utilities:Internet:Mom'}
}