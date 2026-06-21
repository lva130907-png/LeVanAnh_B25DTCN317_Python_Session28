from tabulate import tabulate

class Order:
    def __init__(self, order_id, customer_name, product_name, cost_price, selling_price, quantity, discount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.quantity = quantity
        self.discount = discount

        self.revenue = 0
        self.profit = 0
        self.profit_type = ""

        self.calculate_revenue()
        self.calculate_profit()
        self.classify_profit()
    
    def calculate_revenue(self):
        revenue = self.selling_price * self.quantity - self.discount

        self.revenue = revenue

    def calculate_profit(self):
        profit = (self.selling_price - self.cost_price) * self.quantity - self.discount

        self.profit = profit

    def classify_profit(self):
        if self.profit < 5000000:
            self.profit_type = 'Kém'

        elif self.profit < 20000000:
            self.profit_type = 'Trung bình'

        elif self.profit < 50000000:
            self.profit_type = 'Tốt'

        else:
            self.profit_type = 'Xuất sắc'

class OrderManager:
    def __init__(self):
        self.orders = []

    def find_id_by_list(self, id):
        for order in self.orders:
            if order.order_id == id:
                return order
        return None
    
    def show_table(self, order_list):
        data = []

        for order in order_list:
            data.append([
                order.order_id,
                order.customer_name,
                order.product_name,
                f"{order.cost_price:,.0f}",
                f"{order.selling_price:,.0f}",
                order.quantity,
                f"{order.discount:,.0f}",
                f"{order.revenue:,.0f}",
                f"{order.profit:,.0f}",
                order.profit_type
            ])
        
        headers = [ 
            "Mã đơn", "Khách hàng", "Sản phẩm",
            "Giá vốn", "Giá bán", "SL", "Giảm giá",
            "Doanh thu", "Lợi nhuận", "Xếp loại"        
        ]

        print(tabulate(data, headers=headers, tablefmt="grid"))

    def add_order(self):
        while True:
            new_id = input("Nhập mã đơn mới: ").strip().upper()

            if not new_id:
                print("Mã sản phẩm không để trống!")
                continue

            if self.find_id_by_list(new_id):
                print("Mã sản phẩm đã tồn tại!")
                continue

            break

        while True:
            new_name = input("Nhập tên khách hàng: ").strip().title()

            if not new_name:
                print("Tên khách hàng không để trống!")
                continue

            break

        while True:
            new_product = input("Nhập tên sản phẩm ").strip()

            if not new_product:
                print("Tên sản phẩm không để trống!")
                continue

            break

        new_cost = float_input("Nhập giá vốn: ")

        new_sell = float_input("Nhập giá bán: ", min_value = new_cost)

        new_quantity = int_input("Nhập số lượng: ")

        new_discount = float_input("Nhập giảm giá: ")

        new_order = Order(new_id, new_name, new_product, new_cost, new_sell, new_quantity, new_discount)

        self.orders.append(new_order)

        print("Thêm đơn hàng thành công!")

    def show_all(self):
        if not self.orders:
            print("Danh sách đơn hàng đang rỗng!")
            return
        
        self.show_table(self.orders)

    def update_order(self):
        update_id = input("Nhập id bạn muốn cập nhật: ").strip().upper()

        update_ord = self.find_id_by_list(update_id)

        if not update_ord:
            print("Mã sản phẩm bạn nhập không tồn tại!")
            return
        
        update_ord.cost_price = float_input("Cập nhật giá vốn: ")

        update_ord.selling_price = float_input("Cập nhật giá bán: ")

        update_ord.quantity = float_input("Cập nhật số lượng: ")

        update_ord.discount = float_input("Cập nhật giảm giá: ")

        update_ord.calculate_revenue()
        update_ord.calculate_profit()
        update_ord.classify_profit()

        print("Cập nhật thành công!")

    def delete_order(self):
        remove_id = input("Nhập id bạn muốn xóa: ").strip().upper()

        remove_ord = self.find_id_by_list(remove_id)
        
        if not remove_ord:
            print("Không tìm thấy mã sản phẩm bạn muốn xóa!")
            return
        
        while True:
            confirm = input("Bạn có chắc muốn xóa? (Y?N): ").strip().lower()

            if confirm == 'y':
                self.orders.remove(remove_ord)
                print("Xóa thành công!")
                break
            
            elif confirm == 'n':
                print("Đã hủy thao tác xóa")
                break

            else:
                print("Lựa chọn không hợp lệ! hãy thử lại!")

    def search_order(self):
        print()
        while True:
            print()
            print("1. Tìm kiếm theo tên khách hàng ")
            print("2. Tìm kiếm theo tên sản phẩm ")
            print("3. Thoát")
            print()

            child_choice_one = input("Nhập lựa chọn của bạn: ").strip()

            if child_choice_one == "1":
                search_name_cus = input("Nhập tên khách hàng bạn muốn tìm kiếm: ").strip().lower()

                result = []

                for order in self.orders:
                    if search_name_cus in order.customer_name.lower():
                        result.append(order)

                if not result:
                    print(f"Không tìm thấy {search_name_cus}")
                    continue

                else:
                    self.show_table(result)

            elif child_choice_one == '2':
                search_name_product = input("Nhập tên sản phẩm bạn muốn tìm kiếm: ").strip().lower()

                result = []

                for order in self.orders:
                    if search_name_product in order.product_name.lower():
                        result.append(order)

                if not result:
                    print(f"Không tìm thấy {search_name_product}")
                    continue

                else:
                    self.show_table(result)

            elif child_choice_one == "3":
                print("Thoát chương trình tìm kiếm!")
                break

            else:
                print("Lựa chọn không hợp lệ!Hãy thử lại")

    def sort_order(self):
        while True:
            child_sort_menu()

            child_choice_two = input("Nhập lựa chọn của bạn: ").strip()

            if child_choice_two == "1":
                sorted_order = sorted(self.orders, key=lambda x: x.revenue)

                self.show_table(sorted_order)

            elif child_choice_two == "2":
                sorted_order = sorted(self.orders, key=lambda x: x.revenue, reverse=True)

                self.show_table(sorted_order)

            elif child_choice_two == "3":
                sorted_order = sorted(self.orders, key=lambda x: x.profit)

                self.show_table(sorted_order)

            elif child_choice_two == "4":
                sorted_order = sorted(self.orders, key=lambda x: x.profit, reverse=True)

                self.show_table(sorted_order)

            elif child_choice_two == '5':
                print("Thoát chương trình sắp xếp")
                break

            else:
                print("Lựa chọn không hợp lệ")

    def statistics(self):
        total_revenue = sum(order.revenue for order in self.orders)
        print("Tổng doanh thu là: ",total_revenue)

        print()

        total_profit = sum(order.profit for order in self.orders)
        print("Tổng lợi nhuận là: ",total_profit)

        print()

        max_revenue = max(order.revenue for order in self.orders)
        print("Đơn hàng có lợi nhuận cao nhất: ",max_revenue)

        print()

        min_revenue = min(order.revenue for order in self.orders)
        print("Đơn hàng có lợi nhuận thấp nhất: ",min_revenue)

        print()

        count_least = 0
        count_medium = 0
        count_good = 0
        count_excellent = 0

        for order in self.orders:
            if order.profit_type == "Kém":
                count_least += 1

            elif order.profit_type == "Trung bình":
                count_medium += 1

            elif order.profit_type == "Tốt":
                count_good += 1

            else:
                count_excellent += 1

        print("Số lượng đơn hàng theo từng mức: ")
        print("Kém: ", count_least)
        print("Trung bình: ", count_medium)
        print("Tốt: ",count_good)
        print("Xuất sắc: ",count_excellent)

def float_input(prompt, min_value = 0):
    while True:
        try:
            value = float(input(prompt))

            if value < min_value:
                print(f"Giá trị không được <= {min_value:,.0f}")
                continue

            return value
        
        except ValueError:
            print("Giá trị phải là số!")

def int_input(prompt, min_value = 1, max_value = 10000):
    while True:
        try:
            value = int(input(prompt))

            if value < min_value or value > max_value:
                print(f"Giá trị từ {min_value} đến {max_value}")
                continue

            return value
        
        except ValueError:
            print("Giá trị phải là số!")

def child_sort_menu():
    print(""" 
1. Theo doanh thu tăng dần
2. Theo doanh thu giảm dần
3. Theo lợi nhuận tăng dần
4. Theo lợi nhuận giảm dần
5. Thoát sắp xếp
 """)
    
def show_menu():
    print(""" 
================ MENU ================

1. Hiển thị danh sách đơn hàng
2. Thêm đơn hàng mới
3. Cập nhật đơn hàng
4. Xóa đơn hàng
5. Tìm kiếm đơn hàng
6. Sắp xếp đơn hàng
7. Thống kê lợi nhuận
0. Thoát

=====================================
 """)
    
def main():
    order = OrderManager()

    order.orders.extend([
        Order("OD001", "Nguyen Van An", "Laptop Dell", 12000000, 15000000, 2, 1000000),
        Order("OD002", "Tran Thi Mai", "Chuot Logitech", 200000, 350000, 20, 500000),
        Order("OD003", "Le Hoang Nam", "Ban phim co AKKO", 800000, 1200000, 10, 1000000),
        Order("OD004", "Pham Minh Duc", "Man hinh Samsung", 3500000, 4500000, 5, 0),
        Order("OD005", "Do Thi Huong", "Tai nghe Sony", 1800000, 2500000, 8, 500000),
    ])

    while True:
        show_menu()
        
        choice = input("Nhập lựa chọn của bạn: ").strip()
        print()

        if choice == "1":
            order.show_all()

        elif choice == "2":
            order.add_order()

        elif choice == "3":
            order.update_order()

        elif choice == "4":
            order.delete_order()

        elif choice == "5":
            order.search_order()
        
        elif choice == "6":
            order.sort_order()

        elif choice == "7":
            order.statistics()

        elif choice == "0":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý đơn hàng!")
            break
            
        else:
            print("Lựa chọn không hợp lệ! Hãy thử lại")

if __name__ == "__main__":
    main()
