def sec_to_hours(seconds):
    h = seconds//3600
    m = (seconds % 3600)//60
    s = (seconds % 3600) % 60
    result = ["{} giờ {} phút {} giây".format(h, m, s)]
    return result

def main():
    value = input("Nhập số giây sec (int) :\n")
    print(sec_to_hours(int(value)))


if __name__ == '__main__':
    main()