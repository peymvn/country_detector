import json

def country_detector(text):

  with open('Countries.json') as json_file:
    country_dict = json.load(json_file)

  country_list = []
  for country in country_dict:

    try:
      # country name
      if country.name.lower() in text.lower():
        if not country.alpha_3 in country_list: # if this country is not already detected
          country_list.append(country.alpha_3)
    except:
        pass

    try:
      # country alpha_2 (US, IR, ...) 
      if country.alpha_2 in text: # do not make the text lower to avoid misunderestanding of ALPHA 2 code with some words (like: us)
        if not country.alpha_3 in country_list: # if this country is not already detected
          country_list.append(country.alpha_3)
    except:
      pass

    try:
      # country alpha_3 (USA, IRI, ...) 
      if country.alpha_3 in text: # do not make the text lower to avoid misunderestanding of ALPHA 2 code with some words (like: us)
        if not country.alpha_3 in country_list: # if this country is not already detected
          country_list.append(country.alpha_3)
    except:
      pass

    try:
      # country official name 
      if country.official_name.lower() in text.lower():
        if not country.alpha_3 in country_list: # if this country is not already detected
          country_list.append(country.alpha_3)
    except:
      pass

    try:
      # country common_name name
      if country.common_name.lower() in text.lower():
        if not country.alpha_3 in country_list: # if this country is not already detected
          country_list.append(country.alpha_3)
    except:
      pass

      
    try:
      # country other_names name
      if any([for c in country.other_names.lower().split()] in text.lower()):
        if not country.alpha_3 in country_list: # if this country is not already detected
          country_list.append(country.alpha_3)
    except:
      pass


  return country_list
