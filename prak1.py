percentage = float(input("Masukkan persentase nilai siswa: "))

if percentage >= 90:
    print("Exellenct permformance")
elif percentage >= 80:
    print("Very Good performance")
elif percentage >= 70:
    print("Good performance")
elif percentage >= 60:
    print("Average performance")
else:
    print("Needs Improvement")