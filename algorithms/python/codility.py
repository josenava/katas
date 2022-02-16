def solution(S, K):
    """I am assuming a valid input"""
    week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day_pos = week_days.index(S)

    pos = K % 7

    if day_pos + pos < len(week_days):
        return week_days[day_pos + pos]
    return week_days[day_pos + pos - len(week_days)]


if __name__ == "__main__":
    print(solution("Tue", 500))
