"""v14n-4: overnight equity inventory premium; one entry per session.
Completed-bar stop trigger, next-open execution; gap loss can exceed declaration.
"""
import numpy as np
from numba import njit

PARAMS = {'start': 61200, 'end': 30600, 'risk': 250.0, 'size': 1}
# Exchange dollar/point specifications, not fitted parameters.
POINT_VALUE = {'ES': 50, 'MES': 5, 'NQ': 20, 'MNQ': 2, 'YM': 5,
               'MYM': .5, 'RTY': 50, 'M2K': 5, 'NKD': 5,
               'CL': 1000, 'MCL': 100, 'QM': 500, 'NG': 10000, 'MNG': 1000}

@njit
def _targets(sec, close, low, op, session, start, end, distance, size):
    out = np.zeros(len(sec), dtype=np.int64)
    active = False
    used = False
    anchor = 0.0
    for i in range(len(sec)):
        if i == 0 or session[i] != session[i-1]:
            active = False
            used = False
        window = sec[i] >= start or sec[i] < end
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
            PARAMS['start'], PARAMS['end'],
            PARAMS['risk'] / (POINT_VALUE[symbol] * PARAMS['size']), PARAMS['size'])
    return result

def entry_risk(panel):
    return {s: np.full(len(d), PARAMS['risk'] / PARAMS['size']) for s, d in panel.items()}

if __name__ == '__main__':
    sec = np.array([61200, 61260, 61320, 30540, 30600])
    out = _targets(sec, np.array([100., 101., 101., 101., 101.]),
        np.array([100., 100., 99., 101., 101.]), np.full(5, 100.),
        np.ones(5, dtype=np.int64), 61200, 30600, 2., 1)
    assert out.tolist() == [1, 1, 1, 1, 0]
