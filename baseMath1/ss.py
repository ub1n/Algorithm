def solution(program, flag_rules, commands):
    answer = []
    # rule 정보를 flag_name을 key,flag_argument_type을 값으로 하는 딕셔너리 생성
    rules_dic = {}
    for rule in flag_rules:
        # rule 정보를 띄어쓰기 기준으로 나누어서 배열에 넣음
        arr = rule.split()
        rules_dic[arr[0]] = arr[1]

    # command 정보를 띄어쓰기 기준으로 나누어서 배열에 순서대로 넣음
    commands_arr = []
    for command in commands:
        arr = command.split()
        commands_arr.append(arr)

    for command_arr in commands_arr:
        # 프로그램 이름이 다를경우엔 False를 추가한 후 넘긴다
        if command_arr[0] != program:
            answer.append(False)
            continue
        isTrue = True
        command_index = 1
        while command_index < len(command_arr):
            # 커맨드가 -일때 값을 판단
            if command_arr[command_index][0] == '-':
                # 해당 커맨드가 rule안에 있을 때 커맨드 판별
                if command_arr[command_index] in rules_dic:
                    rule = rules_dic[command_arr[command_index]]
                    command = ''
                    command_index += 1
                    if command_index < len(command_arr):
                        command = command_arr[command_index]
                        command_index += 1
                    # 커맨드가 -e 일때 판단
                    if rule == "NULL":
                        if command == '' or command[0] == '-':
                            continue
                        else:
                            isTrue = False
                            break
                    # 커맨드가 -s일때 판단
                    elif rule == "STRING":
                        if command.isalpha():
                            continue
                        else:
                            isTrue = False
                            break
                    # 커맨드가 -n일때 판단
                    elif rule == "NUMBER":
                        if command.isdecimal():
                            continue
                        else:
                            isTrue = False
                            break
                # 커맨드가 룰 안에 없으면 False
                else:
                    isTrue = False
                    break
            # 커맨드 없이 글자만 있을때 False
            else:
                if command_arr[command_index - 1][0] != '-':
                    isTrue = False
                    break
        answer.append(isTrue)

    return answer
