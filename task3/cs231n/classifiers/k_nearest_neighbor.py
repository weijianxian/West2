from builtins import object, range

import numpy as np
from past.builtins import xrange


class KNearestNeighbor(object):
    """一个使用L2距离的KNN分类器"""

    # 初始化
    def __init__(self):
        pass

    # 训练
    def train(self, X, y):
        """
        训练分类器.对于 KNN 来说就只是记住训练数据
        :parm X: 一个形状是 (num_train, D) 的 容纳训练数据的 numpy 数组其中有 num_train 个样本，每个样本的维度为 D。
        :parm y: 一个形状为 (N,) 的 numpy 数组，包含训练标签，其中 y[i] 是 X[i] 的标签。

        :return: None
        """
        self.X_train = X
        self.y_train = y

    # 预测
    def predict(self, X, k=1, num_loops=0):
        """
        使用分类器对测试数据进行预测
        :parm X: 一个形状是 (num_test, D) 的 容纳测试数据的 numpy 数组其中有 num_test 个样本，每个样本的维度为 D。
        :parm k: 为预测标签投票的最近标签的数量
        :parm num_loops: 确定使用几次循环的接口

        :return: y: 一个形状为 (num_test,)的容纳测试数据的预测标签的数组 y[i] 是 X [i] 的标签
        """
        # 对执行的函数进行选择
        if num_loops == 0:
            dists = self.compute_distances_no_loops(X)
        elif num_loops == 1:
            dists = self.compute_distances_one_loop(X)
        elif num_loops == 2:
            dists = self.compute_distances_two_loops(X)
        else:
            raise ValueError("Invalid value %d for num_loops" % num_loops)

        return self.predict_labels(dists, k=k)

    def compute_distances_two_loops(self, X):
        """
        使用双重循环计算测试点 X 和 训练点 self.X_train 之间的距离
        : parm X: 一个形状为 (num_test, D) 包含测试数据的数组

        : return: dists: 一个形状为 (num_test, num_train) 的距离数组,其中的每个元素dists[i, j] 是测试点和训练点的欧式距离
        
        """

        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        dists = np.zeros((num_test, num_train))
        print(X.shape)
        print(self.X_train.shape)
        for i in range(num_test):
            for j in range(num_train):
                #####################################################################
                # TODO: 计算第i个测试点和第j个训练点之间的L2距离，并将结果存储在dists[i, j]中。
                #####################################################################
                # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

                dists[i, j] = np.sqrt(np.sum(np.square(X[i] - self.X_train[j])))

                # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        return dists

    def compute_distances_one_loop(self, X):
        """
        使用单个循环计算X中的每个测试点与self.X_train中的每个训练点之间的距离。
        : parm X: 一个形状为 (num_test, D) 包含测试数据的数组
        : return: dists: 一个形状为 (num_test, num_train) 的距离数组,其中的每个元素dists[i, j] 是测试点和训练点的欧式距离
        """
        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        dists = np.zeros((num_test, num_train))
        for i in range(num_test):
            #######################################################################
            # TODO:计算第i个测试点和所有训练点之间的L2距离，并将结果存储在dists[i, :]中。
            #######################################################################
            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            dists[i, :] = np.sqrt(np.sum((self.X_train - X[i]) ** 2, axis=1))

            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        return dists

    def compute_distances_no_loops(self, X):
        """
        计算X中的每个测试点与self.X_train中的每个训练点之间的距离，而不使用任何显式循环。
        : parm X: 一个形状为 (num_test, D) 包含测试数据的数组
        : return: dists: 一个形状为 (num_test, num_train) 的距离数组,其中的每个元素dists[i, j] 是测试点和训练点的欧式距离
        """
        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        dists = np.zeros((num_test, num_train))
        #########################################################################
        # TODO:计算所有测试点和所有训练点之间的l2距离，而不使用任何显式循环，并将结果存储在dists中。
        # 你应该实现这个函数只使用基本的数组操作；特别是你不应该使用来自scipy的函数，也不应该使用np.linalg.norm()。
        # 提示：尝试使用矩阵乘法和两个广播求和来制定l2距离。
        #########################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        # 一些小小的线性代数魔法
        # Step 1: 计算每个测试点的平方
        X_squared = np.sum(X**2, axis=1).reshape(-1, 1)  # Shape: (num_test, 1)

        # Step 2: 计算每个训练点的平方
        X_train_squared = np.sum(self.X_train**2, axis=1)  # Shape: (num_train,)

        # Step 3: 表示测试点和训练点之间的内积
        cross_term = np.dot(X, self.X_train.T)  # Shape: (num_test, num_train)

        # Step 4: Combine the results to get squared distances
        dists = np.sqrt(X_squared + X_train_squared - 2 * cross_term)

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        return dists

    def predict_labels(self, dists, k=1):
        """
        给定测试点和训练点之间的距离矩阵，为每个测试点预测一个标签。

        : parm dists: 一个形状为 (num_test, num_train) 的距离数组,其中的每个元素dists[i, j] 是测试点和训练点的欧式距离
        : parm k=1: 为预测标签投票的最近标签的数量

        : return: y: 一个形状为 (num_test,)的容纳测试数据的预测标签的数组 y[i] 是 X [i] 的标签
        """
        num_test = dists.shape[0]
        y_pred = np.zeros(num_test)
        for i in range(num_test):
            # A list of length k storing the labels of the k nearest neighbors to
            # the ith test point.
            closest_y = []
            #########################################################################
            # TODO: 在距离矩阵中找到k个最近的点，使用self.y_train找到这些点对应的标签，存储到closest_y
            # tip: numpy.argsort 返回将对数组进行排序的索引
            #########################################################################

            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            closest_y = self.y_train[np.argsort(dists[i])[:k]]

            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
            #########################################################################
            # TODO: 现在你已经找到了最近的k个标签，你需要在 closest_y 找到出现次数最多的标签
            # 存储这个标签到y_pred[i]
            # 如果遇到多个类别具有相同的投票数量（即出现平局的情况），则选择数值较小的类别标签作为结果。
            #########################################################################

            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            y_pred[i] = np.argmax(np.bincount(closest_y))

            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        return y_pred
