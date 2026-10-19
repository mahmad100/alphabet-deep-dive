"""Input overrides for the scenario engine: returns a copy of a case with chosen inputs changed."""
import copy


def tweak_factory(BASE):
    def tweak(**k):
        c = copy.deepcopy(BASE)
        for key, v in k.items():
            if key == 'cents':
                c['cents'] = [None] + [v] * 4
            elif key == 'step':
                c['margin'] = [BASE['margin'][0] + v * i for i in range(5)]
            elif key == 'services':
                for r in (10, 11, 13):
                    c['growth'][r] = [x + v for x in c['growth'][r]]
            elif key == 'capex_shift':
                c['capex'] = [x + (v if i >= 1 else 0) for i, x in enumerate(c['capex'])]
            else:
                c[key] = v
        return c
    return tweak
