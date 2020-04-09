def estimator(data):

  result = {
    'impact': {},
    'serverImpact': {}
  }

  result['impact'].update({
    'currentlyInfected': data['reportedCases'] * 10
  })
  
  result['impact'].update({
    'infectionsByRequestedTime': result['impact']['currentlyInfected'] * (2**9)
  })
  result['impact'].update({
    'severeCasesByRequestedTime': int((15/100) * result['impact']['infectionsByRequestedTime'])
  })
  result['impact'].update({
    'hospitalBedsByRequestedTime': num_of_beds(data['totalHospitalBeds'], result['impact']['severeCasesByRequestedTime'])
  })
  result['impact'].update({
    'casesForICUByRequestedTime': int((5/100) * result['impact']['infectionsByRequestedTime'])
  })
  result['impact'].update({
    'casesForVentilatorsByRequestedTime': int((2/100) * result['impact']['infectionsByRequestedTime'])
  })
  result['impact'].update({
    'dollarsInFlight': result['impact']['infectionsByRequestedTime'] * (65/100) * 1.5 * 30
  })



  result['serverImpact'].update({
    'currentlyInfected': data['reportedCases'] * 50
  })
  result['serverImpact'].update({
    'infectionsByRequestedTime': result['serverImpact']['currentlyInfected'] * (2**9)
  })
  result['serverImpact'].update({
    'severeCasesByRequestedTime': int((15/100) * result['serverImpact']['infectionsByRequestedTime'])
  })
  result['serverImpact'].update({
    'hospitalBedsByRequestedTime': 
      num_of_beds(data['totalHospitalBeds'], result['serverImpact']['severeCasesByRequestedTime'])
  })
  result['serverImpact'].update({
    'casesForICUByRequestedTime': int((5/100) * result['serverImpact']['infectionsByRequestedTime'])
  })
  result['serverImpact'].update({
    'casesForVentilatorsByRequestedTime': int((2/100) * result['serverImpact']['infectionsByRequestedTime'])
  })
  result['serverImpact'].update({
    'dollarsInFlight': result['serverImpact']['infectionsByRequestedTime'] * (65/100) * 1.5 * 30
  })

  
  return {'data': data, 'estimate': result}

def num_of_beds(totalHopitalBeds, severeCasesByRequestedTime) -> int:
  '''Return numbers of available beds'''
  return totalHopitalBeds - severeCasesByRequestedTime
