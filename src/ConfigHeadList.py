#################################################################################

# 移频脉冲表头
def config_headlist_ypmc():
    head_list = [
        '序号', '备注',

        '主串区段长度(m)', '被串区段长度(m)',
        '钢轨电阻(Ω/km)', '钢轨电感(H/km)',

        '耦合系数',
        '主串频率(Hz)', '被串频率(Hz)',
        '主串道床电阻(Ω·km)', '被串道床电阻(Ω·km)',
        '主串电容数(含TB)', '被串电容数(含TB)',
        '主串电容值(μF)', '被串电容值(μF)',

        '主串分路电阻(Ω)', '被串分路电阻(Ω)',
        '分路间隔(m)',
        '主串电缆长度(km)', '被串电缆长度(km)',

        '主串扼流变压器变比', '被串扼流变压器变比',
        '主串电平级',

        '主串功出电压(V)', '主串轨入电压(V)',
        '被串最大干扰电流(A)', '被串最大干扰位置(m)',
    ]

    return head_list


#################################################################################

# 25Hz电码化表头
def config_headlist_25Hz_coding_():
    head_list = [
        '序号', '备注',

        '主串区段长度(m)', '被串区段长度(m)',

        '钢轨电阻(Ω/km)', '钢轨电感(H/km)',

        '耦合系数',
        '主串频率(Hz)', '被串频率(Hz)',
        '主串道床电阻(Ω·km)', '被串道床电阻(Ω·km)',
        '主串电容数(含TB)', '被串电容数(含TB)',
        '主串电容值(μF)', '被串电容值(μF)',
        '主串拆卸情况', '被串拆卸情况',

        '分路电阻(Ω)',
        '分路间隔(m)',
        '电缆长度(km)',

        '主串电平级',
        '发码继电器状态',

        '调整电阻(Ω)', '调整电感(H)', '调整电容(F)',
        '调整RLC模式',

        'NGL-C1(μF)',

        'WGL-C1(μF)',
        'WGL-C2(μF)',
        'WGL-L1-R(Ω)', 'WGL-L1-L(H)',
        'WGL-L2-R(Ω)', 'WGL-L2-L(mH)',

        'WGL-BPM变比',
        '扼流变压器变比',

        'BE-Rm(Ω)', 'BE-Lm(H)',

        '被串最大干扰电流(A)', '被串最大干扰位置(m)',
        '主串出口电流(A)', '主串入口电流(A)',
    ]

    return head_list


#################################################################################

# 绝缘破损防护表头
def config_headlist_2000A_TB():
    head_list = [
        '序号',
        '备注',

        '主串区段长度(m)', '被串区段长度(m)',

        '钢轨电阻(Ω/km)', '钢轨电感(H/km)',

        '耦合系数',
        '主串频率(Hz)', '被串频率(Hz)',
        '主串道床电阻(Ω·km)', '被串道床电阻(Ω·km)',
        '主串电容数(含TB)', '被串电容数(含TB)',
        '主串电容值(μF)', '被串电容值(μF)',
        '主串拆卸情况', '被串拆卸情况',

        'TB模式',
        # "SVA'互感",

        '分路电阻(Ω)',
        '分路间隔(m)',
        '电缆长度(km)',

        '主串电平级',
        '电源电压',

        # '是否全部更换TB',

        # '主串轨入电压(调整状态)',
        # '被串最大轨入电压(主备串同时分路状态)',

        '被串最大干扰电流(A)', '被串最大干扰位置(m)',
        # '主串出口电流(A)', '主串入口电流(A)',
    ]

    return head_list


#################################################################################

