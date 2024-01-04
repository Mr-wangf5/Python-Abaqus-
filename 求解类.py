import numpy as np

"""用numpy的线性求解器"""
ff = fm.getForceVrctor()
KK = fm. getStructstifinessMatrix()

# 求解
delta = np.linalg.solve(KK, ff)



class LinerSolver:
    def __init__(self, A, b, eqs, max_iter):
        self.A =A
        self.b = b
        self.eqs = eqs
        self.max_iter = max_iter

    def CGsolver(self):
        iter = 0
        err = 8e9
        n = self.A.shape[0]

        x0 = np.zeros(n)
        r0 = self.b
        p0 = r0

        while (err > self.eqs and iter < self.max_iter):
            iter += 1

            inproduct_r0 = np.dot(r0, r0)
            tmp_row = np.dot(self.A, p0)
            I = np.dot(tmp_row, p0)
            alpha = inproduct_r0/1

            x1 = x0 + alpha * p0
            r1 = r0 - alpha * tmp_row

            err = np.linalg.norm(r1)

            inproduct_r1 = np.dot(r1, r1)
            beta = inproduct_r1/ inproduct_r0

            p1 = r1 + beta * p0

            x0 = x1
            r0 = r1
            p0 = p1

        print("迭代步数为：", iter)
        return  x1

"""自定义求解器"""
cls = LinerSolver(KK, 1e-4, 500)           # 创建一个求解器的实例cls
delta = cls.CGsolver()        # 调用共轭梯度法求解

