num_students = 4
num_exams = 5

def get_validated_score(exam_num):
    while True:
        try:
            score = float(input(f"  {exam_num}. Sınav notu: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Not 0 ile 100 arasında olmalıdır. Tekrar deneyin.")
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")

student_data = [] 

for i in range(num_students):
    student_name = input(f"{i+1}. Öğrencinin adını giriniz: ")
    print(f"{student_name} için {num_exams} sınav notunu giriniz:")
    student_scores = [get_validated_score(j + 1) for j in range(num_exams)]
    student_data.append({'name': student_name, 'scores': student_scores})


student_averages = [sum(s['scores']) / len(s['scores']) for s in student_data if s['scores']]


if student_averages:
    overall_average = sum(student_averages) / len(student_averages)
    print(f"\nGenel Sınav Ortalaması (Öğrenci Ortalamalarının Ortalaması): {overall_average:.2f}")
else:
    overall_average = 0
    print("Hiçbir not girilmedi, genel ortalama 0 olarak ayarlandı.")

print("\nÖğrenci Başarı Durumları:")
for student in student_data:
    student_name = student['name']
    student_scores = student['scores']

    if student_scores:
        student_average = sum(student_scores) / len(student_scores)
        status = "BAŞARILI (Ortalamanın üzerinde veya eşit)" if student_average >= overall_average else "BAŞARISIZ (Ortalamanın altında)"
        print(f"{student_name} Ortalaması: {student_average:.2f}\n{student_name}: {status}")
    else:
        print(f"{student_name} için not girilmedi, ortalama hesaplanamadı.")