# 2000A一体化表头
def config_headlist_2000A_inte():
    head_list = [
        '序号', '备注',

        '主串区段长度(m)', '被串区段长度(m)',
        # '钢轨电阻(Ω/km)', '钢轨电感(H/km)',

        '主串钢轨电阻', '主串钢轨电感',
        '被串钢轨电阻', '被串钢轨电感',

        '耦合系数',
        '主串频率(Hz)', '被串频率(Hz)',
        '主串道床电阻(Ω·km)', '被串道床电阻(Ω·km)',
        '主串电容数(含TB)', '被串电容数(含TB)',
        '主串电容值(μF)', '被串电容值(μF)',

        '主串拆卸情况', '被串拆卸情况',

        '主串分路电阻(Ω)', '被串分路电阻(Ω)',
        '分路间隔(m)',
        '主串电缆长度(km)', '被串电缆长度(km)',

        # '主串扼流变压器变比', '被串扼流变压器变比',
        '主串电平级',

        '主串功出电压(V)', '主串轨入电压(V)',
        '被串最大干扰电流(A)', '被串最大干扰位置(m)',

        '主串TB1电流(A)', '主串TB2电流(A)',
        '被串TB1电流(A)', '被串TB2电流(A)',

        '主串扼流变压器变比', '主串扼流变压器变比'
    ]

    return head_list


#################################################################################

# 2000A一体化表头
def config_headlist_2000A_QJ():
    head_list = [
        '序号', '备注',

        '主串区段长度(m)', '被串区段长度(m)',
        # '钢轨电阻(Ω/km)', '钢轨电感(H/km)',

        '主串钢轨电阻', '主串钢轨电感',
        # '被串钢轨电阻', '被串钢轨电感',

        '耦合系数',
        '主串频率(Hz)', '被串频率(Hz)',
        '主串道床电阻(Ω·km)', '被串道床电阻(Ω·km)',
        # '主串电容数(含TB)', '被串电容数(含TB)',
        '主串电容值(μF)', '被串电容值(μF)',

        # '主串拆卸情况', '被串拆卸情况',
        '主串发送器位置', '被串发送器位置',

        '主串分路电阻(Ω)', '被串分路电阻(Ω)',
        '分路间隔(m)',
        '主串电缆长度(km)', '被串电缆长度(km)',

        # '主串扼流变压器变比', '被串扼流变压器变比',
        '主串电平级',

        # '主串功出电压(V)', '主串轨入电压(V)',
        '被串最大干扰电流(A)', '被串最大干扰位置(m)',

        # '主串TB1电流(A)', '主串TB2电流(A)',
        # '被串TB1电流(A)', '被串TB2电流(A)',

        # '主串扼流变压器变比', '主串扼流变压器变比'
    ]

    return head_list


#################################################################################

# 绝缘破损防护表头
def config_headlist_inhibitor_c():
    head_list = [
        '序号',
        '备注',

        '主串区段长度(m)', '被串区段长度(m)',

        '钢轨电阻(Ω/km)', '钢轨电感(H/km)',

        '耦合系数',
        '主串频率(Hz)', '被串频率(Hz)',
        '主串道床电阻(Ω·km)', '被串道床电阻(Ω·km)',
        '主串电容数(含TB)', '被串电容数(含TB)',
        '主串电容值(μF)', '被串电容值(μF)',

        # '主串抑制电容L1(μH)', '主串抑制电容C1(μF)', '主串抑制电容模式',
        # '被串抑制电容L2(μH)', '被串抑制电容C2(μF)', '被串抑制电容模式',

        '主串故障模式', '被串故障模式',
        '主串故障位置', '被串故障位置',
        'TB模式',

        '主串分路电阻(Ω)', '被串分路电阻(Ω)',
        '主串电缆长度(km)', '被串电缆长度(km)',

        '分路间隔(m)',

        '主串电平级',
        '电源电压',

        # '是否全部更换TB',

        # '主串轨入电压(调整状态)',
        # '被串最大轨入电压(主备串同时分路状态)',

        '被串最大干扰电流(A)', '被串最大干扰位置(m)',
        # '主串出口电流(A)', '主串入口电流(A)',
        '被串轨入电压(调整状态)', '被串最大轨入电压(主被串同时分路状态)',
    ]

    return head_list


#################################################################################

