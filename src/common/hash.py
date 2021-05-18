import collections
if __name__ =='__main__':
    od = collections.OrderedDict()
    #增加
    od['c'] =0 
    od['j'] =2 
    od['f'] =1 
    print(od)
    #查询
    od.get('c')
    od['c']
    print('items',od.items())
    #删除
    od.pop('c')
    print(od)
    od.popitem(last=False)
    od['c'] =0 
    od['f'] =2 
    print(od)

    d = collections.defaultdict(int)
    d['1'] =1
    print(d['1'],d['2'],d.get('3',4))