



class DictDiffer(object):
    """docstring for DictDiffer"""
    def __init__(self, dbase, dnew):
        super(DictDiffer, self).__init__()
        self.dbase = dbase
        self.dnew  = dnew
    
    def compare(self):
        kbase = set(self.dbase.keys())
        knew  = set(self.dnew.keys())

        common_keys  = kbase.intersection(knew)
        new_keys     = knew - kbase
        removed_keys = kbase - knew

        diff_values  = dict([(k, [self.dbase[k], self.dnew[k]]) for k in common_keys
            if self.diff_vals(self.dbase[k], self.dnew[k])])

        equal_values = dict([(k, self.dbase[k]) for k in common_keys if k not in diff_values])

        return {
            'new'     : dict([(k, self.dnew[k]) for k in new_keys]),
            'removed' : dict([(k, self.dbase[k]) for k in removed_keys]),
            'equal'   : equal_values,
            'diff'    : diff_values,
        }

    def equal(self):
        c = self.compare()
        return (len(c['new']) == 0) and (len(c['removed']) == 0) and (len(c['diff']))

    def diff_vals(self, vbase, vnew):
        if type(vbase) != vnew:
            return True

        if type(vbase) is dict:
            return not (DictDiffer(vbase, vnew).equal())
        else:
            return not (vbase == vnew)

