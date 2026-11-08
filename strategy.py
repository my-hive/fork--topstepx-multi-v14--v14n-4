"""v14n-4: overnight equity inventory premium; one entry per session.
Completed-bar stop trigger, next-open execution; gap loss can exceed declaration.
"""
import numpy as np
from numba import njit

PARAMS = {'start': 3600, 'end': 30600, 'risk': 250.0, 'size': 1}
# Exchange dollar/point specifications, not fitted parameters.
POINT_VALUE = {'ES': 50, 'MES': 5, 'NQ': 20, 'MNQ': 2, 'YM': 5,
               'MYM': .5, 'RTY': 50, 'M2K': 5, 'NKD': 5,
               'CL': 1000, 'MCL': 100, 'QM': 500, 'NG': 10000, 'MNG': 1000}

@njit
def _targets(sec, close, low, op, session, times, contract, start, end, distance, size):
    out = np.zeros(len(sec), dtype=np.int64)
    active = False
    used = False
    anchor = 0.0
    for i in range(len(sec)):
        if i == 0 or session[i] != session[i-1]:
            active = False
            used = False
        if i > 0 and (times[i] - times[i-1] != 60_000_000_000 or contract[i] != contract[i-1]):
            active = False
        window = (sec[i] >= start or sec[i] < end) if start > end else start <= sec[i] < end
        if active:
            if out[i-1] == 0:
                anchor = op[i]
            if not window or low[i] <= anchor - distance:
                active = False
        if not used and window and sec[i] >= start:
            active = True
            used = True
            anchor = close[i]
        if active:
            out[i] = size
    return out

def signals(panel):
    result = {}
    for symbol, df in panel.items():
        session = df.session.to_numpy().astype('datetime64[D]').astype(np.int64)
        result[symbol] = _targets(df.ct_sec.to_numpy(), df.close.to_numpy(),
            df.low.to_numpy(), df.open.to_numpy(), session,
            df.index.as_unit('ns').asi8, df.contract.astype('category').cat.codes.to_numpy(),
            PARAMS['start'], PARAMS['end'],
            PARAMS['risk'] / (POINT_VALUE[symbol] * PARAMS['size']), PARAMS['size'])
    return result

def entry_risk(panel):
    return {s: np.full(len(d), PARAMS['risk'] / PARAMS['size']) for s, d in panel.items()}

if __name__ == '__main__':
    import pandas as pd
    idx = pd.date_range('2020-01-01 23:00', periods=3, freq='min', tz='UTC')
    df = pd.DataFrame({'session': pd.Timestamp('2020-01-02'),
        'ct_sec': [3600, 3660, 3720], 'close': [100., 100., 100.],
        'low': [100., 100., 100.], 'open': [100., 100., 100.], 'contract': 'ESH0'}, index=idx)
    assert signals({'ES': df})['ES'].tolist() == [1, 1, 1]
    df.index = idx[:2].append(idx[2:] + pd.Timedelta(minutes=1))
    assert signals({'ES': df})['ES'].tolist() == [1, 1, 0]
