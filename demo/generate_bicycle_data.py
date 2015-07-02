
import pandas as pd
import bicycledataprocessor as bdp

dataset = bdp.DataSet()
run = bdp.Run('00283', dataset, filterFreq=10.0)

# Create a pandas data frame that can be exported to csv with
# phi, delta, phid, deltad, psi, Tdelta, Tdeltad

name_map = {
    'SteerAngle': 'delta',
    'RollAngle': 'phi',
    'RollRate': 'phid',
    'YawAngle': 'psi',
    'SteerRate': 'deltad',
    'PullForce': 'F',
    'SteerTorque': 'T_delta',
    'ForwardSpeed': 'v'
}

data = {}

for k, v in name_map.items():
    data[v] = run.taskSignals[k]

data['Td_delta'] = run.taskSignals['SteerTorque'].time_derivative()
data['time'] = run.taskSignals['SteerAngle'].time()

df = pd.DataFrame(data)

df.to_csv('bicycle-measurements.csv')
