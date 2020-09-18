import numpy as np


def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    else:
        a = np.array(list)
        b = np.split(a, 3)

        # mean calculation
        m_a = np.mean(b, axis=0).tolist()
        m_b = np.mean(b, axis=1).tolist()
        m_c = np.mean(b)
        m_calc = [m_a, m_b, m_c]

        # variance calculation
        v_a = np.var(b, axis=0).tolist()
        v_b = np.var(b, axis=1).tolist()
        v_c = np.var(b)
        v_calc = [v_a, v_b, v_c]

        # standard deviation calculation
        st_a = np.std(b, axis=0).tolist()
        st_b = np.std(b, axis=1).tolist()
        st_c = np.std(b)
        st_calc = [st_a, st_b, st_c]

        # max calculation
        ma_a = np.amax(b, axis=0).tolist()
        ma_b = np.amax(b, axis=1).tolist()
        ma_c = np.amax(b)
        ma_calc = [ma_a, ma_b, ma_c]

        # min calculation
        mi_a = np.amin(b, axis=0).tolist()
        mi_b = np.amin(b, axis=1).tolist()
        mi_c = np.amin(b)
        mi_calc = [mi_a, mi_b, mi_c]

        # sum calculation
        s_a = np.sum(b, axis=0).tolist()
        s_b = np.sum(b, axis=1).tolist()
        s_c = np.sum(b)
        s_calc = [s_a, s_b, s_c]

        calculations = {"mean": m_calc, "variance": v_calc, "standard deviation": st_calc, "max": ma_calc, "min": mi_calc, "sum": s_calc}

        return calculations
