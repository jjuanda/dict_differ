



class DictDiffer(object):
    """docstring for DictDiffer"""
    def __init__(self, dbase, dnew):
        super(DictDiffer, self).__init__()
        self.dbase = dbase
        self.dnew  = dnew
        self.ccmp = None
    
    def compare(self, ign_keys=[]):
        kbase = set(self.dbase.keys()) - set(ign_keys)
        knew  = set(self.dnew.keys()) - set(ign_keys)

        common_keys  = kbase.intersection(knew)
        new_keys     = knew - kbase
        removed_keys = kbase - knew

        diff_values  = dict([(k, [self.dbase[k], self.dnew[k]]) for k in common_keys
            if self.diff_vals(self.dbase[k], self.dnew[k])])

        equal_values = dict([(k, self.dbase[k]) for k in common_keys if k not in diff_values])

        self.ccmp = {
            'new'     : dict([(k, self.dnew[k]) for k in new_keys]),
            'removed' : dict([(k, self.dbase[k]) for k in removed_keys]),
            'equal'   : equal_values,
            'diff'    : diff_values,
        }

        return self.ccmp

    def equal(self):
        c = self.ccmp
        if c is None:
            c = self.compare()
        return (len(c['new']) == 0) and (len(c['removed']) == 0) and (len(c['diff']) == 0)

    def diff_vals(self, vbase, vnew):
        if type(vbase) != type(vnew):
            return True
        elif type(vbase) is dict:
            return not (DictDiffer(vbase, vnew).equal())
        else:
            return not (vbase == vnew)



if __name__ == '__main__':
    from bson.objectid import ObjectId
    import datetime
    from pprint import pprint

    qq = [{'oldid': ObjectId('54b4d42655067b0b926a5c83'),
  'dt': datetime.datetime(2014, 5, 14, 0, 0),
  'nav': '27.71',
  'isin': 'NL0000289783',
  '_id': ObjectId('55eaddd455067ba9a2545b56'),
  'dt_created': datetime.datetime(2014, 5, 14, 17, 9, 56, 890000)},
 {'oldid': ObjectId('54b4d42655067b0b926a5c84'),
  'dt': datetime.datetime(2014, 5, 14, 0, 0),
  'nav': '27.71',
  'isin': 'NL0000289783',
  '_id': ObjectId('55eaddd455067ba9a2545b57'),
  'dt_created': datetime.datetime(2014, 5, 14, 17, 9, 56, 890000)}]

    dd=DictDiffer(qq[0], qq[1])
    pprint(dd.compare()) 