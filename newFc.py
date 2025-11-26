import sys
# add optional matplotlib import
try:
    import matplotlib.pyplot as plt
except Exception:
    plt = None

def tinhfcfscho(sotientrinh, dstientrinh):
    

    dstientrinh.sort(key=lambda x: x[1])

    thientai = 0
    tongtcho = 0
    
    print("Tien trinh   T.gian den    T.gian thuc hien   T.gian cho")
    
    ketquacuoi = []

    for i in range(sotientrinh):
        idprocess = dstientrinh[i][0]
        tden = dstientrinh[i][1]
        tthuchien = dstientrinh[i][2]

        # ensure current time moves to arrival if idle
        if tden > thientai:
            thientai = tden

        # start time is current time before executing
        start = thientai
        cho = start - tden

        # finish time
        finish = start + tthuchien

        # advance current time
        thientai = finish

        ketquacuoi.append([idprocess, tden, tthuchien, cho, start, finish])
        tongtcho += cho
    
    for dong in ketquacuoi:
        # print id, arrival, duration, waiting
        print(f" {dong[0]:<11}{dong[1]:<13}{dong[2]:<19}{dong[3]}")

    print(f"\nThoi gian cho trung binh = {tongtcho / sotientrinh:.2f}")

    # draw gantt chart if matplotlib is available
    if plt is None:
        print("\nChua cai dat matplotlib. De ve bieu do Gantt, chay: pip install matplotlib")
        return

    # prepare data for Gantt
    ids = [f"P{row[0]}" for row in ketquacuoi]
    starts = [row[4] for row in ketquacuoi]
    durations = [row[5] - row[4] for row in ketquacuoi]
    y_pos = range(len(ketquacuoi))

    fig, ax = plt.subplots(figsize=(8, 1 + len(ketquacuoi)*0.5))
    ax.barh(y_pos, durations, left=starts, height=0.4, align='center', color='skyblue', edgecolor='k')

    # annotate process id inside bars and time ticks
    for i, (s, d, pid) in enumerate(zip(starts, durations, ids)):
        ax.text(s + d/2, i, pid, va='center', ha='center', color='black', fontsize=9, fontweight='bold')

    # x ticks: show integer times spanning min start to max finish
    min_t = min(starts)
    max_t = max([row[5] for row in ketquacuoi])
    ax.set_xticks(range(min_t, max_t + 1))
    ax.set_yticks(y_pos)
    ax.set_yticklabels(ids)
    ax.set_xlabel("Thoi gian")
    ax.set_title("Gantt chart (FCFS)")

    plt.tight_layout()
    plt.savefig("gantt.png")
    print("\nGantt chart luu tai: gantt.png")
    plt.show()


if __name__ == "__main__":
    # ID cua cac tien trinh
    idtientrinh = [1, 2, 3, 4,5]
    
    thoigianden = [0, 1, 2, 3,4]
    thoigianthuchien = [10, 1, 2, 1, 5]

    soluongtientrinh = len(idtientrinh)
    
    danhsachtientrinh = []
    for i in range(soluongtientrinh):
        danhsachtientrinh.append([idtientrinh[i], thoigianden[i], thoigianthuchien[i]])

    tinhfcfscho(soluongtientrinh, danhsachtientrinh)