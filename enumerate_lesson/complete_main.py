def format_leaderboard(player_names):
    formatted = []
    for index, name in enumerate(player_names):
        formatted.append(f"{index + 1}. {name}")
    return formatted
