def estimator(data):

  result = {
    'data': data,
    'impact': {},
    'serverImpact': {}
  }

  result['impact'].update({
    'currentlyInfected': data['reportedCases'] * 10
  })
  result['serverImpact'].update({
    'currentlyInfected': data['reportedCases'] * 50
  })

  result['impact'].update({
    'infectionsByRequestedTime': result['impact']['currentlyInfected'] * (2**9)
  })
  result['serverImpact'].update({
    'infectionsByRequestedTime': result['impact']['currentlyInfected'] * (2**9)
  })

  result['serverImpact'].update({
    'severeCasesByRequestedTime': int((15/100) * result['impact']['infectionsByRequestedTime'])
  })

  result['impact'].update({
    'hospitalBedsByRequestedTime': 
      num_of_beds(data['totalHospitalBeds'], result['serverImpact']['severeCasesByRequestedTime'])
  })

  result['impact'].update({
    'casesForICUByRequestedTime': int((5/100) * result['impact']['infectionsByRequestedTime'])
  })

  result['impact'].update({
    'casesForVentilatorsByRequestedTime': int((2/100) * result['impact']['infectionsByRequestedTime'])
  })

  result.update({
    'dollarsInFlight': result['impact']['infectionsByRequestedTime'] * (65/100) * 1.5 * 30
  })

  
  return result

def num_of_beds(totalHopitalBeds, severeCasesByRequestedTime) -> int:
  '''Return numbers of available beds'''
  return totalHopitalBeds - severeCasesByRequestedTime


data = {
  'region': {
  'name': "Africa",
  'avgAge': 19.7,
  'avgDailyIncomeInUSD': 5,
  'avgDailyIncomePopulation': 0.71
  },
  'periodType': "days",
  'timeToElapse': 58,
  'reportedCases': 674,
  'population': 66622705,
  'totalHospitalBeds': 1380614
}

print(estimator(data))