def solution(id_list, report, k):
    answer = []
    blockdic = {i:[] for i in id_list}
    answerdic = {i:0 for i in id_list}
    for i in range(len(report)):
        reporter,respondent = report[i].split(' ')
        if reporter not in blockdic[respondent]:
            blockdic[respondent].append(reporter)
    for b in blockdic:
        if len(blockdic[b]) >= k:
            for j in blockdic[b]:
                answerdic[j] += 1
    for k,v in answerdic.items():
        answer.append(v)
    return answer
solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)