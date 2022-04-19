import pandas as pd
import numpy as np
import time
import os
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['font.sans-serif'] = ['consolas']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False


def main():
    # path1 = '站内数字化_850m_电容断线.xlsx'
    path1 = '仿真输出_20220419101058.xlsx'
    df_input = pd.read_excel(path1)

    # fig = plt.figure(figsize=(16, 9), dpi=100)
    # fig.subplots_adjust(hspace=0.4)
    # # fig.suptitle('test')

    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
    res_dir = '图表汇总\\站内数字化电容断线_%s' % timestamp

    if not os.path.exists(res_dir):
        os.makedirs(res_dir)

    for length in range(400, 851, 50):
        df = df_input.loc[df_input["主串区段长度(m)"] == length].copy()

        c_num_list = list(set(df['主串电容数(含TB)'].values))
        c_num_list.sort()

        print(c_num_list)

        for c_num in c_num_list:

            for pop_num in [1, 2]:
                fig = plt.figure(figsize=(16, 9), dpi=100)
                fig.subplots_adjust(hspace=0.4)

                condition = '断%s个电容' % pop_num
                fig_tittle = '邻线干扰电流_站内数字化_%sm_%s个电容_%s' % (length, c_num, condition)
                fig.suptitle(fig_tittle)

                print(c_num, pop_num)

                for index, freq in enumerate([1700, 2000, 2300, 2600]):
                    ax = fig.add_subplot(2, 2, index+1)
                    generate_plot(df, c_num, freq, pop_num, ax)

                filename1 = '%s\\%s_%s.png' % (res_dir, fig_tittle, timestamp)
                fig.savefig(filename1)
            # plt.show()


def generate_plot(df_input, c_num, freq, pop_num, ax):

    df = df_input.loc[
        (df_input["主串电容数(含TB)"] == c_num) & (df_input["主串频率(Hz)"] == freq),
        ['被串拆卸情况', '被串最大干扰电流(A)', '被串最大干扰位置(m)']
    ].copy()
    df.index = df['被串拆卸情况'].map(format_c_pop)

    normal = df.loc['正常', '被串最大干扰电流(A)']
    # print(normal)

    if pop_num == 1:
        res = df.loc[df['被串拆卸情况'].map(lambda x: len(eval(x)) == 1), '被串最大干扰电流(A)']
    elif pop_num == 2:
        res = df.loc[df['被串拆卸情况'].map(lambda x: len(eval(x)) == 2), '被串最大干扰电流(A)']

    # print(res)

    condition = '断%s个电容' % pop_num

    x_label = res.index

    length = res.size

    tmp = {
        1700: 263,
        2000: 234,
        2300: 217,
        2600: 200,
    }

    threshold = tmp[freq]

    xx = np.arange(length)
    yy = res.values
    yy2 = np.ones(length) * threshold / 1000
    yy3 = np.ones(length) * normal
    yy4 = np.ones(length) * threshold / 1000 * 0.75

    title = '被串钢轨电流-%sHz-%s' % (freq, condition)

    ax.set_title(title)
    ax.set_xlabel('断开电容')
    ax.set_ylabel('邻线干扰钢轨电流(A)')

    ax.yaxis.grid(True, which='major')
    ax.set_ylim([0, 0.3])

    txt = '最大干扰电流%.2fmA，门限值%sfmA' % (np.max(yy) * 1000, threshold)
    ax.text(0.05, 0.95, txt, fontsize=10, color='blue', va='top', ha='left', transform=ax.transAxes)

    ax.plot(xx, yy2, linestyle='--', alpha=0.8, color='orange', label='门限值')
    ax.plot(xx, yy4, linestyle='--', alpha=0.8, color='r', label='门限值75%')
    ax.plot(xx, yy3, linestyle='--', alpha=0.8, color='g', label='正常情况')
    ax.plot(xx, yy, linestyle='-', alpha=0.8, color='blue', label=condition)

    ax.set_xticks(xx)
    ax.set_xticklabels(x_label)

    ax.legend()
    for label in ax.xaxis.get_ticklabels():
        if pop_num > 1:
            label.set_rotation(90)

        label.set_color('blue')
        # label.set_font(8)


def format_c_pop(str_c_pop):
    tmp = eval(str_c_pop)
    if len(tmp) == 0:
        ret = '正常'
    elif len(tmp) == 1:
        ret = 'C%s' % tmp[0]
    else:
        ret = 'C%s C%s' % tmp

    return ret


if __name__ == '__main__':
    main()