#!/usr/bin/env python3

import argparse
import json
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools

def initialize_analyticsreporting():
  """Initializes an analyticsreporting service object.
  
  Parameters:
  -----------
    None.
      It only needs the variables listed below in order to authenticate

  Returns:
  --------
    analytics:
      analytics an authorized analyticsreporting service object.
  """

  #Initializing the authentication process
  SCOPES = 'https://www.googleapis.com/auth/analytics.readonly'
  DISCOVERY_URI = 'https://analyticsreporting.googleapis.com/$discovery/rest'
  KEY_FILE_LOCATION = 'client_secrets.p12'
  SERVICE_ACCOUNT_EMAIL = ''
  VIEW_ID = ''

  try:
    credentials = ServiceAccountCredentials.from_p12_keyfile(SERVICE_ACCOUNT_EMAIL, KEY_FILE_LOCATION, scopes=SCOPES)

    http = credentials.authorize(httplib2.Http())

    # Build the service object.
    analytics = build('analytics', 'v4', http=http, discoveryServiceUrl=DISCOVERY_URI)
    return analytics
  except:
    raise

def get_report(analytics):
    """ Use the Analytics Service Object to query the Analytics Reporting API V4.
    
    Parameters:
    -----------
    analytics(obj):
    	The analytics object contructed.

    Returns:
    --------
    	The dictionary with all the responses to the request
    """
    query = {"reportRequests": 
              [{"viewId": "XXXXXX", "dateRanges":[{"startDate": "yesterday","endDate": "today"}],
              "metrics": [{"expression": "ga:sessions"}, 
                          {"expression": "ga:sessionDuration"},
                          {"expression": "ga:avgTimeOnPage"},
                          {"expression": "ga:adClicks"},
                          {"expression": "ga:adCost"},
                          {"expression": "ga:CPM"},
                          {"expression": "ga:CPC"},
                          {"expression": "ga:pageValue"},
                          {"expression": "ga:pageviews"}],
              "dimensions": [{"name": "ga:campaign"}]
              }]
            }

    try:
      return analytics.reports().batchGet(body = query).execute()
    except:
      raise

def print_response(response):
  """Parses and prints the Analytics Reporting API V4 response

  Parameters:
  -----------
  response(dict)
  	the response from the APIs request

  Returns:
  --------
  	None
  """

  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    rows = report.get('data', {}).get('rows', [])

    for row in rows:
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])

      for header, dimension in zip(dimensionHeaders, dimensions):
        print (header + ': ' + dimension)

      for i, values in enumerate(dateRangeValues):
        print( 'Date range (' + str(i) + ')')
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          print (metricHeader.get('name') + ': ' + value)

def to_json(response, filename):
  """ Function that saves response into json file
  
  Parameters:
  ----------- 
  response(dict):
    the response to the request
  filename(string):
    filename to save the response on

  Returns:
  --------
    exception in case there is some error along the code
  """
  try:
    write_json = open('{}.json'.format(filename), 'w')
    json.dump(response, write_json, indent = 4)
    write_json.close()
  except:
    raise

def main():
  """ Function the calls the authentication, get the response of the analytics report, and saves into a json file
  """

  analytics = initialize_analyticsreporting()
  response = get_report(analytics)
  #print_response(response)
  to_json(response, 'filename')

if __name__ == '__main__':
  main()