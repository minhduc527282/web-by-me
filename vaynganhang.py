import pandas as pd

# Nhập thông tin từ người dùng
loan_amount = float(input("Nhập số tiền vay (VD: 1300000000): "))
loan_term_years = int(input("Nhập thời hạn vay (năm): "))
interest_rate_annual = float(input("Nhập lãi suất ưu đãi (%/năm): "))

# Chuyển đổi thông tin
loan_term_months = loan_term_years * 12
interest_rate_monthly = interest_rate_annual / 100 / 12
monthly_principal = loan_amount / loan_term_months

# Lập bảng trả nợ
schedule = []
remaining_balance = loan_amount

for month in range(1, loan_term_months + 1):
    monthly_interest = remaining_balance * interest_rate_monthly
    total_payment = monthly_principal + monthly_interest
    schedule.append({
        "Tháng": month,
        "Dư nợ đầu kỳ (VNĐ)": round(remaining_balance),
        "Tiền gốc (VNĐ)": round(monthly_principal),
        "Tiền lãi (VNĐ)": round(monthly_interest),
        "Tổng thanh toán (VNĐ)": round(total_payment),
    })
    remaining_balance -= monthly_principal

# Xuất Excel
df = pd.DataFrame(schedule)
file_name = f"Lich_tra_no_{loan_term_years}nam_{interest_rate_annual}phantram.xlsx"
df.to_excel(file_name, index=False)

print(f"✅ Đã tạo file: {file_name}")
