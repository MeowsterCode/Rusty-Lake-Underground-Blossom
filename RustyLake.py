def next_step(game_map, start_point, direction): #计算虫子按照瓜子儿指向方向移动后的位置
    start_point[0] += direction[0]
    start_point[1] += direction[1]
    if start_point[0] >= len(game_map) or start_point[0] < 0 or start_point[1] >= len(game_map[0]) or start_point[1] < 0:
        return "None" # 如果移动后坐标超过范围，虫子消失
    while game_map[start_point[0]][start_point[1]] == 0: #如果移动后位置没有小洞，则继续循着瓜子方向移动
        start_point[0] += direction[0]
        start_point[1] += direction[1]
        if start_point[0] >= len(game_map) or start_point[0] < 0 or start_point[1] >= len(game_map[0]) or start_point[1] < 0:
            return "None"
    return start_point


def permutation(directions): #递归函数，返回列表所有排列情况
    if len(directions) == 1:
        return [directions]
    else:
        orders = []
        for d, direction in enumerate(directions):
            results = permutation(directions[:d] + directions[d+1:]) #取出列表中的一个数，递归剩下的数的所有排列
            for result in results:
                orders.append([direction] + result)
        return orders


def play(game_map, start_point, end_point, directions):
    orders = permutation(directions)
    for order in orders: #遍历所有排列情况，直到找到符合要求的排列
        tmp_point = [i for i in start_point] #虫子所在位置
        for direction in order:
            tmp_point = next_step(game_map, tmp_point, direction) #依次计算安排列摆放瓜子儿后虫子的位置
            if tmp_point == "None": #如果虫子消失，说明这个排列不正确，继续验证下一个排列
                break
        if tmp_point == end_point: #验证虫子移动完毕后位置是否与目标终点相同，若是，返回该排列，反之继续验证下一个
            return order
    print("No solution") #如果所有排列都不符合，游戏无解
            
    
if __name__=="__main__": 
    game_map = [[1,0,0,1,1,1,1,1,1,1],\
            [0,1,1,1,1,1,1,1,1,1],\
            [0,0,1,1,0,1,1,1,0,1],\
            [0,1,1,0,1,1,1,1,0,1],\
            [1,1,1,0,0,0,0,0,1,1]] #有小洞的位置为1，没有小洞的位置为0
    start_point = [0,0] #起始点
    end_point = [0,9] #目标终点
    directions = [[1,0],[1,0],[0,1],[0,1],[-1,1],[1,1],[-1,0]] #瓜子儿方向，向下、向右为[+1,+1]
    print(play(game_map, start_point, end_point, directions))
