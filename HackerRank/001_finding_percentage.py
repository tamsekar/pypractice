if __name__ == '__main__':
    n = int(input())  # number of students records.
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    query_scores = student_marks[query_name]
    total = query_scores[0] + query_scores[1] + query_scores[2]
    average = total / len(query_scores)
    print("{:.2f}".format(average))
    
