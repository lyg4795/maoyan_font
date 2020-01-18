import numpy as  np
def covv(font,font3):
    # 分别计算两个字体文件x轴和y轴的协方差，协方差越大，则两个字体x或者y的变化趋势越接近，越可能是同一个数字
    num_dict_new={}
    num_dict = {'uniE26D':7, 'uniF651':2, 'uniE759':9, 'uniE798':0, 'uniE2E8':6, 'uniF117':1, 'uniE63A':8, 'uniEBF4':4, 'uniF689':3, 'uniF4E1':5}
    # 获取字体的编码列表
    font_list = font.getGlyphOrder()[2:]
    font_list3 = font3.getGlyphOrder()[2:]
    for i in font_list:
        max_len=0
        real_code=''
        # 获取该编码下的坐标
        fo = font['glyf'][i]
        # 将坐标转化为矩阵
        nparray=np.array(fo.coordinates)
        nplen = nparray.shape[0]
        for j in font_list3:
            fo3=font3['glyf'][j]
            nparray3 = np.array(fo3.coordinates)
            nplen3=nparray3.shape[0]
            # 如果两个编码下的组成数字的点的数量大于5，则视为不同数字
            if abs(nplen3-nplen)>5:
                continue
            need_len=min(nplen,nplen3)
            # 分别计算x,y 的协方差
            corr1=np.cov(nparray[:need_len,0],nparray3[:need_len,0])[0,1]
            corr2 = np.cov(nparray[:need_len, 1], nparray3[:need_len, 1])[0, 1]
            if corr2<0 or corr1<0:
                continue
            #     取协方差最大的
            if max_len<corr2+corr1:
                max_len = corr2 + corr1
                real_code=j
            # var_font.append({j:[corr1,corr2]})
        num_dict_new[real_code]=num_dict[i]
    return num_dict_new
        # print(i,var_font)