# 绝缘破损防护表头
def config_headlist_hanjialing():
    head_list = [
        '序号',
        '备注',
        '主串区段', '被串区段',
        '主串方向', '被串方向',
        '主串左端里程标', '被串左端里程标',

        '主串区段长度(m)', '被串区段长度(m)',

        '钢轨电阻(Ω/km)', '钢轨电感(H/km)',

        '线间距', '耦合系数',
        '主串频率(Hz)', '被串频率(Hz)',
        '主串道床电阻(Ω·km)', '被串道床电阻(Ω·km)',
        '主串电容数(含TB)', '被串电容数(含TB)',
        '主串电容值(μF)', '被串电容值(μF)',

        # '主串抑制电容L1(μH)', '主串抑制电容C1(μF)', '主串抑制电容模式',
        # '被串抑制电容L2(μH)', '被串抑制电容C2(μF)', '被串抑制电容模式',

        # '主串故障模式', '被串故障模式',
        # '主串故障位置', '被串故障位置',
        # 'TB模式',

        '主串分路电阻(Ω)', '被串分路电阻(Ω)',
        '主串电缆长度(km)', '被串电缆长度(km)',

        '分路间隔(m)',

        '主串电平级',
        '电源电压',

        # '是否全部更换TB',

        # '主串轨入电压(调整状态)',
        # '被串最大轨入电压(主备串同时分路状态)',

        '调整电阻(Ω)', '调整电感(H)', '调整电容(F)',
        '调整RLC模式',

        'NGL-C1(μF)',

        'WGL-C1(μF)',
        'WGL-C2(μF)',
        'WGL-L1-R(Ω)', 'WGL-L1-L(H)',
        'WGL-L2-R(Ω)', 'WGL-L2-L(mH)',

        'WGL-BPM变比',
        '扼流变压器变比',

        'BE-Rm(Ω)', 'BE-Lm(H)',

        '被串最大干扰电流(A)', '被串最大干扰位置(m)',
    ]

    return head_list


#################################################################################

# 绝缘破损防护表头
def config_headlist_20200730():
    head_list = [
        '序号',
        '备注',
        '主串区段', '被串区段',
        '主串方向', '被串方向',
        # '主串左端里程标', '被串左端里程标',

        '主串区段长度(m)', '被串区段长度(m)',

        '钢轨电阻(Ω/km)', '钢轨电感(H/km)',

        '线间距', '耦合系数',
        '主串频率(Hz)', '被串频率(Hz)',
        '主串道床电阻(Ω·km)', '被串道床电阻(Ω·km)',
        '主串电容数(含TB)', '被串电容数(含TB)',
        '主串电容值(μF)', '被串电容值(μF)',

        # '主串抑制电容L1(μH)', '主串抑制电容C1(μF)', '主串抑制电容模式',
        # '被串抑制电容L2(μH)', '被串抑制电容C2(μF)', '被串抑制电容模式',

        # '主串故障模式', '被串故障模式',
        # '主串故障位置', '被串故障位置',
        # 'TB模式',

        '主串分路电阻(Ω)', '被串分路电阻(Ω)',
        '主串电缆长度(km)', '被串电缆长度(km)',

        '分路间隔(m)',

        '主串电平级',
        '电源电压',

        # '是否全部更换TB',

        # '主串轨入电压(调整状态)',
        # '被串最大轨入电压(主备串同时分路状态)',

        # '调整电阻(Ω)', '调整电感(H)', '调整电容(F)',
        # '调整RLC模式',
        #
        # 'NGL-C1(μF)',
        #
        # 'WGL-C1(μF)',
        # 'WGL-C2(μF)',
        # 'WGL-L1-R(Ω)', 'WGL-L1-L(H)',
        # 'WGL-L2-R(Ω)', 'WGL-L2-L(mH)',
        #
        # 'WGL-BPM变比',
        # '扼流变压器变比',
        #
        # 'BE-Rm(Ω)', 'BE-Lm(H)',

        # '被串最大干扰电流(A)', '被串最大干扰位置(m)',
        '被串最大轨入电压(主调整被调整)',
    ]

    return head_list