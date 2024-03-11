import math

class MortgageCalculator:
    def __init__(self, principal, annual_rate, term_years):
        self.principal = principal
        self.annual_rate = annual_rate
        self.term_years = term_years
        self.monthly_rate = self.annual_rate / 12
        self.total_payments = self.term_years * 12
        self.remaining_principal = principal

    def equal_installment_monthly_payment(self):
        payment = (self.principal * self.monthly_rate * (1 + self.monthly_rate) ** self.total_payments) / ((1 + self.monthly_rate) ** self.total_payments - 1)
        total_payment_amount = payment * self.total_payments

        annual_remaining_principals = []
        # 迭代计算每个月的还款额和剩余本金
        for n in range(1, self.total_payments + 1):
            # 计算第n个月的利息
            interest_paid = self.remaining_principal * self.monthly_rate
            # 计算第n个月偿还的本金
            principal_paid = payment - interest_paid
            # 更新剩余本金
            self.remaining_principal -= principal_paid
            # 记录剩余本金
            # 如果是最后一个月，剩余本金应为0
            if n == self.total_payments:
                self.remaining_principal = 0
            annual_remaining_principals.append(self.remaining_principal)

        return payment, total_payment_amount, annual_remaining_principals

    def equal_principal_monthly_payment(self):
        payments = [(self.principal / self.total_payments) + (self.principal * self.monthly_rate * (i + 1) / self.total_payments) for i in range(self.total_payments)]
        payments.reverse()
        return payments, sum(payments)

    def print_results(self):
        eqi_payment, eqi_total, remaining_principals = self.equal_installment_monthly_payment()
        eqp_payments, eqp_total = self.equal_principal_monthly_payment()
        print(f"等额本息：每月还款额 {eqi_payment:.2f}元, 总还款额 {eqi_total:.2f}元，每月剩余本金{remaining_principals}")
        print(f"等额本金：每月还款额列表 {eqp_payments}, 总还款额 {eqp_total:.2f}元")

def calculate_annual_rental_cost(initial_monthly_rent, annual_increase_rate, rental_years):
    # 将月租金转换为年租金
    initial_annual_rent = initial_monthly_rent * 12
    # 初始化变量
    annual_rental_cost = []
    current_annual_rent = initial_annual_rent

    # 计算每年的租金开销并添加到列表中
    for year in range(1, rental_years + 1):
        annual_rental_cost.append(current_annual_rent)  # 添加当前年的年租金
        # 更新下一年的年租金（考虑上涨）
        current_annual_rent *= (1 + annual_increase_rate)

    return annual_rental_cost

def calculate_annual_price(initial_price, annual_increase_rate, simu_years):
    # 初始化变量
    annual_prices = []
    current_price = initial_price

    # 计算每年的价格并添加到列表中
    for year in range(1, simu_years + 1):
        annual_prices.append(current_price)  # 添加当前年的价格
        # 更新下一年的价格（考虑上涨）
        current_price *= (1 + annual_increase_rate)

    return annual_prices

def print_ele_per_12(remaining):
    counter = 0
    for ele in remaining:
        print(f"    {ele:.2f}", end=' ')

        # 更新计数器
        counter += 1

        # 当计数器达到12时，输出换行符并重置计数器
        if counter % 12 == 0:
            print()
            counter = 0

    # 如果列表长度不是12的倍数，确保最后一组数据后也有换行
    if counter != 0:
        print()

if __name__ == '__main__':
    fortune = 500000
    house_price = 1000000
    annual_increase_rate_price = 0.04  # 价格年增长率
    deposit_rate = 0.035 # 存款年利率
    loan_principal = house_price - fortune  # 贷款本金（例如：1,000,000元）
    annual_rate = 0.04         # 年利率（例如：5%）
    term_years = 20            # 贷款期限（例如：30年）

    initial_monthly_rent = 1000  # 初始月租金（例如：1000元/月）
    annual_increase_rate = 0.05  # 年增长率（例如：3%）
    #rental_years = 20  # 租房年数（例如：5年）

    # 计算每年的租金开销列表
    annual_rental_cost_list = calculate_annual_rental_cost(initial_monthly_rent, annual_increase_rate, term_years)

    annual_price_list = calculate_annual_price(house_price, annual_increase_rate_price, term_years)

    calculator = MortgageCalculator(loan_principal, annual_rate, term_years)

    eqi_payment, eqi_total, remaining_principals = calculator.equal_installment_monthly_payment()

    print(f"等额本金，每月{eqi_payment:.2f}元，总计{eqi_total:.2f}元，剩余本金列表:")
    print_ele_per_12(remaining_principals)

    # 等额本息
    current_fortune = fortune
    for year, price in enumerate(annual_price_list, start=1):
        paid_loan_this_year = eqi_payment * 12
        cost = annual_rental_cost_list[year-1]
        current_fortune += current_fortune *deposit_rate
        current_fortune += paid_loan_this_year
        current_fortune -= cost
        paid_loan_total = paid_loan_this_year * year

        print(f"第 {year} 年的房价为：{price:.2f}元，累积已还贷款：{paid_loan_total:.2f}元，资产{price - paid_loan_total - remaining_principals[year*12 - 1]:.2f}元；年租金{cost:.2f}元（每月{cost/12:.2f}元）资产{current_fortune:.2f}元")


    # 等额本金
    eqp_payments, eqp_total = calculator.equal_principal_monthly_payment()
    print(f"等额本金：总还款额 {eqp_total:.2f}元，每月还款额列表:")
    print_ele_per_12(eqp_payments)

    current_fortune = fortune
    paid_loan_total = 0
    for year, price in enumerate(annual_price_list, start=1):
        paid_loan_this_year = sum(eqp_payments[(year-1)*12 : year*12])
        #print(f"当年还款{paid_loan_this_year:.2f}元")
        cost = annual_rental_cost_list[year-1]
        current_fortune += current_fortune *deposit_rate
        current_fortune += paid_loan_this_year
        current_fortune -= cost
        paid_loan_total += paid_loan_this_year
        remaining_principal = loan_principal * (1 - year / term_years)

        print(f"第 {year} 年的房价为：{price:.2f}元，累积已还贷款：{paid_loan_total:.2f}元，资产{price - paid_loan_total - remaining_principal:.2f}元；年租金{cost:.2f}元（每月{cost/12:.2f}元）资产{current_fortune:.2f}元")