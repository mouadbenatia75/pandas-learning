import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing csv files of movies informaiton and thier rating information
movies = pd.read_csv("movies.csv")
rating = pd.read_csv("ratings.csv")
# Merging the movies dataframe and the rating dataframes
MoviesRating = pd.merge(movies , rating , on="movieId")
# Group by the movies Id for Aggregation 
GroupRating = MoviesRating.groupby("movieId")
# Replaces the timestamp with the date time 
MoviesRating["timestamp"] = pd.to_datetime(MoviesRating["timestamp"])
movies_stats =( 
    MoviesRating.groupby("title")
    .agg(mean_rating=("rating","mean") , total_votes = ("rating","count"))
    .reset_index()
)
popularMovies = movies_stats[movies_stats["total_votes"] >= 50]

top_rating_movies = popularMovies.sort_values(by = "mean_rating", ascending=False).head(20)

# print(movies)
# print(movies_stats)
# print(popularMovies)
# Aggregation select the mean , max and  min rating for each movie
# print(GroupRating["rating"].mean().to_string())
# print(GroupRating["rating"].max())
# print(GroupRating["rating"].min())


plt.figure(figsize=(11, 7))

bars = plt.barh(
    top_rating_movies["title"],
    top_rating_movies["mean_rating"],
    color = "#4C72B0",
    edgecolor="#2C3E50",
    alpha=0.85,
)

plt.xlabel("Mean Rating (Out of 5.0)", fontsize=11, fontweight="bold")
plt.ylabel("Movie Title", fontsize=11, fontweight="bold")
plt.title(
    "Top 20 Highest-Rated Movies on MovieLens (Min. 50 Votes)",
    fontsize=13,
    fontweight="bold",
    pad=15,
)

plt.xlim(0, 5.2)

plt.gca().invert_yaxis()

plt.grid(axis="x", linestyle="--", alpha=0.5)

for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.05,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.2f}",
        va="center",
        ha="left",
        fontsize=9,
        color="black",
    )

plt.tight_layout()
plt.show()