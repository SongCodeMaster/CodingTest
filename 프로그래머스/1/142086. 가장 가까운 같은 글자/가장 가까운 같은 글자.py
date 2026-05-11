def solution(s):
    answer = []
    word_dict = {}
    for i, word in enumerate(s):
        if word in word_dict:
            answer.append(i - word_dict[word])
            word_dict[word] = i
        else:
            word_dict[word] = i
            answer.append(-1)
    return answer