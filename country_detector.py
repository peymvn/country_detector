import json
import re

def country_detector(text):

  with open('/content/country_detector/Countries.json') as json_file:
    country_dict = json.load(json_file)

  country_list = []
  for country in country_dict['Countries']:

    try:
      # country name
      if country['name'].lower() in text.lower():
        if not country['alpha_3'] in country_list: # if this country is not already detected
          country_list.append(country['alpha_3'])
    except:
        pass

    try:
      # country alpha_2 (US, IR, ...)
      m = re.findall('\\b' + country['alpha_2'] + '\\b', text)
      if bool(m): # do not make the text lower to avoid misunderestanding of ALPHA 2 code with some words (like: us)
        if not country['alpha_3'] in country_list: # if this country is not already detected
          country_list.append(country['alpha_3'])
    except:
      pass

    try:
      # country alpha_3 (USA, IRI, ...) 
      m = re.findall('\\b' + country['alpha_3'] + '\\b', text)
      if bool(m): # do not make the text lower to avoid misunderestanding of ALPHA 3 code with some words (like: us)
        if not country['alpha_3'] in country_list: # if this country is not already detected
          country_list.append(country['alpha_3'])
    except:
      pass

    try:
      # country official name 
      if country['official_name'].lower() in text.lower():
        if not country['alpha_3'] in country_list: # if this country is not already detected
          country_list.append(country['alpha_3'])
    except:
      pass

    try:
      # country common_name name
      if country['common_name'].lower() in text.lower():
        if not country['alpha_3'] in country_list: # if this country is not already detected
          country_list.append(country['alpha_3'])
    except:
      pass

      
    try:
      # country other_names ||| other_names contains splitted single words representing one probable form of that country
      for c in country['other_names'].lower().split():
        if c in text.lower():
          if not country['alpha_3'] in country_list: # if this country is not already detected
            country_list.append(country['alpha_3'])
    except:
      pass


  return country_list
