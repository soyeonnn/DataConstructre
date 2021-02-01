from collections import deque


def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""

    print(f"테스트하는 문자열: {string}")
    stack = deque()  # 사용할 스택 정의

    for i in range(len(string)):
        # 열리는 괄호면 스택에 넣어준다.
        if string[i] == '(':
            stack.append((i, True))

        # 닫는 괄호일 경우, 경우를 또 나누어준다.
        elif string[i] == ')':
            # 스택이 비어있지 않은 경우
            if stack:
                # 열리는 괄호가 들어있으면 지워준다.
                if stack[-1][1] is True:
                    stack.pop()
                # 닫히는 괄호가 들어있으면 잘못 된 경우이기 때문에 스택에 넣어준다.
                elif stack[-1][1] is False:
                    stack.append((i, False))
            # 스택이 비어있는 경우, 닫는 괄호가 들어오면 잘못 된 경우이기 때문에 그냥 스택에 넣어준다.
            else:
                stack.append((i, False))

    # 잘못된 괄호 출력
    for i in range(len(stack)):
        if stack[i][1] is True:
            print("문자열 {} 번째 위치에 있는 괄호가 닫히지 않았습니다".format(stack[i][0]))
        elif stack[i][1] is False:
            print("문자열 {} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다".format(stack[i][0]))


case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)