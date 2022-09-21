print('Nhập K nếu bạn muốn ra kéo')
print('Nhập B nếu bạn muốn ra búa')
print('Nhập A nếu bạn muốn ra bao')

nguoi_choi = "A"
while nguoi_choi !="O":
    import random
    may=random.randint(1,3)

    ### 1 sẽ là kéo, 2 là búa, 3 là bao
    print("--------------")

    nguoi_choi=input("Bạn muốn ra gì?") # nên dùng uppercase và lowercase
    if nguoi_choi=="K" or nguoi_choi=="k":
        if may==1:
            print("Máy ra kéo")
            print("Hòa")
        if may==2:
            print("Máy ra búa")
            print("Máy thắng")
        if may==3:
            print("Máy ra bao")
            print("Người chơi thắng")
    if nguoi_choi=="B" or nguoi_choi=="b":
        if may==1:
            print("Máy ra kéo")
            print("Bạn thắng")
        if may==2:
            print("Máy ra búa")
            print("Hòa")
        if may==3:
            print("Máy ra bao")
            print("Bạn thua")
    if nguoi_choi=="A" or nguoi_choi=="a":
        if may==1:
            print("Máy ra kéo")
            print("Máy thắng")
        if may==2:
            print("Máy ra búa")
            print("Bạn thắng")
        if may==3:
            print("Máy ra bao")
            print("Hòa")