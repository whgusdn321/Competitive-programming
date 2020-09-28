tc = int(input())
for t in range(tc):
    p, f = map(int, input().split())
    sw_cnt, ax_cnt = map(int, input().split())
    s_weight, ax_weight = map(int, input().split())

    ans = 0
    k = min(sw_cnt+1, p//s_weight + 1)
    for my_sw_cnt in range(k):
        ans_ = 0
        sw_cnt_ = sw_cnt
        ax_cnt_ = ax_cnt

        # my_sw_cnt = min(sw_cnt_, my_sw_cnt)
        sw_cnt_ -= my_sw_cnt
        my_cap = p - my_sw_cnt*s_weight
        ans_ += my_sw_cnt

        my_ax_cnt = min(ax_cnt_, my_cap // ax_weight)
        ax_cnt_ -= my_ax_cnt
        my_cap = p - my_ax_cnt*ax_weight
        ans_ += my_ax_cnt

        if s_weight <= ax_weight:
            f_sw_cnt = min(sw_cnt_, f//s_weight)  # first take sword
            f_cap = f - f_sw_cnt*s_weight
            ans_ += f_sw_cnt

            f_ax_cnt = min(ax_cnt_, f_cap//ax_weight)
            ans_ += f_ax_cnt
        else:
            f_ax_cnt = min(ax_cnt_, f//ax_weight)
            f_cap = f - f_ax_cnt*ax_weight
            ans_ += f_ax_cnt

            f_sw_cnt = min(sw_cnt_, f_cap//s_weight)
            ans_ += f_sw_cnt
        ans = max(ans, ans_)
    print(ans)

