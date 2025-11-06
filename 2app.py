
# دریافت اطلاعات کاربر از ورودی (در اجرا واقعی از input استفاده کنید)
first_name = input("نام را وارد کنید: ")
last_name  = input("نام خانوادگی را وارد کنید: ")
age_input  = input("سن را وارد کنید: ")
major_input = input("رشته تحصیلی را وارد کنید: ")
gpa_input  = input("معدل را وارد کنید: ")

# تبدیل سن به عدد صحیح با استفاده از int()
age = int(age_input)  # تبدیل رشته سن به عدد صحیح

# تبدیل معدل به عدد ممیز شناور با استفاده از float()
gpa = float(gpa_input)  # تبدیل رشته معدل به float

# محاسبه تعداد ماه‌های عمر و ذخیره در متغیر age_month
age_month = age * 12  # هر سال ۱۲ ماه دارد، پس ضرب در ۱۲ می‌کنیم

# تغییر فرمت نام‌ها و رشته
first_name_fixed = first_name.upper()     # نام را به حروف بزرگ تبدیل می‌کنیم
last_name_fixed  = last_name.title()      # نام خانوادگی را به حالت استاندارد (هر کلمه با حرف بزرگ) تبدیل می‌کنیم
major_fixed      = major_input.strip()    # رشته تحصیلی را با strip() تمیز می‌کنیم تا فاصله‌های اضافی حذف شوند

# ساخت رشته متناظر با نام کامل
full_name = f"{first_name_fixed} {last_name_fixed}"  # ترکیب نام و نام خانوادگی

# چاپ اطلاعات با استفاده از f-string به صورت کارت شناسایی منظم
print("+" + "-"*38 + "+")
print("|{:^38}|".format("کارت شناسایی دانشجو"))  # عنوان کارت وسط‌چین
print("+" + "-"*38 + "+")
print("| {:<15}: {:>17} |".format("نام و نام خانوادگی", full_name))
print("| {:<15}: {:>17} |".format("سن (سال)", age))
print("| {:<15}: {:>17} |".format("سن (ماه)", age_month))
print("| {:<15}: {:>17} |".format("رشته تحصیلی", major_fixed))
print("| {:<15}: {:>17.2f} |".format("معدل", gpa))
print("+" + "-"*38 + "+")

# چاپ همان اطلاعات با روش concatenation (ترکیب رشته‌ای)
# دقت: برای الحاق رشته و عدد باید اعداد را به str تبدیل کنیم
concat_line = "نام و نام خانوادگی: " + full_name + " | " + "سن (سال): " + str(age) + " | " + \
              "سن (ماه): " + str(age_month) + " | " + "رشته: " + major_fixed + " | " + "معدل: " + str(gpa)
print("\n--- با استفاده از concatenation ---")
print(concat_line)
