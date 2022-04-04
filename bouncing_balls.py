"""
Description:
A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.

He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

Three conditions must be met for a valid experiment:
1. Float parameter "h" in meters must be greater than 0
2. Float parameter "bounce" must be greater than 0 and less than 1
3. Float parameter "window" must be less than h.
If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

Note:
The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.
"""
from random import randint


def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce >= 1 or bounce <= 0 or window >= h:
        return -1
    cnt = 1
    for i in range(int(h // bounce)):
        h *= bounce
        if h > window:
            cnt += 2
    return cnt


def fixed_tests():
    def testing(h, bounce, window, exp):
        print("Testing: ", h, bounce, window)
        actual = bouncing_ball(h, bounce, window)
        # print("ACTUAL ", actual)
        # print("EXPECT ", exp)
        assert actual == exp, 'Wrong answer'

    def tests():
        testing(2, 0.5, 1, 1)
        testing(3, 0.66, 1.5, 3)
        testing(30, 0.66, 1.5, 15)
        testing(30, 0.75, 1.5, 21)
        testing(30, 0.4, 10, 3)
        testing(40, 0.4, 10, 3)
        testing(10, 0.6, 10, -1)
        testing(40, 1, 10, -1)
        testing(-5, 0.66, 1.5, -1)
        testing(5, -1, 1.5, -1)
        testing(4, 0.25, 1, 1)

    def bouncing_ball_tests(h, bounce, window):
        if (h <= 0) or (window >= h) or (bounce <= 0) or (bounce >= 1):
            return -1
        seen = -1
        while h > window:
            seen += 2
            h = h * bounce
        return seen

    def randomtests():
        someheights = [12, 10.5, 144, 233, 15.25, 61, 98, 15.9, 25.8, 41.8, 67,
                       109, 17, 28, 46, 7.5, 12.20, 19, 3, 5,
                       83, 13, 21, 35.5, 57, 92, 14,
                       24, 39, 6.5]
        somebounces = [0.6, 0.6, 0.6, 0.6, 0.6, 1.1, 9, 1, 0.6, 0.6, 0.6,
                       0.75, 0.75, 0.75, 0.75, 0.75, 12.20, 0.75, 0.75,
                       0.83, 0.13, 0.21, 0.35, 0.57, 0.9, 0.14,
                       0.24, 0.39, 0.65, 0.65]
        somewin = [1.5, 1.5, 1.44, 2.33, 1, 6.1, 9.8, 1.9, 2.8, 4.8, 3,
                   1.09, 1.7, 2.8, 46, 7.5, 12.20, 1.9, 3, 5,
                   0.83, 1.3, 2.1, 3.5, 0.57, 0.92, 1.4,
                   2.4, 3.9, 6.5]
        for x in range(0, 50):
            rn = randint(0, 29)
            f1 = someheights[rn]
            f2 = somebounces[rn]
            f3 = somewin[rn]
            sol = bouncing_ball_tests(f1, f2, f3)
            testing(f1, f2, f3, sol)

    tests()
    randomtests()
    passed = 'All tests passed :)'
    print('-' * len(passed))
    print(passed)
    print('-' * len(passed))


if __name__ == '__main__':
    fixed_tests()
