def get_total_matches(matches):
    return len(matches)


def get_total_seasons(matches):
    return matches["season"].nunique()


def get_most_successful_team(matches):
    winners = matches["winner"].dropna()

    if winners.empty:
        return "N/A"

    return winners.value_counts().idxmax()


def get_top_player(matches):
    players = matches["player_of_match"].dropna()

    if players.empty:
        return "N/A"

    return players.value_counts().idxmax()