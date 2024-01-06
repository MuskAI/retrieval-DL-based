import numpy as np
from scipy import spatial


def distance(v1, v2, d_type='d1'):
    assert v1.shape == v2.shape, "shape of two vectors need to be same!"
    # print('Distance type method {}'.format(d_type))
    if d_type == 'd1':
        return np.sum(np.absolute(v1 - v2))
    elif d_type == 'd2':
        return np.sum((v1 - v2) ** 2)
    elif d_type == 'd2-norm':
        return 2 - 2 * np.dot(v1, v2)
    elif d_type == 'd3':
        # TODO 测试用 要删除
        return np.sum(v1 * v2)
        pass
    elif d_type == 'd4':
        pass
    elif d_type == 'd5':
        pass
    elif d_type == 'd6':
        pass
    elif d_type == 'd7':
        return 2 - 2 * np.dot(v1, v2)
    elif d_type == 'd8':
        return 2 - 2 * np.dot(v1, v2)
    elif d_type == 'cosine':
        return spatial.distance.cosine(v1, v2)
    elif d_type == 'square':
        return 1 - np.sum((v1 - v2) ** 2)


def infer(query, samples=None, db=None, sample_db_fn=None, depth=None, d_type='d1', topk=3, thr=0.4):
    ''' infer a query, return it's ap
      arguments
        query       : a dict with three keys, see the template
                      {
                        'img': <path_to_img>,
                        'cls': <img class>,
                        'hist' <img histogram>
                      }
        samples     : a list of {
                                  'img': <path_to_img>,
                                  'cls': <img class>,
                                  'hist' <img histogram>
                                }
        db          : an instance of class Database
        sample_db_fn: a function making samples, should be given if Database != None
        depth       : retrieved depth during inference, the default depth is equal to database size
        d_type      : distance type
    '''
    assert samples != None or (
            db != None and sample_db_fn != None), "need to give either samples or db plus sample_db_fn"
    if db:
        samples = sample_db_fn(db)

    q_img, q_cls, q_hist = query['img'], query['cls'], query['hist']
    results = []

    for idx, sample in enumerate(samples):
        s_img, s_cls, s_hist, s_md5 = sample['img'], sample['cls'], sample['hist'], sample['md5']
        # if 'test' in s_img:
        #   print(sample['img'])
        #   print(s_hist)
        if q_img == s_img:
            continue
        results.append({
            'dis': distance(q_hist, s_hist, d_type=d_type),
            'cls': s_cls,
            'md5': s_md5
        })
    results = sorted(results, key=lambda x: x['dis'])
    std_results = []
    top_cls = []
    for i in range(len(results)):
        if results[i]['cls'] not in top_cls:
            top_cls.append(results[i]['cls'])
            std_results.append({'cls': results[i]['cls'],
                                'dis': results[i]['dis']})
        if len(top_cls) >= topk:
            break

    if depth and depth <= len(results):
        results = results[:depth]


    # 根据客户要求标准化输出
    # for idx,item in enumerate(results):
    #     if item['dis'] > thr:
    #         pass
    #     else:
    #         std_results.append(item)

    return top_cls, results, std_results
