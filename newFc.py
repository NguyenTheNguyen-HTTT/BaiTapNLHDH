def tinhfcfscho(sotientrinh, dstientrinh):
    """
    Tinh toan thoi gian cho va thoi gian cho trung binh
    cho thuat toan FCFS.
    """
    # Sap xep danh sach tien trinh dua tren thoi gian den
    dstientrinh.sort(key=lambda x: x[1])

    thientai = 0
    tongtcho = 0
    
    print("Tien trinh   T.gian den    T.gian thuc hien   T.gian cho")
    
    ketquacuoi = []

    for i in range(sotientrinh):
        idprocess = dstientrinh[i][0]
        tden = dstientrinh[i][1]
        tthuchien = dstientrinh[i][2]

        if tden > thientai:
            thientai = tden
        
        cho = thientai - tden
        
        thientai += tthuchien
        
        ketquacuoi.append([idprocess, tden, tthuchien, cho])
        tongtcho += cho
    
    for dong in ketquacuoi:
        print(f" {dong[0]:<11}{dong[1]:<13}{dong[2]:<19}{dong[3]}")

    print(f"\nThoi gian cho trung binh = {tongtcho / sotientrinh:.2f}")


if __name__ == "__main__":
    # ID cua cac tien trinh
    idtientrinh = [1, 2, 3, 4, 5]
    
    thoigianden = [0, 3, 8, 13, 17]
    thoigianthuchien = [11, 7, 19, 4, 9]

    soluongtientrinh = len(idtientrinh)
    
    danhsachtientrinh = []
    for i in range(soluongtientrinh):
        danhsachtientrinh.append([idtientrinh[i], thoigianden[i], thoigianthuchien[i]])

    tinhfcfscho(soluongtientrinh, danhsachtientrinh)