class A:
    def __init__(self, a, b):
        self.a = a + 1  # A 类的 a 初始化时加 1
        self.b = b + 1  # A 类的 b 初始化时加 1

    def run(self):
        print("A's run:", self.a, self.b)

class B(A):
    def __init__(self, a, b):
        super().__init__(a, b)  # 调用 A 类的初始化方法
        # B 类继续修改 a 和 b 的值
        self._a = self.a + 1  # 存储 A 类的 a 基础上加 1
        self._b = self.b + 2  # 存储 A 类的 b 基础上加 2

    def run(self):
        # B 类的 run 方法使用修改后的 _a 和 _b
        print("B's run:", self._a, self._b)

    def call_a_run(self):
        # 显式调用 A 类的 run 方法，使用 A 类的 a 和 b
        super().run()  # 输出 A 类原始的 a 和 b

# 测试代码
q = B(10, 15)

# 调用 B 类的 run 方法
q.run()  # 输出: B's run: 12 18

# 调用 A 类的 run 方法
q.call_a_run()  # 输出: A's run: 11 16
